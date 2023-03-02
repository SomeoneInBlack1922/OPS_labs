import Лаба3_tasks as t
def start(n):
    #Реалізує виконання завдання. Я зробив це окремою функцією щоб вліпити "---The task has begun" не копіюючи прінти у всі кейси
    print("--The task has begun--")
    match n:
        case 1:
            t.task1()
        case 2:
            t.task2()
        case 3:
            t.task3()
        case 4:
            t.task4()
        case 5:
            t.task5()
        case 6:
            t.task6()
        case 7:
            t.task7()

print("--Enter the number of tusk to run--","--Enter '0' to stop the program--",sep="\n")
while True:
    print(">> ",end="")
    n=int(input())
    if(n==0):
        break
    else:
        start(n)
    print("--Done--","--Enter number of the next task or '0' to stop the program--",sep="\n")
print("--The program has stopped--")