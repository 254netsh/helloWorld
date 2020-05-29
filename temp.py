fo = open("myFile.txt","w+")

fo.write("hello world\n this is my first file\n am writting from code")

fo = open("myFile.txt","r+")
str=fo.read()
print(str)
fo.close