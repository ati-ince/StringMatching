import os
import codecs, filecmp

encoding_international= 'utf-8' ; encoding_local='cp1254' #or windows cp1254

def file_diff_modif(file1, file2): # file1 -> 1. (yeni degişiklik), file2 -> 0 (güncel dosya) # only add some utf-8 text to bottm side
    f1 = codecs.open(file1, encoding=encoding_international)  # or windows cp1254
    f2 = codecs.open(file2, encoding=encoding_international)  # or windows cp1254
    #yani len(file1) > len(file2)
    len1=0;len2=0;len_dif=[]
    for line1 in f1:
        for line2 in f2:
            if line1!=line2:  #then add
                f2.write("%r\n" %line1) # add to f2 from f1.....
            len2+=1
        len1+=1
    f1.close();f2.close()
    len_dif.append(len1);len_dif.append(len2)
    return len_dif

def file_write_test(file, _string):
    f = codecs.open(file, encoding=encoding_international)  # or windows cp1254
    f = codecs.open(file, 'a', 'utf-8') # open for writing.... -> 'a' append ile ekliyoruz...
    f.write("%r" % _string)  # add to f2 from f1.....
    f.close()
    return True

def textlinenum(filename):
    f=codecs.open(filename, encoding=encoding_international)
    linelen=0
    for line in f:
        linelen+=1
    f.close()
    return linelen

# tree_printer('.')  # like start point
def tree_printer(root):
    all_list=[]
    for root, dirs, files in os.walk(root):
        for d in dirs:
            dir_buf=os.path.join(root, d)
            #print (dir_buf)
            all_list.append(dir_buf)
        for f in files:
            file_buf=os.path.join(root, f)
            #print (file_buf)
            all_list.append(file_buf)
    return all_list

def all_file_tree(address):
    for root, dirs, files in os.walk(address):
        for filename in files:
            print(filename)

def tree_printer_other1(root):
    all_list=[]
    for root, dirs, files in os.walk(root):
        for d in dirs:
            dir_buf=os.path.join(root, d)
            #print (dir_buf)
            all_list.append(dir_buf)
        for f in files:
            file_buf=os.path.join(root, f)
            #print (file_buf)
            all_list.append(file_buf)
    return all_list