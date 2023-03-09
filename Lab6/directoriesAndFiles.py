import string
import os
os.chdir("Lab6")

def test1(path):
    dirs,files,all=[],[],[]
    for dirpach,dirnames,filenames in os.walk(path):
        for dirname in dirnames:
            dirs.append(os.path.join(dirpach,dirname))
            all.append(os.path.join(dirpach,dirname))
        for filename in filenames:
            files.append(os.path.join(dirpach,filename))
            all.append(os.path.join(dirpach,filename))
    print(*dirs)
    print("\n",*files)
    print("\n",*all)

def test2(path):
    print("File Exists: ", os.access(path, os.F_OK))
    print("For Read: ", os.access(path, os.R_OK))
    print("For Writing: ", os.access(path, os.W_OK))
    print("Executable: ", os.access(path, os.X_OK))

def test3(path):
    print("Path exists: ", os.path.exists(path))
    print("Filename: ", os.path.basename(path))

def test4(path):
    with open(path,"r") as file:
        print(len(file.readlines()))

def test5(path,list):
    with open(path,"w") as file:
        for i in list:
            file.write(f"{i}\n")

def test6():
    if not os.path.isdir("Letters"):
        os.mkdir("Letters")
    os.chdir("Letters")
    for i in string.ascii_uppercase:
        with open(i+".txt","w") as file:
            file.write("")

def test7(path1,path2):
    with open(path1,"r") as file:
        text=file.read()
    with open(path2,"w") as file:
        file.write(text)

def test8(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("No such file")
        
# test1(".")
# test2(".")
# test3(".")
# test4(".")
# test5("example.txt",[1,2,3,4,5])
# test6()
# test7("example.txt","example2.txt")
# test8("example.txt")
