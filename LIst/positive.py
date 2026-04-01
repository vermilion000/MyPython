# code to print only positive  numbers in a list
k = input("Enter the number of elements in list : ")    #to store no of elements in list

a = list(map(int,input("Enter the elements(with space) : ").split())) #map used to iterate(),input(),int(),split(),list() are used to thier usual usage

for i in range(0,len(a)) :
    if (a[i] > 0) :
        print(a[i])
