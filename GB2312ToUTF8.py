"""
Input: Document with GB2312 encoding
Output: Document with UTF-8 encoding

Written by: Liz ZHANG
Date: 02/21/2016
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os


def change_encode(fin):
    # Get input file name fron the input path
    filename = fin.split('/')[-1]
    # Get the position for the last occurance of '/' to split the path and the filename
    position = fin.rfind('/')
    if position < 0:
        # Input file is in the current folder
        path = os.path.dirname(os.path.realpath(fin))
    else:
        path = fin[:position]

    # Expand "out_" prefix to the filename for the out file
    fout = "out_"+filename
    while os.path.isfile(path+'/'+fout):
        # Make sure to have one more "out_" prefix for the out file, so that no file will be overwritten
        fout = "out_"+fout

    # If the input file does not exist
    if not os.path.isfile(fin):
        print "Error: No such file!"
        sys.exit(2)

    # Convert encoding
    content = open(fin, 'r').read().decode('gb2312')
    outpath = path+'/'+fout
    fo = open(outpath, 'w')
    fo.write(content.encode('utf8'))
    print ("Congratulations: Convert Successfully!")


def main(argv):
    # Wrong argument number
    if len(argv) != 2:
        print("Error: Wrong argument number.")
        sys.exit(2)
    fin = argv[1]
    # Not txt file
    if not fin.endswith('.txt'):
        print("Error: Please choose a txt file. Format: python GB2312ToUTF8.py path/to/input/text_file.txt")
        sys.exit(2)
    change_encode(fin)


if __name__ == '__main__':
    main(sys.argv)
