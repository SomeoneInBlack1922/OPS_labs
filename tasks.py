import Лаба_3_working_functions as f

def task1():
    #Я зрозумів другу позицію у натуральному розумінні а не у індексному
    a=[1,6,-8,12,7]
    print(a)
    a.insert(1,-5)
    print(a)
    per=f.lper(a)
    print("Найменьше значення:",per["min"],"Найбільше значення",per["max"],sep='\n')
    #Я зрозумів що цей новий список має бути третім
    a.insert(2,[1,2,3])
    print("Додав список [1,2,3] на третю позицію:",a,sep='\n')
    print("Визначив довжину списку:",len(a),sep='\n')
def task2():
    #Я зробив 4 товари, бо мій код не залежить від їх кількості
    lc=["Хліб","Молоко","Сік","Масло"]
    la=[54,35,21,32]
    lb=[27,30,15,25]
    print("Товари:",f.lsimp(lc))
    print("Їх кількість:",f.lsimp(la))
    print("Їх ціна:",f.lsimp(lb))
    #Визначаю загальну вартість товарів на складі
    fullvalue=0
    for i in range (4):
        fullvalue+=la[i]*lb[i]
    print("Загальна вартість всіх товарів дорівнює",fullvalue,sep=' ')
    #Визначаю середню ціну
    averegevalue=fullvalue/sum(la)
    print("Середня ціна товарів дорівнює",round(averegevalue,2),sep=' ')
def task3():
    #Я зрозумів завдання як згенерувати випадкові числа
    A1=list()
    A2=list()
    rand=0
    for i in range(25):
        import random
        rand=random.randint(-50, 50)
        if rand>=0:
            A1.append(rand)
        else:
            A2.append(rand)
    print("I generated 25 random numbers from -50 to 50","There are possitive:",f.lsimp(A1),sep="\n")
    print("And there are negattive:",f.lsimp(A2),sep="\n")
def task4():
    a='Мене звуть Миколай Дацко. Я навчаюся у Державному університеті телекомунікацій на спеціальності інжинерія програмного забезпечення. Наша група називається ТЦР, тобто "технології цифрового розвитку". У нас дружній та злагоджени й колектив. Я дійсно люблю писати програми та отримувати нові знання. Щодня прокидаючись з радість підключаюся на пари. У вільний час я люблю грати у ігри та слухати музику. Також я люблю їсти, а хто не любить? І спати, ну звісно ж. Сподіваюся на плідну подальшу співпрацю.'
    a1=a.split('.')
    for i in range(len(a1)-1):
        if a1[i][0] == ' ':
            a1[i] = a1[i][1:]
        if a1[i] == '':
            del a1[i]
            i+=1
            continue   
        a1[i]+='.'
        print(a1[i])
def task5():
    a="Миколай Дацко, ТЦР - 11, інжинерія програмного забезпечення"
    print(a[:13])
    print(a[15:23])
    print(a[25:])
    a=a.replace(',','')
    print(a.split(' '))
def task6():
    a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    #Я описав функцію outcut яка приймає список та індекси елементів що мають бути вирізані
    print(f.outcut(a,0,4,5))
def task7():
    print("Введіть рядок, а я верну його у нижньому регістрі. Для закінчення программи пропустіть введення рядка")
    a=str()
    while (True):
        a=input("Введіть рядок: ")
        a=a.lower()
        if a=='':
            break
        print("Ваш рядок: ",a,sep='')