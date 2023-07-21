"""
读写txt文件
"""
with open("./in_out/test.txt",'+w') as f:#目前处于只写的状态
    f.write("hello world!")
f.close()