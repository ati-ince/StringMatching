
import os
import codecs

'''
SelectedEncoding= 'utf-8' # cp437 for english, which created first...  Can be change after which is fitted.. .
SelectOtherEncoding = 'cp855' # cp855 for SERbIAN for test
#sample read a file... with true codec...
#### NOTE: One project folder have to 2 file and other has to 1 file. And 1 file should be referance for string matching and creating...
f_other = codecs.open("Str-SERB_O2.rc", encoding=SelectedEncoding) #select for other lang format for example serbian
#f_new = open("Str-SERB_New_O2.rc","w") #opens file with name of "***.txt"

for line in f_other:
    print(line)
    #f_new.write(line)

#f_new.close()
'''

SelectedEncoding= 'utf-8' # cp437 for english, which created first...  Can be change after which is fitted.. .
SelectOtherEncoding = 'utf-8' # cp855 for SERbIAN for test
fileformat='.rc' #you can change

#sample read a file... with true codec...
#### NOTE: One project folder have to 2 file and other has to 1 file. And 1 file should be referance for string matching and creating...

ProjFolderName=['G7', 'O4']
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
k=0
for line in f:
    bufStr=str(line).split(';')
    RefFileStringCode.append(bufStr[0]) #name of string kind of , it is referance string name list and order...
    # then comin ,"somethings......" with bufStr[1]
    # lets delete ," and latest one so
    bufStr2=bufStr[1][2:-1] #correct method
    if len(bufStr2)!=0:
        RefFileStringInfo.append(bufStr2)
    else:
        RefFileStringInfo.append("Dummy Text for Test, elements: "+"["+str(k)+"]")
        print("----------------  ERROR ----------------" + "-> number: " + str(k))
    k+=1
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

#############################################################################################


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

print("ref  ", RefFile)

print("lan file  ", LangFile )
'''
New file should be Ref file directory + Lang file file name
'''
buf1=RefFile.split("\\")[:-1]
link = ""
for k in range(len(buf1)):
    link+=buf1[k]+"\\"
_directory=link[:-1] #delete lates "\"
#get file name from Lang file
buf2=LangFile.split("\\")[-1]
newfilename=_directory+"\\"+buf2
#lets test is it correct?
print("new file last", newfilename)
f_last = codecs.open(newfilename, 'w', 'utf-8')  # open for writing.... -> 'a' append ile ekliyoruz...

for xx in range(len(RefFileStringInfo)):
    if RefFileStringCode[xx]==FileStringCode[xx]:
        data=FileStringCode[xx] + ";," + '"'+FileStringInfo[xx] +'"'
        print(data)
        '''
        Bu kısımda tüm dosyayı yazdırabiliriz.
        '''

        f_last.write(data+"\n")  # add to f2 from f1.....
    else:
        print(" *** FALSE *** || " + RefFileStringInfo[xx] + " || " + FileStringInfo[xx])

f_last.close()


