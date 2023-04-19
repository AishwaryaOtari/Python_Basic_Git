import sys
n=int(input('Enter the number of students='))
d={}
for i in range(n):
    name=input('Enter name of student=')
    marks=int(input('Enter marks of student='))
    d[name]=marks
while True:
    name=input('Enter name of student u want to display')
    marks=d.get(name,-1)
    if marks==-1:
        print('Entered student is not present in our data')
    else:
        print('Student namr=',name,'Student marks=',marks)

    option=input('U want to continue(Y,N)')
    if option=='n':
         break
    if option=='y':
         continue
sys.exit(0)




import sys
print("Enter number start from")
start=int(input())
print("Enter number to end")
end=int(input())
while start<end:
    print(start)
    start=start+2
sys.exit(0)

import sys
print("All the even numbers from 50 to 100")
for i in range(50,61,2):
    print(i)
sys.exit(0)
l4N9kH
nl4qg6



l1=[]
l2=[]
print('Enter no to print values')
val=int(input())
for i in range(val):
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)

print('List of even number is=',l1)
print('List of odd number is=',l2)
