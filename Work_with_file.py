import re
import os

filename = "mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f"
filename1 = "4.txt"
filename2 = "text1.txt"

myfile2 = open(filename2)
myfile = open(filename)
myfile1 = open(filename1,mode='w')

line = myfile.read()
looktext = r"(?!6000)(?!8209)[0-9]{4}\D{20}"
resultlooktext = re.findall(looktext,line)
print(os.getcwd())
with open("text1.txt") as file:
    line1 = file.read()
    wordintext = r"[А-Яа-яA-Za-z0-9]+"
    res = re.findall(wordintext,line1)
    print(len(res))
with open("text{}.txt".format(1),'a') as fil:
    fil.write("\n" + str(len(res)))
   # os.rename("text1.txt","text110.txt")



old_file = os.path.join(r"C:\Users\ЕГОР\PycharmProjects\new1\venv", "text1.txt")
new_file = os.path.join(r"C:\Users\ЕГОР\PycharmProjects\new1\venv", "text22.txt")
os.rename(old_file, new_file)
"""

for line in resultlooktext:
    print(line)
    myfile1.write(line+ "\n")


"""
myfile.close()
