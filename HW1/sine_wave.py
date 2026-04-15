

import numpy as np
import scipy.io.wavfile as wavfile
import sounddevice as sd

# Parameters 
SAMPLE_RATE  = 48000          # samples per second
FREQUENCY    = 440            # Hz
DURATION     = 1.0            # seconds
MAX_AMP      = 32767          # 16-bit signed max
QUARTER_AMP  = MAX_AMP // 4   # 8191 (≈ 8192 per spec)
HALF_AMP     = MAX_AMP // 2   # 16383 (≈ 16384 per spec)
CLIP_LIMIT   = QUARTER_AMP    # hard-clip threshold

# Generate time axis
n_samples = int(SAMPLE_RATE * DURATION)
t = np.linspace(0, DURATION, n_samples, endpoint=False)

# Part 1 — ¼-amplitude sine wave
sine_samples = (QUARTER_AMP * np.sin(2 * np.pi * FREQUENCY * t)).astype(np.int16)
wavfile.write("sine.wav", SAMPLE_RATE, sine_samples)
print("Wrote sine.wav")

# Part 2 — ½-amplitude sine wave, hard-clipped at ¼ amplitude
clipped_float = HALF_AMP * np.sin(2 * np.pi * FREQUENCY * t)
clipped_float = np.clip(clipped_float, -CLIP_LIMIT, CLIP_LIMIT)
clipped_samples = clipped_float.astype(np.int16)
wavfile.write("clipped.wav", SAMPLE_RATE, clipped_samples)
print("Wrote clipped.wav")

# Part 3 — Play clipped wave directly 
# sounddevice wants float32 in [-1.0, 1.0]
playback = (clipped_float / MAX_AMP).astype(np.float32)
print("Playing clipped sine wave…")
sd.play(playback, samplerate=SAMPLE_RATE)
sd.wait()
