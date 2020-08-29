import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

#Find files from the "Organize Me" exercize file with specific extension
def pickDirectory(value): #Create function
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix==value:
                return category
    return "Misc"
print(pickDirectory(".pdf")) #Example; shows that "pdf" is in the DOCUMENTS category

#Organize the file
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath=Path(item)
        filetype=filePath.suffix.lower()
        directory=pickDirectory(filetype)
        directoryPath=Path(directory)
        if directoryPath.is_dir()!=True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()

#Run in terminal with cd /Users/JacobRaymond\ 1/Desktop/Ex_Files_Python_Automation/Exercise\ Files/OrganizeMe