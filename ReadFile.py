#Import test file
f=open("/Users/JacobRaymond 1/Desktop/Ex_Files_Python_Automation/Exercise Files/inputFile.txt", "r")
for line in f:
    line_split=line.split()
    if line_split[2]=="P":
        print(line)
f.close()