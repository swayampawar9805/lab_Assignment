list_marks = []

def students_marks():
    a = int(input("Enter marks:"))
    list_marks.append(a)
    
def average():
    sum = 0
    for i in list_marks:
        sum = sum + i
    avg = sum/len(list_marks)
    print("Average marks of class:",avg)

def highest_frequency():
    list_sample = []
    for i in list_marks:
        list_sample.append(i)
    set_sample = set(list_sample)
    for i in set_sample:
        if len(list_sample)>1:
           list_sample.remove(i)
    print("high frequency:",set(list_sample))
    
def mx():
    m = 0
    mxm = 0
    for i in list_marks:
        if i >= m:
           mxm = i
        else:
            continue
        m = i
    return mxm

def mi():
    n = mx()
    mim = 0
    for i in list_marks:
        if i <= n:
            mim = i
        else:
            continue
        n = i
    print("min marks:",mim)  


e = True
s = int(input("Enter total number of student:"))  
while e:
     students_marks()
     w = str(input("want to continue(y/n):"))
     if w == "n":
        e = False
print("list of marks:",list_marks)

print("1 - The average score of class")
print("2 - Highest and lowest score of class")
print("3 - Count of absent student")
print("4 - Marks with higest frequency")
print("5 - TO PRINT ALL")
print("6 - Exit")

fg = True
while fg:
    choice = int(input("Enter your choice:"))
    if choice==1:
        average()
    elif choice==2:
        max_marks = mx()
        print("max marks:",max_marks) 
        mi()
    elif choice==3:
        print("Number of absent student:",s-len(list_marks))
    elif choice==4:
        highest_frequency()
    elif choice==5:
        average()
        max_marks = mx()
        print("max marks:",max_marks) 
        mi()
        print("Number of absent student:",s-len(list_marks))
        highest_frequency() 
    elif choice==6:
        fg = False