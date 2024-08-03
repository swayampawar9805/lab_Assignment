list_criket = []
list_badminton = []
list_football = []
list_both_criket_badminton = []
list_either_criket_badminton = []
list_neither_criket_badminton = []
list_both_criket_football = []

def criket_student():
    c = str(input("Enter name:"))
    if c not in list_criket:  
       list_criket.append(c)
    
def badminton_student():
    b = str(input("Enter name:"))
    if b not in list_badminton:
       list_badminton.append(b)
    
def football_student():
    f = str(input("Enter name:"))
    if f not in list_football:
       list_football.append(f)

def both_criket_badminton():
    for i in list_criket:
        for j in list_badminton:
            if i==j:
               list_both_criket_badminton.append(i)
               
def either_criket_badminton():
    list_merged1 = list_criket + list_badminton
    for u in list_merged1:
        if u not in list_both_criket_badminton:
           list_either_criket_badminton.append(u)
        
def neither_criket_badminton():
    list_merged1 = list_criket + list_badminton
    list_merged2 = list_criket + list_badminton + list_football
    for a in list_merged2:
        if a not in list_merged1:
           list_neither_criket_badminton.append(a)
           
def both_criket_football():
    list_merged3 = list_football + list_criket
    for x in list_merged3:
        if x not in list_badminton:
            list_both_criket_football.append(x)
    
print("---------1 - to print both criket and badminton student list")
print("---------2 - to print either criket or badminton student list")
print("---------3 - to print neither criket or badminton student list")
print("---------4 - to print no badminton student list")
print("---------5 - to print all list")

e = True
while e:     
     print("CRIKET STUDENT")    
     d = int(input("Enter number of students:"))
     for i in range(0,d):
         criket_student()
     print(list_criket)
     print("BADMINTON STUDENT")
     d = int(input("Enter number of students:"))
     for i in range(0,d):
         badminton_student()
     print(list_badminton)
     print("FOOTBALL STUDENT")
     d = int(input("Enter number of students:"))
     for i in range(0,d):
         football_student()
     print(list_football)
     choice=int(input("Enter your choice:"))
     if choice ==1:
        both_criket_badminton()
        print("list both criket and badminton:",list_both_criket_badminton)
     if choice ==2:
        either_criket_badminton()
        print("list either criket or badminton:",list_either_criket_badminton)
     if choice ==3:
        neither_criket_badminton()
        print("list neither criket nor badminton:",list_neither_criket_badminton)
        print("number of student who  neither play criket nor badminton:",len(list_neither_criket_badminton))
     if choice==4:   
        both_criket_football()
        print("no badminton student:",list_both_criket_football)
        print("number of student who do not play badminton:",len(list_both_criket_football)) 
     if choice==5:
        both_criket_badminton()
        print("both criket and badminton:",list_both_criket_badminton)
        either_criket_badminton()
        print("either criket or badminton:",list_either_criket_badminton)
        neither_criket_badminton()
        print("neither criket nor badminton:",list_neither_criket_badminton)
        print("number of student who  neither play criket nor badminton:",len(list_neither_criket_badminton))
        both_criket_football()
        print("no badminton student:",list_both_criket_football)
        print("number of student who do not play badminton:",len(list_both_criket_football))
     d = str(input("want to continue(y/n):"))
     q="n"
     if q==d:
        e = False    
     
