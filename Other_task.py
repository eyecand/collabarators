import re
import hashlib

filenam = "mir.txt_hash_a914ca73703aaf4906e11d8117bbb90f"
filename1 = "4.txt"


myfile = open(filenam)
myfile1 = open(filename1,mode='w')
mas = []
new_mas = []                #создаю новый массив чтобы записать hash
i = 0                       #счетчик
#---------------------------------№4-----------------------------------
line = myfile.read()
looktext = r"(?!6000)(?!8209)[0-9]{4}\D{20}"
resultlooktext = re.findall(looktext,line)
for line in resultlooktext:
   # print(line)
    myfile1.write(line+ "\n")

myfile.close()
myfile1.close()
#-----------------------------------------------------------------------

#---------------------------------№1-----------------------------------
myfile = open(filenam)
text = (myfile.read()).split("судьба")
for x in text:                                #записываю в массив текст после разделения
    x = x.strip()
    mas.append(x)


print(mas)
print("Total:")
print (len(mas))            # проверка длины массива

#-----------------------------------------------------------------------

#---------------------------------№2-3-----------------------------------

wordintext = r"[А-Яа-яA-Za-z0-9]+"


for i in range(1,len(mas)):                            #записываем текст из задания №1 в каждый файл
    filename ='text{}.txt'.format(i)
    y = open(filename, "w")
    y.write(mas[i])



                                                            #расчет количества слов и запись в массив
mas_word = []
for i in range(i,len(mas)):
    filename = 'text{}.txt'.format(i)
    y = open(filename, 'w+')
    line1 = y.read()
    res = re.findall(wordintext, line1)
    mas_word.append(i)

#for i in range(1,len(mas)):                             #запись количества слов в каждый файл + считаем хеш каждого файла
 #   filename = 'text{}.txt'.format(i)
  #  y = open(filename, 'a')
 #   y.write(str(mas_word))

for i in range(1,len(mas)):
    fname = 'text{}.txt'.format(i)
    z = open(fname, 'rb')
    heh = hashlib.md5(z.read()).hexdigest()
    new_mas.append(heh)

print(new_mas)

for i in range(1, len(mas)+1):                                  #меняю название файла
    filename = 'text{0}.txt_hash_{1}'.format(i,new_mas[i])
    y = open(filename, "w")
    y.write(mas[i])

myfile.close()
