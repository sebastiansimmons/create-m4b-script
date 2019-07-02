import sys
import os

from pydub import AudioSegment

def convertToAudiobook(directory):
    path = os.getcwd() + "\\" + directory
    files = []
    output = AudioSegment.empty()
    output.export("output.mp3", format="mp3")
    
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file.endswith(".mp3"):
                files.append(os.path.join(r, file))

    mylist = open("mylist.txt","w")
    for file in files:
        print(file)
        mylist.write("file '" + file + "'\n")               #FFMPEG uses a .txt file for the concat command
    mylist.close()

    os.system("ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp3")
    os.system("rm mylist.txt")
    os.system("ffmpeg -i output.mp3 " + "output.m4b")
    os.system("rm output.mp3")

def checkFiles(directory):
    path = os.getcwd() + "\\" + directory
    files = []
       # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file.endswith(".mp3"):
                print(os.path.join(r, file))

    return

if __name__ == "__main__":
    # Create check for proper arguments
    if sys.argv[1] == '-l':
        checkFiles(sys.argv[2])
    else:
        convertToAudiobook(sys.argv[1])
