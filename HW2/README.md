# Bell 103 Modem Decoder

**Kyle Wilson**

## Overview

A decoder for audio messages encoded using the Bell 103 modem protocol 

## Process

Going into this I had a loose understanding for what FSK was but had never actually implemented
anything like it. The concept of using dot products to detect frequencies clicked pretty quickly
once I thought about it as "how much does this block of audio resemble a reference sine wave".

Getting it running was satisfying. Feeding it some test files first  before running it on my own message was a good sanity check and made
the final decode feel pretty simple. Everything is up and running now with nothing to keep working at.

## Usage

```bash
python decode.py message.wav
```

Prints the decoded message and writes it to `mesasge.txt`.

## Dependencies

- Python 3
- numpy
