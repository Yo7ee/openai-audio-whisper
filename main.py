import os
import openai

from dotenv import load_dotenv
from pydub import AudioSegment

import argparse

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-s', '--slice_audio',
        type = str,
        help = 'To slice the audio to fit the volumne under 25MB.'
    )


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# folder path setting
# put original audio
data_dir = os.path.join(os.path.dirname(__file__), 'data')

# put slice audio
slice_data_dir = os.path.join(os.path.dirname(__file__), 'slice_data')

def audio_transcription(filepath):
    audio_file= open(filepath, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file) #{"test":"audio content"}

    #transcript = { "text": "abc adf asd {0}".format(filepath)} #測試用
    write_into_txt = "{0} ".format(transcript["text"])
    with open("2327_183_20231026.txt", 'a+') as f:
        f.write(write_into_txt)

def slice_audio(filename, minutes, slice_data_dir):
    data_path = os.path.join(data_dir, "{0}.mp3".format(filename))
    song = AudioSegment.from_mp3(data_path)

    # PyDub handles time in milliseconds
    slice_minutes = minutes * 60 * 1000

    for i, chunk in enumerate(song[::slice_minutes]):
        filename_with_path = os.path.join(slice_data_dir, filename)
        chunk.export("{0}_{1}.mp3".format(filename_with_path, i), format="mp3")


if __name__ == "__main__":
    slice_audio("2327_183_20231026", 15, slice_data_dir)

    # slice_files = os.listdir(slice_data_dir) #[xxx, xxx, xxx]
    # for filename in slice_files:
    #     filepath = os.path.join(slice_data_dir, filename)
    #     audio_transcription(filepath)