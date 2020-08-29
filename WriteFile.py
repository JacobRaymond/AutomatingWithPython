#Import test file
f=open("/Users/JacobRaymond 1/Desktop/Ex_Files_Python_Automation/Exercise Files/inputFile.txt", "r")
#Create new file
passFile=open("PassFile.txt", "w")
failFile = open("FailFile.txt", "w")
for line in f:
    line_split=line.split()
    if line_split[2]=="P":
        passFile.write(line)
    else:
        failFile.write(line)  # Updates the created file
f.close()
passFile.close()
failFile.close()