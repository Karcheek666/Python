# import os,shutil,os.path,pathlib
import os as os
from os import *
import shutil as sh
from shutil import *


# Create needed variables
wr_dir = '/Users/hyper/Downloads'
au_dir = '/Users/hyper/Music'
pic_dir = '/Users/hyper/Pictures'
vid_dir = '/Users/hyper/Videos'
txt_dir = '/Users/hyper/Documents'
zip_dir = '/Users/hyper/Downloads/zip'
rar_dir = '/Users/hyper/Downloads/rar'
exe_dir = '/Users/hyper/Downloads/Software'
iso_dir = '/Users/hyper/Downloads/iso'
tor_dir = 'User/hyper/Downloads/torrents'
full_dir = os.path.join


# Create Read function
def main():
    # Read Filenames
    for dirname, dirnames, filenames in os.walk(wr_dir):
        for filename in filenames:
            source = full_dir(dirname, filename)
            # Create Sort and move function
            # Move file to respective directories
            # MP3 to audio
            if filename.endswith('mp3'):
                sh.move(source, full_dir(au_dir, filename))
            # jpeg to pics
            elif filename.endswith('jpeg'):
                sh.move(source, full_dir(pic_dir, filename))
            # MP4 to Video
            elif filename.endswith('mp4'):
                sh.move(source, full_dir(vid_dir, filename))
            # txt documents
            elif filename.endswith('txt'):
                sh.move(source, full_dir(txt_dir, filename))
            # Sorting Software
            elif filename.endswith('zip'):
                sh.move(source, full_dir(zip_dir, filename))
            elif filename.endswith('rar'):
                sh.move(source, full_dir(rar_dir, filename))
            elif filename.endswith('exe'):
                sh.move(source, full_dir(exe_dir, filename))
            elif filename.endswith('iso'):
                sh.move(source, full_dir(iso_dir, filename))
            elif filename.endswith('torrent'):
                sh.move(source, full_dir(tor_dir, filename))    
            else:
                pass
        pass
    pass

# Call function
if __name__ == '__main__':
    main()