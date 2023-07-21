"""
读写txt文件
"""
with open("./in_out/test.txt",'w') as f:#目前处于只写的状态
    f.write("hello world!\n")
    f.write("hello world!\n")
    f.write("hello world!\n")
with open("./in_out/test.txt","r") as f:
    for line in f.readlines():
        print(line)
f.close()