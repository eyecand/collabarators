import hashlib
import re
filename = "text1.txt"


#myfile = open(filename, 'r')
#x= hashlib.md5(myfile.read()).hexdigest()
#print(x)

#name = 'egor'
#age = 20
#print('Мое имя {0}\n Мой возраст {1}'.format(name, age))
mas = []
with open('mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f','r') as f:
    text = (f.read()).split('судьба')
    for line in text:
        line = line.strip()
        mas.append(line)

print(mas)
print("Total array: " + str(len(mas)))
""""

with open('4.txt', 'w') as myfile1:
    with open('mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f','r') as file:
        line = file.read()
        looktext = r"(?!6000)(?!8209)[0-9]{4}\D{20}"
        resultlooktext = re.findall(looktext,line)
        for line in resultlooktext:
   # print(line)
            myfile1.write(line+ "\n")
"""

