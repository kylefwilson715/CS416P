import numpy as np
import wave
import sys

# Constants
FS = 48000       # sample rate
BAUD = 300       # bits per second
N = FS // BAUD   # 160 samples per bit
F0 = 2025        # space (0)
F1 = 2225        # mark (1)

# Precompute reference arrays once
n = np.arange(N)
cos0 = np.cos(2 * np.pi * F0 * n / FS)
sin0 = np.sin(2 * np.pi * F0 * n / FS)
cos1 = np.cos(2 * np.pi * F1 * n / FS)
sin1 = np.sin(2 * np.pi * F1 * n / FS)

def tone_power(block, cos_ref, sin_ref):
    I = np.dot(block, cos_ref)
    Q = np.dot(block, sin_ref)
    return I*I + Q*Q

# Read WAV
with wave.open(sys.argv[1], 'rb') as f:
    raw = f.readframes(f.getnframes())

samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

# Decode bits
num_bits = len(samples) // N
bits = []
for i in range(num_bits):
    block = samples[i*N : i*N + N]
    p0 = tone_power(block, cos0, sin0)
    p1 = tone_power(block, cos1, sin1)
    bits.append(1 if p1 > p0 else 0)

# 8N1 framing: every 10 bits = 1 byte
message = []
for i in range(0, len(bits) - 9, 10):
    start = bits[i]
    data  = bits[i+1:i+9]   # 8 data bits, LSB first
    stop  = bits[i+9]

    if start != 0 or stop != 1:
        continue  # bad frame, skip

    byte = 0
    for bit_pos, bit in enumerate(data):
        byte |= bit << bit_pos  # LSB first

    message.append(chr(byte))

result = ''.join(message)
print(result)

with open('message.txt', 'w') as f:
    f.write(result)
