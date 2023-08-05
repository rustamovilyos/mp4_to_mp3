import moviepy.editor
from pathlib import Path


def audio_converter():
    video_file = Path("angel.mp4")
    video = moviepy.editor.VideoFileClip(f"{video_file}")
    audio_file = video.audio
    audio_file.write_audiofile(f"{video_file.stem}.mp3")


if __name__ == "__main__":
    audio_converter()
