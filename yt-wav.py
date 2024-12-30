import yt_dlp
from pydub import AudioSegment
import os
import subprocess


def download_audio_from_youtube(url, output_path):
    """
    Downloads the audio from a YouTube URL and returns the file path of the downloaded audio.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, 'downloaded_audio.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        audio_file = os.path.join(
            output_path, 'downloaded_audio.' + info_dict['ext'])
        return audio_file


def convert_using_ffmpeg(input_audio_path, output_wav_path):
    """
    Converts an audio file to 16kHz WAV using FFmpeg.
    """
    command = [
        "ffmpeg",
        "-i", input_audio_path,   # Input file
        "-ar", "16000",           # Set the sample rate to 16kHz
        "-ac", "1",               # Mono audio
        "-vn",                    # No video
        output_wav_path           # Output file
    ]
    subprocess.run(command, check=True)
    print(f"Audio saved as {output_wav_path}")


def main():
    youtube_url = "https://www.youtube.com/watch?v=idz2tedwyRc"  # Your YouTube URL
    # Specify your output directory
    output_path = "/Users/abdirahman/Desktop/final_model"
    output_wav_path = os.path.join(output_path, "output_16k.wav")

    os.makedirs(output_path, exist_ok=True)

    try:
        print("Downloading audio from YouTube...")
        downloaded_audio_path = download_audio_from_youtube(
            youtube_url, output_path)

        print("Converting to 16kHz WAV...")
        convert_using_ffmpeg(downloaded_audio_path, output_wav_path)

        os.remove(downloaded_audio_path)
        print("Process complete!")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
