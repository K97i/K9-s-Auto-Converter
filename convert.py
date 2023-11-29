import os
import sys
import ffmpeg

def convert(file: str):
    path = file.rsplit('\\', 1)[0]

    filename = file.rsplit('\\', 1)[1].rsplit('.',1)[0]
    filetype = file.rsplit('\\', 1)[1].rsplit('.',1)[1]

    print(f"\033[94mProcessing: {filename}.{filetype}\033[0m")

    if filetype.lower() in ["mkv", "mov"]:
        # Converts .mkv or .mov to .mp4
        dest_filetype = ".mp4"

    elif filetype.lower() in ["mp3", "m4a"]:
        # Converts .mp3 or .m4a to .wav
        dest_filetype = ".wav"

    else:
        print("Not supported!")
        return

    (
        ffmpeg
        .input(file)
        .output(path + "\\\\" + filename + dest_filetype)
        .run()
    )
    
if __name__ == "__main__":

    sys.argv.pop(0)

    if sys.argv:
        for file in sys.argv:
            convert(file)

    else:
        file = input("Enter the path to the file: ")

        if os.path.isfile(file):
            convert(file)
        
        else:    
            print("Malformed input!")