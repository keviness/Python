# try read and write files.py

outfile = open("newfiles.txt", "w")
outfile.writelines(["hello", ",", "the world", "!"])
outfile.close()
infile = open("newfiles.txt", "r")
a = infile.read()
print(a)
