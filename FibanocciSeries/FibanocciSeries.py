#code to print fibanocci eries upto certain no of times 

k = int(input("enter the Number of elements required "))
a = 0
b = 1
print(a)
print(b)
sum = a
for i in range(1,k-1) :   #setting range to number entered
  sum = a + b 
  a = b                #swapping to next to numbers in sequqnce
  b = sum
  print(sum)
  
  
