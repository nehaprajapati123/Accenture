def doreverse():
    string = input("Enter Your String ")
    string =string.split()
    list1 = []
    i = 1
    while i<=len(string):
        print(string[-i],end = ' ')
        i+=1
        
doreverse()