import sys
import os
import glob
from shutil import copyfile


def fileToStr(fileName):
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def make_html(source_path,demo_name):
    # output directory is hardwired
    out_audio_dir = 'audio'
    out_dir_rel = os.path.join('html',out_audio_dir)
    
    # title is easy
    title = demo_name
    
    # deal with files
    # - create empty string
    # - loop over files
    # -- copy file
    # -- append track element by substituting track template
    # - substitute list of tracks into player template
    
    
    track_list = []
    search_str = source_path + '/*.wav'
    input_files = glob.glob(search_str)
    for inpath in input_files:
        track_name = os.path.basename(inpath)
        track_path = os.path.join(out_audio_dir,track_name)
        copyfile(inpath,os.path.join(out_dir_rel,track_name))
        track_list.append(fileToStr('trackTemplate.html').format(**locals()))
    track_list = ''.join(track_list)    
    player = fileToStr('playerTemplate.html').format(**locals())
    contents = fileToStr('indexTemplate.html').format(**locals())
    strToFile(contents, 'html/index.html')

if __name__ == "__main__":
    demo_name = 'Audio demo'
    if len(sys.argv) < 2:
        print("Usage python make_html.py path_to_audio [demo_name]")
    else:
        source_path = sys.argv[1]
        if len(sys.argv) > 2:
            demo_name = sys.argv[2]
        make_html(source_path,demo_name)