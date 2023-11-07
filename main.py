import os
import openai

from dotenv import load_dotenv
from pydub import AudioSegment


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
SLICE_DATA_DIR = os.path.join(os.path.dirname(__file__), 'slice_data')
TRANSCRIPT_AND_AUDIO_FILENAME= "2327_183_20231026"

def audio_transcription(filepath, exportFilename):
    audio_file= open(filepath, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file) #{"test":"audio content"}

    write_into_txt = "{0} ".format(transcript["text"])
    with open("{0}.txt".format(exportFilename), 'a+') as f:
        f.write(write_into_txt)

def slice_audio(filename, minutes, SLICE_DATA_DIR):
    data_path = os.path.join(DATA_DIR, "{0}.mp3".format(filename))
    song = AudioSegment.from_mp3(data_path)

    # PyDub handles time in milliseconds
    slice_minutes = minutes * 60 * 1000

    for i, chunk in enumerate(song[::slice_minutes]):
        filename_with_path = os.path.join(SLICE_DATA_DIR, filename)
        chunk.export("{0}_{1}.mp3".format(filename_with_path, i), format="mp3")


if __name__ == "__main__":
    slice_audio(TRANSCRIPT_AND_AUDIO_FILENAME, 15, SLICE_DATA_DIR)

    slice_files = os.listdir(SLICE_DATA_DIR) #[xxx, xxx, xxx]
    for filename in slice_files:
        filepath = os.path.join(SLICE_DATA_DIR, filename)
        audio_transcription(filepath, TRANSCRIPT_AND_AUDIO_FILENAME)