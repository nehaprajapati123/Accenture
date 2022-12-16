list1 = [[1,2,3],[4,5,6],[8,99]]
def mylist():
    sum = 0
    for i in list1:
        
        for j in i:
            sum = sum + j
        
    print("maximum: ",max(i))
    print("sum: ",sum)
mylist()