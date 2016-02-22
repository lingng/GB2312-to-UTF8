##GB2312 to UTF-8 Converter
====
####Introduction
Allow users to convert a text file with GB2312 encoding to UTF-8 encoding.

####Usage
Please use the following command line to run the script:

	python GB2312ToUTF8.py path/to/input/text_file.txt
	
* The output file will be in the same folder as the input file. 
* The name for the output file will have a prefix "out_". 
* The script will automatically expand one more "out_" prefix to avoid overwrite other text file with the same file name.

====
#### 简介
用户可使用此脚本将GB2312编码的txt文件转换为UTF8编码的txt文件。
#### 使用方法介绍
请在终端使用如下命令执行该脚本：
	
	python GB2312ToUTF8.py path/to/input/text_file.txt
	
* 输出文件与输入文件在同一文件夹中.
* 输出文件名将包含"out_"前缀，以此与输入文件区分开。
* 如若文件夹内已包含带有"out\_"前缀文件名的文件，该脚本会通过多增添一个"out\_"前缀的方式，避免覆盖原有文件。