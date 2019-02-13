import os

# cwd = os.getcwd() #возвращает текущий каталог:
# #print (cwd)
#
# os.listdir(cwd)
# #print (os.listdir(cwd)) #Вы вести список файлов и подкаталогов для данного каталога
#
# #

def walk(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    number_file = len(os.listdir(dir)) # подсчет в текущем каталоге
    if os.path.isfile(path):
        number = len(os.listdir(os.path.split(dir)[0])) #подсчет в каталоге на уровень выше
        print(path + "_____" + "dlina:" + str(number_file) + "__________" + "last:" + str(number))
    else:
        walk(path)

path =r"C:\Задание_2\TARGET_PATH"


walk(path)

#
# path, dirs, files = os.walk(".").next()
# file_count = len(files)
#
# for index, part_file in enumerate(os.listdir(path)):

