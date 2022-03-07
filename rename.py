#!/usr/bin/env python3

'''
Author: Me


                         WHAT THE SCRIPT DOES:
Rename *.srt to video file.srt and moves from Subs folder to video file folder.
removes .txt and .exe file and Subs folder
'''

import os


def diff_path(vid,sub):
    vid_path = vid
    sub_path = sub
    sub_format =".srt"
    vidFiles = []
    subFiles = []
    for name in os.listdir(vid_path):
        if (name.endswith('.mp4') or name.endswith('.mkv') or name.endswith('.avi')):
            vidFiles.append(name)
    for name in os.listdir(sub_path):
        if (name.endswith(sub_format)):
            subFiles.append(name)
    rename_files(vid_path,sub_path, vidFiles, subFiles, sub_format)
    return 



def rename_files(vid_path, subpath, vidFiles, subFiles, sub_format):
    vidFiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    subFiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    os.chdir(vid_path)
    try:
        assert(len(subFiles)==len(vidFiles))
        for i,vname in enumerate(vidFiles):
            print("{0} renamed to {1} ".format(subFiles[i], os.path.splitext(vname)[0]+sub_format))
            os.rename(subpath+'/'+subFiles[i],vid_path+'/'+os.path.splitext(vname)[0]+sub_format)
            print('Remove Subtitile folder')
            os.rmdir(subpath)
            print('Remove RARBG.txt')
            os.remove(vid_path+'/RARBG.txt')
            print('Remove RARBG_DO_NOT_MIRROR.exe')
            os.remove(vid_path+'/RARBG_DO_NOT_MIRROR.exe')
    except AssertionError:
        print(len(subFiles))
        print(len(vidFiles))
    return 


def main():
    dir_path ='/home/pi/rename/downloaded'
    directories_to_check=os.listdir(dir_path)
    for i in range(len(directories_to_check)):
        diff_path(dir_path +"/"+ directories_to_check[i],dir_path +"/"+ directories_to_check[i] +"/Subs")

main()

