import os
import re, sys, msvcrt

cls = lambda: os.system('cls')
cls()

def walk(dir):

  for name in os.listdir(dir):
    path = os.path.join(dir, name)
    number_file = len(os.listdir(dir))
    Key = msvcrt.getch()
    if Key == b'q':
        sys.exit()
    if os.path.isfile(path):
            #array.append(path)
            number = len(os.listdir(os.path.split(dir)[0]))
            print(re.sub(r"(\\)", '  \\1', path) + "\ " + str(number_file) + " \ " + str(number)+ ' \ '  + str(abs(int(number_file)- int(number)))+"\n")

    else:
            walk(path)
print("Enter the path: ")
path = input()
print("Press to continue any Key or exit is 'q' ")

walk(path)


