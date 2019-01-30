import re

filename = "mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f"
filename1 = "4.txt"
filename2 = "text1.txt"

myfile2 = open(filename2)
myfile = open(filename)
myfile1 = open(filename1,mode='w')

line = myfile.read()
looktext = r"(?!6000)(?!8209)[0-9]{4}\D{20}"
resultlooktext = re.findall(looktext,line)

line1 = myfile2.read()
wordintext = r"[А-Яа-яA-Za-z0-9]+"
res = re.findall(wordintext,line1)
print(len(res))



for line in resultlooktext:
    print(line)
    myfile1.write(line+ "\n")



myfile.close()
myfile1.close()