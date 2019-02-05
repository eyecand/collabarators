import re
import hashlib
import os

filenam = "mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f"
filename1 = "4.txt"


# myfile = open(filenam)
# myfile1 = open(filename1,'w')
mas = []
new_mas = []                #создаю новый массив чтобы записать hash
mas_word = []
i = 0
#---------------------------------№4-----------------------------------
with open('4.txt', 'w') as myfile1:
    with open('mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f','r') as file:
        line = file.read()
        looktext = r"(?!6000)(?!8209)[0-9]{4}\D{20}"
        resultlooktext = re.findall(looktext,line)
        for line in resultlooktext:
   # print(line)
            myfile1.write(line+ "\n")

#-----------------------------------------------------------------------

#---------------------------------№1-----------------------------------
with open('mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f','r') as f:
    text = (f.read()).split('судьба')
    for line in text:
        line = line.strip()
        mas.append(line)

print(mas)
print("Total array: " + str(len(mas)))

#-----------------------------------------------------------------------

#---------------------------------№2-3-----------------------------------
for i in range(0, len(mas)):
    with open('text{}.txt'.format(i), 'w') as f:
               f.write(mas[i])

for i in range(0,len(mas)):
    with open('text{}.txt'.format(i), 'r') as y:
        line1 = y.read()
        wordintext = r"[А-Яа-яA-Za-z0-9]+"
        res = re.findall(wordintext, line1)
        mas_word.append(len(res))
print(mas_word)

for i in range(0,len(mas)):
    with open("text{}.txt".format(i),'a') as fil:
        fil.write("\n" + str(mas_word[i]))


for i in range(0,len(mas)):
    with open('text{}.txt'.format(i),"rb") as z:
        heh = hashlib.md5(z.read()).hexdigest()
        new_mas.append(heh)

print(new_mas)
os.chdir(r"C:\Users\ЕГОР\PycharmProjects\new1\venv")
for i in range(0, len(mas)):
    old_file = os.path.join(r"C:\Users\ЕГОР\PycharmProjects\new1\venv", "text{}.txt".format(i))
    new_file = os.path.join(r"C:\Users\ЕГОР\PycharmProjects\new1\venv", "text.txt_hash_{}".format(new_mas[i]))
    os.rename(old_file, new_file)

