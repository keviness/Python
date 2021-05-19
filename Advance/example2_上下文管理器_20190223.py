#example2_上下文管理器_20190223
read_file = open("NewPython.txt")
write_file = open("NewPython_1.txt", "w")
try:
    for line in read_file:
        write_file.write(line)
finally:
    read_file.close()
    write_file.close()
