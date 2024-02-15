import os
import sys
import ffmpeg

def convert(file: str):
    path, filename = os.path.split(file)
    filename, filetype = filename.rsplit('.', 1)
    
    print(f"\033[94mProcessing: {filename}{filetype}\033[0m")

    if filetype.lower() in ["mkv", "mov"]:
        # Converts .mkv or .mov to .mp4
        dest_filetype = ".mp4"

    elif filetype.lower() in ["mp3", "m4a"]:
        # Converts .mp3 or .m4a to .wav
        dest_filetype = ".wav"
        
    elif filetype.lower() in ["wav"]:
        # Converts .wav to .mp3 for Discord Sharing
        dest_filetype = ".mp3"

    else:
        print("Not supported!")
        return

    (
        ffmpeg
        .input(file)
        .output(path + dest_filetype)
        .run()
    )
    
if __name__ == "__main__":

    # If you drag-and-drop a file to the PyInstaller-ed script, 
    # the paths of the files are added to the arguments.

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