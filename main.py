import os
from transcriber import VideoTranscriber
from utils import save_txt, save_srt

def main():
    video_path = input("Enter video file path: ")

    os.makedirs("output", exist_ok=True)

    transcriber = VideoTranscriber(model_size="tiny")

    result = transcriber.transcribe_video(r"C:\Users\joshi\Desktop\VideoAudioExtraction\DemoVideo.mp4")

    txt_path = "output/transcript.txt"
    srt_path = "output/subtitles.srt"

    save_txt(result["text"], txt_path)
    save_srt(result["segments"], srt_path)

    print("\nTranscription completed successfully!")
    print(f"Transcript saved at: {txt_path}")
    print(f"SRT saved at: {srt_path}")

if __name__ == "__main__":
    main()