file = open('1.txt', 'r', encoding='utf-16')

list_1 = list()
resultData = list()
for line in file.readlines():
    resultData.append(list(line.split('\n')))#[0].split(':')


file.close()
j=39
print(len(resultData))
for i in resultData:
    print(resultData[j].remove('Длина рабочей подачи:'))
    # stringA = str(resultData[j])
    # print(stringA)
    # numA = int(stringA[17:])
    #print(numA)
    print(resultData[j+1])
    print(resultData[j+2])
    j +=25 
    if j>len(resultData): break  
