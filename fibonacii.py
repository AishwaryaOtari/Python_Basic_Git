n=int(input('Enter the number of terms'))
first,second=0,1
count=0
if n<=0:
    print('Enter valid number')
elif n==1:
    print(first)

else:
    while count<n:
        print(first)
        nth=first+second
        sys
import sys
sys.exit(0)
def fbo():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fbo()
for i in f:
    if i>5:
        break
    print(i)
import sys
sys.exit(0)
def fbo():
    a,b=0,1
    for i in range(5):
        yield a
        a,b=b,a+b

for i in fbo():
    print(i)
