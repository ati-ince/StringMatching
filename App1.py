import os
import codecs

SelectedEncoding= 'UTF-8' # cp437 for english, which created first...  Can be change after which is fitted.. .
SelectOtherEncoding = 'cp855' # cp855 for SERbIAN for test
fileformat='.rc' #you can change

#sample read a file... with true codec...
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
        if ".rc" in name: # use file type .rc, .txt or what you want
            fileindex=fileindex+1
            print(name)
    StringFileNumber.append(fileindex)
    print("string file number=" + str(StringFileNumber[i]))
    fileindex=0
    print("*********************")

#then, we choose 1 file folder should be referance for string ordeer..
# lets take ref file for order
directoryF=ProjDirs[(StringFileNumber[0] > StringFileNumber[1])] #ref file
langdirectoryF=ProjDirs[(StringFileNumber[0] < StringFileNumber[1])] #which other lang file exist...
for name in os.listdir(directoryF):
    if fileformat in name:
        RefFile=directoryF+'\\'+name
        print("ref file: "+ RefFile) # finally, get the file which ref for us...
for name in os.listdir(langdirectoryF):
    if fileformat in name:
        if name!=RefFile.split("\\")[-1]:#last element
            LangFile = langdirectoryF + '\\' + name
            print("lang file: " + LangFile) # which other lang file wil use for creatin.. .

#lets get the string referance from refFile

f = codecs.open(RefFile, encoding=SelectedEncoding)
RefFileStringCode=[]
RefFileStringInfo=[]
for line in f:
    bufStr=str(line).split(';')
    RefFileStringCode.append(bufStr[0]) #name of string kind of , it is referance string name list and order...
    bufStr2=bufStr[1].split('"')
    RefFileStringInfo.append(bufStr2[1])
f.close()

# we get the ref list from RefFile... Now get the Othe rlang file for read and filled..

f_other = codecs.open(LangFile, encoding=SelectOtherEncoding) #select for other lang format for example serbian
LangFileStringCode=[]
LangFileStringInfo=[]
for line in f_other:
    bufStr=str(line).split(';')
    LangFileStringCode.append(bufStr[0]) #name of string kind of , it is referance string name list and order...
    bufStr2 = bufStr[1].split('"')
    LangFileStringInfo.append(bufStr2[1])
f_other.close()

print("finito file list things........................")

# lets create new file list
FileStringCode=[]
FileStringInfo=[]

# we use RefFile for ref : StringCode with Length...
for ref in range(len(RefFileStringCode)):
    for lan in range(len(LangFileStringCode)):
        if LangFileStringCode[lan]==RefFileStringCode[ref]:
            FileStringCode.append(RefFileStringCode[ref])
            FileStringInfo.append(LangFileStringInfo[lan])
            break
    if (len(FileStringCode)<=ref):
        FileStringCode.append(RefFileStringCode[ref])
        FileStringInfo.append(RefFileStringInfo[ref])

print("ref file string code and info: " + str(len(RefFileStringCode)))
print("new file string code: " + str(len(FileStringCode)) + "||" + "new file string info : " + str(len(FileStringInfo)))

#lets test is it correct?

for xx in range(len(RefFileStringInfo)):
    if RefFileStringCode[xx]==FileStringCode[xx]:
        print(FileStringCode[xx] + ";," + '"'+FileStringInfo[xx] +'"')
    else:
        print(" *** FALSE *** || " + RefFileStringInfo[xx] + " || " + FileStringInfo[xx])


#############################################################################################################################
'''  BUG - HERE !!!!! -> we open EN file with UTF-8 but, we should open other lang file with other language format
        like if we create serbian file we should open with 
        
        I corrected :) using 2 different codec I bleive...
  '''

# ok we create other lang list and lets fill the new file
## f = codecs.open(RefFile, encoding=SelectedEncoding)
# lets write true folder name firstly....
creation_path=os.path.dirname(os.path.realpath(RefFile))
lang_file_name= creation_path + '\\' + LangFile.split('\\')[-1]

print("will create file ----->>>   " + lang_file_name + " <<<<-----")

f_new = open(lang_file_name,"w") #opens file with name of "***.txt"
for line in range(len(FileStringCode)):
    f_new.write(FileStringCode[line]+";"+","+'"'+FileStringInfo[line]+'"' + '\n')

f_new.close()

print("finito bro :)))))))))))))))))))))))))))))))))")

'''
BUG INFO : codec error we get :((((((((((   but finish main part
'''