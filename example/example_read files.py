# Write and read files.py

outfile = open("20181016.txt","w")
outfile.writelines(["Hello", " ", "world"])
outfile.close()
infile = open("20181016.txt","r")
a = infile.read()
print(a)
