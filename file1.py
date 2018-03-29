#coding:utf-8

# This program demonstrat that the instruction: content = file.read() read all the file and
#  the cursor will be in the end of the file test.txt

file = open("test.txt")   # read all the file test.txt
contentline = file.readline() # Read the first line in the file test.txt
content = file.read()      # Read all the contents of the file test.txt And the cursor is in the end of the last line
content_empty = file.read()# Nothing will displied because the cursor is already in the end of the file

file.close()
print("contentline = {} content = {} and content_empty = {}".format(contentline,content,content_empty))
