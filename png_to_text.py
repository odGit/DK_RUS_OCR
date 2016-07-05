# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:33:18 2014

@author: olgis
DONE: get all pictures in folder
DONE: save TEXT into file

"""

import Image
import pytesseract
import os
import sys
import glob


def main():
    png_path = sys.argv[1]
    #file_path = os.getcwd()  # current directory
    png_list = glob.glob(png_path + "/*.png")
    list_len = len(png_list)
    print "There are %s files in  selected folder" % list_len
    
    for item in xrange(len(png_list)): 
        print "Processing %s out of %s" %(item+1, list_len)
        png_to_text(png_list[item])
    

def png_to_text(png_file):
    if not os.path.isfile(png_file):
        print "'%s' is not a file. Skip." % png_file

    png_name, ext = os.path.splitext(png_file)
    
    out_rus = pytesseract.image_to_string(Image.open(png_file), lang = 'rus')
    
    with open(png_name + "_RU.txt", 'w+') as ru_f:
        ru_f.write(out_rus)

    
    out_dan = pytesseract.image_to_string(Image.open(png_file), lang = 'dan')
    
    with open(png_name + "_DK.txt", "w+") as dk_f:
        dk_f.write(out_dan)
                         
if __name__ == "__main__":
    main()                         