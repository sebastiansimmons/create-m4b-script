#
#
#
#
import sys
import os

from pydub import AudioSegment

def convertToSingleFile(folder):
    """Converts a list of mp3 files to a single m4b (apple audiobook) format"""
    path = os.getcwd() + "\\" + folder  # This might be unnecessary
    files = []
    loop = 0
    segments = []
    output = AudioSegment.empty()
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
            for file in f:
                if file.endswith(".mp3"):
                    files.append(os.path.join(r, file))
                    #print("LOADING: " +  os.path.join(r, file))
                    #output = output + (AudioSegment.from_mp3(folder + "\\" +file))


    #big = output.export("output.mp3", format="mp3")
    output.export("output.mp3", format="mp3")
    file = open("mylist.txt","w")

    for f in files:
        file.write("file '" + f + "'\n")
    file.close() 

    os.system("ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp3")

    os.system("ffmpeg -i output.mp3 output.m4b\nrm " + os.getcwd()+ "\\output.mp3")



def viewAllSubDirs(path):
    folders = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))

    for f in folders:
        print(f)
    

def viewAllFiles(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        print(f)



if __name__ == "__main__":
    # Create check for proper arguments
    if not sys.argv[1]:
        print("python convert-audiobook.py <directory filled with mp3s>")
    else:
        convertToSingleFile(sys.argv[1])
