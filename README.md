# AI Video Transcription System

## Overview
This project is an end-to-end AI-based video transcription system built using OpenAI Whisper.

It converts video files into:
- Plain text transcripts (.txt)
- Subtitle files (.srt)

## Features
- Offline transcription
- Automatic language detection
- Timestamped subtitles
- Modular architecture
- Clean and readable code

## Tech Stack
- Python
- PyTorch
- Whisper
- FFmpeg

## Project Structure
video_transcriber/
│
├── main.py
├── transcriber.py
├── utils.py
├── output/

## Installation

1. Create environment:
conda create -n transcriber python=3.10
conda activate transcriber

2. Install dependencies:
pip install -r requirements.txt

3. Install FFmpeg:
conda install -c conda-forge ffmpeg

## Usage

Run:
python main.py

Enter video path when prompted.

Outputs will be saved inside the output/ directory.

## Future Improvements
- Streamlit Web Interface
- REST API version
- Transcript summarization
- Speaker diarization
