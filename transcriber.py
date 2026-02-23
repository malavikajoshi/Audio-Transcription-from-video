import whisper
import os

class VideoTranscriber:
    def __init__(self, model_size="base"):
        print("Loading Whisper model...")
        self.model = whisper.load_model(model_size)
        print("Model loaded successfully.")

    def transcribe_video(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError("Video file not found.")

        print("Starting transcription...")
        result = self.model.transcribe(video_path)

        return result

