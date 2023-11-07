# OpenAI-audio-whisper

## Overview

The OpenAI-audio-whisper project provides two functions: `slice_audio` and `audio_transcription`. These functions offer convenient audio processing capabilities.

### `slice_audio`

`slice_audio` allows you to effortlessly divide an audio file into smaller, manageable slices. This function is useful for tasks such as transcription or analyzing specific segments of audio.

**Required parameters:**

- `filename`: The name of the audio file.
- `time`: The duration of each slice.
- `directory`: The location where the audio slices will be saved.

### `audio_transcription`

`audio_transcription` converts audio files into text, facilitating tasks like generating transcripts from spoken content.

**Required parameter:**

- `file_path`: The path to the audio file for transcription.

## Project Customization

Within this project, you have the flexibility to customize the "slice_data" or "data" folder according to your specific needs.

## Supported Audio Format

Please note that the `audio_transcription` function currently only supports the mp3 format.

---

_If you have any questions or encounter any issues, please don't hesitate to reach out to us._
