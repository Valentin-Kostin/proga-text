from tkinter import *
from tkinter import filedialog

def clicked():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    return file 

def clickedSum():
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

    res = numA+numB 
    print('Длина рабочей подачи: ', numA)
    print('Длина подачи врезания: ', numB)
    print('Длина быстрых перемещений: ', numC)
    print('итого: ', res)
    lbl = Label(window, text=res)
    lbl.grid(column=2, row=2)
    lbl = Label(window, text='Длина рабочей подачи: '+numA)
    lbl.grid(column=2, row=2)
    lbl = Label(window, text=res)
    lbl.grid(column=2, row=2)
    lbl = Label(window, text=res)
    lbl.grid(column=2, row=2)
    return res

window = Tk()
window.title("Добро пожаловать!")
window.geometry('350x200')
lbl = Label(window, text="Привет!")
lbl.grid(column=0, row=0)
# txt = Entry(window,width=10)
# txt.grid(column=1, row=0)
# btn = Button(window, text="Загрузить файл", command=clicked)
# btn.grid(column=1, row=0)

trek = clicked()
file = open(trek, 'r', encoding='utf-16')
resultData = list()

btn = Button(window, text="посчитать", command=clickedSum)
btn.grid(column=2, row=0)



window.mainloop()



# file = clicked() 
# file = file('1.txt', 'r', encoding='utf-16')   


#https://habr.com/ru/company/vdsina/blog/557316/
#https://dvsemenov.ru/tkinter-primery-i-rukovodstvo-kak-delat-gui-na-python/#i-4