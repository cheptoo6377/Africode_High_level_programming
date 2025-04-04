#read
with open("newfile.txt","r") as f:
    content = f.read()
    print(content)
#append
with open("newfile.txt","a") as f:
    f.write("this is a new line we are creating")
    #binary
    with open("/home/dorothy/Documents/my_projects/Africode_High_level_Programming/Python/file_handling/is.jpg","rb") as b:
        for data in b:
            with open("c.jpg","wb") as f:#new file created
                f.write(data)