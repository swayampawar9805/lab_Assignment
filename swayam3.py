list_criket = []
list_badminton = []
list_football = []
list_both_criket_badminton = []
list_either_criket_badminton = []
list_neither_criket_badminton = []
list_no_badminton = []

def student_names():
    print("CRIKET STUDENTS")
    a =int(input("Enter number of students:"))
    for i in range(0,a):
        s =str(input("Enter criket student name:"))
        if s not in list_criket:
            list_criket.append(s)
    print("criket list:",list_criket)
    print("BADMINTON STUDENTS")
    b =int(input("Enter number of students:"))
    for i in range(0,b):
        s =str(input("Enter badminton student name:"))
        if s not in list_badminton:
            list_badminton.append(s)
    print("badminton list:",list_badminton)
    print("FOOTBALL STUDENTS")
    c =int(input("Enter number of students:"))
    for i in range(0,c):
        s =str(input("Enter football student name:"))
        if s not in list_football:
            list_football.append(s)
    print("football list:",list_football)

def both_criket_and_badminton():
    for i in list_criket:
        for j in list_badminton:
            if i == j:
                list_both_criket_badminton.append(i)

def either_criket_or_badminton():
    merged_list = list_criket + list_badminton
    for w in merged_list:
        if w not in list_both_criket_badminton:
            list_either_criket_badminton.append(w)

def neither_criket_nor_badminton():
    merged_list_3 = list_criket + list_badminton
    for s in list_football:
        if s not in merged_list_3:
            list_neither_criket_badminton.append(s)

def no_badminton():
    merged_list_2 = list_criket + list_football
    for r in merged_list_2:
        if r not in list_badminton:
            list_no_badminton.append(r)

e = True
while e == True:
    student_names()
    print("1 - list of students who plays both criket and badminton")
    print("2 - list of students who plays either criket or badminton")
    print("3 - list of students who plays neither criket or badminton")
    print("4 - list of students who do not play badminton")
    f = int(input("Enter your choice:"))
    if f == 1:
        both_criket_and_badminton()
        print("list of students who plays both criket and badminton:",list_both_criket_badminton)
    elif f==2:
        either_criket_or_badminton()
        print("list of students who plays either criket or badminton:",list_either_criket_badminton)
    elif f==3:
        neither_criket_nor_badminton()
        print("list of students who plays neither criket or badminton:",list_neither_criket_badminton)
    elif f==4:
        no_badminton()
        print("list of students who do not play badminton:",list_no_badminton)
    g = str(input("want to continue(y/n):"))
    if g == "y":
        e = True
    elif g=="n":
        e = False

