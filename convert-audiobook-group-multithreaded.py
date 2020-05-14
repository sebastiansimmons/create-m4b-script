import sys
import os
from multiprocessing import Pool

from pydub import AudioSegment

def checkFiles(directory):
    path = os.getcwd() + "\\" + directory
    files = []
       # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if file.endswith(".mp3"):
                print(os.path.join(r, file))

    return

def worker(info):
        filename = info['filename']

        title = info['title']
        author = info['author']
        outputdir = info['outputdir']
        index = info['index']
        newFile = 'track' + str(index) +".m4b"

        ffmpeg = "ffmpeg -i \"" + filename + "\" -vn "
        ffmpeg += "-metadata track={0}/{1} ".format(index + 1, info['out_of'])
        ffmpeg += "-metadata album=\"" + title + "\" "
        ffmpeg += "-metadata title=\"" + title + "\" "
        ffmpeg += "-metadata author=\"" + author + "\" "
        ffmpeg += outputdir + "\\" + newFile
        print(ffmpeg)
        os.system(ffmpeg)     
  

if __name__ == "__main__":
    # Create check for proper arguments
    if sys.argv[1] == '-l':
        checkFiles(sys.argv[2])
    else:
        directory = sys.argv[1]

        path = os.getcwd() + "\\" + directory
        files = []

        title = input("Title:\n>")
        author = input("Author:\n>")
        outputdir = input("dir name:\n>")
        converted_count = 0

        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if file.endswith(".mp3"):
                    converted_count += 1
                    info = {'filename':os.path.join(r, file),
                            'title':title,
                            'author':author,
                            'outputdir':outputdir,
                            'index':converted_count}
                    files.append(info)
                    
        for item in files:
            item['out_of'] = len(files)
        os.mkdir(outputdir)
        num_processes=min(converted_count, os.cpu_count())
        p = Pool(processes=num_processes)
        p.map(worker, files)

        
