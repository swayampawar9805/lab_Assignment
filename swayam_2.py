list_marks = []

def students_marks():
    a = int(input("Enter marks:"))
    list_marks.append(a)
    
def average():
    sum = 0
    for i in list_marks:
        sum = sum + i
    avg = sum/len(list_marks)
    print("Average:",avg)

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
    mx = 0
    for i in list_marks:
        if i >= m:
           mx = i
        m = i
    print("max:",mx)

def mi():
    mi = list_marks[0]
    for i in list_marks:
        if i <= mi:
           print("min:",mi)

e = True
s = int(input("Enter total number of student:"))  
while e:
     students_marks()
     w = str(input("want to continue(y/n):"))
     if w == "n":
        e = False
print("list of marks:",list_marks)
average()
print("Number of absent student:",s-len(list_marks))
highest_frequency()
mx()
mi()
