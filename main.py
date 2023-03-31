from tkinter import *
from tkinter import filedialog


def clicked():    
    trek = filedialog.askopenfilename(filetypes=(
        ("Text files", "*.txt"), ("all files", "*.*")))
    file = open(trek, 'r', encoding='utf-16')
    return file


def clickedSum():
    file = clicked()
    resultData = list()
    for line in file.readlines():
        resultData.append(list(line.split('\n')))  # [0].split(':')
    
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

    res = (numA+numB)/1000    
    lbl = Label(window, text='итого: ' + str(res) + ' метров')
    lbl.grid(column=2, row=2)
    lbl2 = Label(window, text='Длина рабочей подачи: ' + str(numA/1000)+ ' метров')
    lbl2.grid(column=2, row=3)
    lbl3 = Label(window, text='Длина подачи врезания: ' + str(numB/1000)+ ' метров')
    lbl3.grid(column=2, row=4)
    lbl4 = Label(window, text='Длина быстрых перемещений: ' + str(numC/1000)+ ' метров')
    lbl4.grid(column=2, row=5)
    file.close()# return res


window = Tk()
window.title("ПОДСЧЕТ ДЛИНЫ РЕЗА")
window.geometry('350x200')
lbl = Label(window, text="Привет!")
lbl.grid(column=2, row=0)
btn = Button(window, text="загрузить файл и посчитать", command=clickedSum)
btn.grid(column=2, row=1)

window.mainloop()


# file = clicked()
# file = file('1.txt', 'r', encoding='utf-16')


# https://habr.com/ru/company/vdsina/blog/557316/
# https://dvsemenov.ru/tkinter-primery-i-rukovodstvo-kak-delat-gui-na-python/#i-4
