from tkinter import *
from tkinter import filedialog

# def clicked():
#     file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
#     return file
# window = Tk()
# window.title("Добро пожаловать!")
# window.geometry('350x200')

# btn = Button(window, text="Загрузить файл", command=clicked)
# btn.grid(column=1, row=0)
# window.mainloop()
file = open('1.txt', 'r', encoding='utf-16')
list_1 = list()
resultData = list()
for line in file.readlines():
    resultData.append(list(line.split('\n')))  # [0].split(':')
file.close()
numA = 0
numB = 0
numC = 0
j = 39
for i in resultData:
    stringA = str(resultData[j])
    stringA = stringA[23:-11]
    numA += int(stringA)

    stringB = str(resultData[j+1])
    stringB = stringB[24:-8]
    numB += int(stringB)

    stringC = str(resultData[j+2])
    stringC = stringC[28:-9]
    numC += int(stringC)

    j += 25
    if j > len(resultData):
        break

print('Длина рабочей подачи: ', numA)
print('Длина подачи врезания: ', numB)
print('Длина быстрых перемещений: ', numC)
print('итого: ', numA+numB)
#https://habr.com/ru/company/vdsina/blog/557316/
#https://dvsemenov.ru/tkinter-primery-i-rukovodstvo-kak-delat-gui-na-python/#i-4