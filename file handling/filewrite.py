file=open("first.txt","w");
w="Hello users!!"
l=["This is first line\n"
    "This is second line\n"]
file.write(w)
file.writelines(l)
file.close()
