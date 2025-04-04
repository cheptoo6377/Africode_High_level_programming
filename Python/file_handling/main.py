#file input output
#open ()
#append,write ,read
#close()
# open("file","mode")
#modes 
#r -read read a file that must exist
#w -write
#w -write
#a -append
#x -exclusive creation
#t -text mode
#b -binary mode read and write file using binary mode 


# print(f.read())
# f.close()
# f = open("output.txt","w")
# f.write("this is another file")
# f.write("this content will overide the existing one")
# f.close()\
#appendfile_handling/isspice.jpg
# f = open("test.txt","a")
# f.write("this is added at the end of the file ")
# f.close()
#binary
# b = open("image.jpg","+rb")
# # print(f.read())
# #copy
# for data in b:
# #     open("copied.jpg","wb") as f:
#  with open("copied.jpg","wb") as b:
    #do something to file
with open("image.jpg","rb") as b:
    for data in b:
        print(data)
        with open("copied.jpg","wb") as f:
            f.write(data)




