# HW1 — Sine Wave & Clipping
Running program does the following:

1. **`sine.wav`** — a 1-second, 440 Hz, mono, 16-bit PCM sine wave at ¼ maximum amplitude (peak ≈ 8192).
2. **`clipped.wav`** — the same wave generated at ½ amplitude (peak ≈ 16384), then hard-clipped symmetrically at ¼ amplitude (±8192). The flat tops and bottoms give it the characteristic "fuzz" distortion of a symmetrical diode hard-clip circuit.
3. **Plays** the clipped wave directly to your audio output via `sounddevice` — samples are generated in memory and sent straight to the speaker, no file read-back.

## How it went

Straightforward once the parameters were clear. The main gotcha was the `sounddevice` playback format: it wanted `float32` in `[-1.0, 1.0]`, so the integer samples need to be normalized by dividing by 32767 before passing them in. `np.clip` makes the hard-clipping a one-liner.

## Dependencies

- Python 3.12+
- numpy
- scipy
- sounddevice

```
pip install numpy scipy sounddevice
```

`sounddevice` requires **PortAudio** to be installed on your system:

## Running

```
python3 sine_wave.py
```



