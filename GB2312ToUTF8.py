"""
Input: Document with GB2312 encoding
Output: Document with UTF-8 encoding
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def change_encode(fin):
    filename = fin.split('/')[-1]

    position = fin.rfind('/')
    path = fin[:position]

    fout = "out_"+filename

    content = open(fin, 'r').read().decode('gb2312')
    outpath = path+'/'+fout
    fo = open(outpath, 'w')
    fo.write(content.encode('utf8'))
    print ("Congratulations: Convert Successfully!")


def main(argv):
    if len(argv) != 2:
        print("Error: Wrong argument number.")
        sys.exit(2)

    fin = argv[1]

    if not fin.endswith('.txt'):
        print("Error: Please choose a txt file. Format: python GB2312ToUTF8.py path/to/input/text_file.txt")
        sys.exit(2)

    change_encode(fin)


if __name__ == '__main__':
    print ("This python script allows you to transfer a GB2312 encoded text file to UTF-8 encoded text file. The output file will be stored in the same folder with the input file, with a prefix of \"out_\". Please use the following format to run the script: \npython GB2312ToUTF8.py path/to/input/text_file.txt")
    print ("===============================================")
    main(sys.argv)
