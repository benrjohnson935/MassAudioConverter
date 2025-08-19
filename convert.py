import pydub
import os

def get_type(file_name):
    return file_name[-3:]

def mass_convert(read_path, write_path, type="mp3"):

    for root, dirs, files in os.walk(read_path):
        for file_name in files:
            print(f"Converting {file_name}...\n")
            get_type(file_name)
            try:
                audio = pydub.AudioSegment.from_file(read_path + file_name, format="m4a")
            except:
                print(f"{file_name} is of unsupported type. Skipping...\n", file_name)
                continue
            final_name = write_path + file_name[:-4] + "." + type
            audio.export(final_name, format=type)