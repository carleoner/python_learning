from asyncore import read, write

# open(file_name, access_mode)
# read mode
# r - read only at beg, rb - read in binary format at beg
# r+ - read and write at beg, rb+ - read and write in binary format
# write mode
# w - write only, overwrite file if exist, if not create a file
# wb - write in binary format cond same as up
# w+ - write and read same cond as up
# wb+ - wrirte and read in binary format same cond as up
# append mode
# a - append, pointer at the end
# ab - append in binary format
# a+ - append and read
# ab+ - append and read in binary format


fp = open("../data/13_data.txt", 'r')
print(fp.read())
fp.close()

# read() - until EOF
# read(size) - until size
# readline()
# readlines() - until EOF

fp = open("../data/13_data.txt", 'a')
data = "so here I am\nand now here"
fp.write(data)
fp.close()

# pointer position
#fp.tell()
#fp.seek(position, from)

fp = open("../data/13_data.txt", 'r')
print(f"Pointer position before reading is: {fp.tell()}")
fp.seek(5)
print(f"Pointer position after seek func is: {fp.tell()}")
fp.read()
print(f"Pointer position after reading is: {fp.tell()}")
fp.close()