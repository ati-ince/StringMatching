import os
import codecs

#sample read a file... with true codec...
''' 
f = codecs.open('Str-EN_O2.txt', encoding='cp857') # cp857 for turkish
for line in f:
    print ((line))
'''

#### NOTE: One project folder have to 2 file and other has to 1 file. And 1 file should be referance for string matching and creating...

ProjFolderName=['G8', 'O2']
ProjDirs=[] #lists
StringFileNumber=[] #
fileindex=0

for i in range(len(ProjFolderName)):
    ProjDirs.append(os.getcwd()+'\\'+ProjFolderName[i])
    print("Directories:"), print(ProjDirs[i])  # get directories
    filesbuf= os.listdir(ProjDirs[i])
    for name in filesbuf:
        if ".txt" in name:
            fileindex=fileindex+1
            print(name)
    StringFileNumber.append(fileindex)
    print("string file number=" + str(StringFileNumber[i]))
    fileindex=0
    print("*********************")

#then, we choose 1 file folder should be referance for string ordeer..
# lets take ref file for order
directoryF=ProjDirs[(StringFileNumber[0] > StringFileNumber[1])]
for name in os.listdir(directoryF):
    if ".txt" in name:
        RefFile=directoryF+'\\'+name
        print(RefFile) # finally, get the file which ref for us...







'''
files = os.listdir(Proj2Dir)
for name in files:
    if ".txt" in name:
        print(name) '''