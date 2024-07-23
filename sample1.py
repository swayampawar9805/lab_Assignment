list_criket = []
list_badminton = []
list_football = []
list_Candk = []
list_CorK = []
list_CandF = []
list_not_criket_badminton =[]

def criket_student():
    a = str(input("Enter name:"))
    list_criket.append(a)
    
def badminton_student():
    b = str(input("enter name:"))
    list_badminton.append(b)
    
def football_student():
    c = str(input("enter name:"))
    list_football.append(c)

def both_criket_and_badminton():
    for i in list_criket:
        for j in list_badminton:
            if i == j:
                list_Candk.append(i)

def either_criket_or_badminton():
    merged_list = list_criket + list_badminton
    for w in merged_list:
        if w not in list_Candk:
            list_CorK.append(w)

def both_criket_and_football():
    merged_list_2 = list_criket + list_football
    for r in merged_list_2:
        if r not in list_badminton:
            list_CandF.append(r)

def neither_criket_nor_badminton():
    merged_list_3 = list_criket + list_badminton
    for s in list_football:
        if s not in merged_list_3:
            list_not_criket_badminton.append(s)

while True:
    print("1 - To enter criket student")
    print("2 - To enter badminton student")
    print("3 - To enter football student")
    print("4 - To print all lists")
    num = int(input("enter choice:"))
    if num ==1:
        criket_student()

    elif num ==2:
        badminton_student()

    elif num ==3:
        football_student()

    elif num == 4:
        both_criket_and_badminton()
        either_criket_or_badminton()
        both_criket_and_football()
        print("list of criket student",list_criket)
        print("list of badminton student",list_badminton)
        print("list of football student",list_football)
        print("list of students who plays both criket and badminton",list_Candk)
        print("number of students who plays both criket and badminton",len(list_Candk))
        print("list of students who plays either criket or badminton",list_CorK)
        print("number of students who plays either criket or badminton",len(list_CorK))
        print("list of students who plays both criket and football but not badminton",list_CandF)
        print("number of students who plays both criket and football but not badminton ",len(list_CandF))
        print("list of students who plays neither criket nor badminton",list_not_criket_badminton)
        print("number of students who plays neither criket nor badminton",len(list_not_criket_badminton))
