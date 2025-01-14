# FILE HANDLING
#7.1
#filee=open("labText","x")
file=open("labText.txt","w")
file.write("This is a newly created Text file")
file.close()
file=open("labText.txt","r")
print(filee.read())
file.close()
#7.2
file=open("labText.txt","a")
file.write(" on part 7.2")
file.close()
file=open("labText.txt","r")
print(file.read())
file.close()
#7.3
with open("textFile.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)
