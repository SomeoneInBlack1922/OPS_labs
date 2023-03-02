def lper(a=list):
    #Вертає нійбільше та найменьше значення словником
    mi=a[0]
    ma=a[0]
    for i in range(len(a)-1):
        if a[i+1]>ma:
            ma=a[i+1]
        elif a[i+1]<mi:
            mi=a[i+1]
    return{"min":mi,"max":ma}
def dav(a=dict):
    #Рахує середнє арифметичне значень словника. Я використовую це один раз тому можна було і у коді написати
    a=a.values()
    r=None
    for i in range(len(a)):
        r+=a[i]
    return r/len(a)
def lsimp(a=list):
    #Вертає список нормальним рядком без квадратних дужок та лапок
    a=str(a)
    a=a.replace("[","")
    a=a.replace("]","")
    a=a.replace("'","")
    return a
def outcut(a=list(), *b):
    b=sorted(b)
    n=0
    for i in range(len(b)):
        del a[b[i]-n]
        n+=1
    return a
