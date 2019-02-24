import os

cls = lambda: os.system('cls')
cls()

def walk(dir):
  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    number_file = len(os.listdir(dir))
    if os.path.isfile(path):
        number = len(os.listdir(os.path.split(dir)[0]))
        print(path + "/"  + str(number_file) + "/" + str(number)+ '/'  + str(abs(int(number_file)- int(number)))+"\n")
    else:
        walk(path)

path =r"C:\Users\ЕГОР\PycharmProjects\new1"


walk(path)


