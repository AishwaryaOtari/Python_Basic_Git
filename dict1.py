import sys
s='AishwaryaAishotariOtari'
d={}
for i in s:
    if i in d.keys():
        d[i]=d.get(i,0)+1
    else:
        d[i]=1
print(d)
sys.exit()






import sys
d={1:100,2:200,3:300,1:1000,4:400,5:500,3:4000,True:123}
print(d.keys())
sum1=0
mul1=1
for i in d.keys():
    sum1=sum1+i
    mul1=mul1*i

print('Addition of all keys from given dic=',sum1)
print('Multiplication of all keys from given dict=',mul1)
sys.exit(0)




import sys
d={1:1,'otari':2,'aish':3,4:4,5:5}
print(d)
print(d.values())
v1=0
v2=1
for i in d.values():
    v1=v1+i
    v2=v2*i

print('Addition of all values of given dict=',v1)

print('Multiplication of all values from given dict=',v2)
sys.exit(0)






import sys
d={1:100,2:200,3:300,1:1000,4:400,5:500,3:4000,True:123}
print(d.keys())
k=sum(d.keys())
print('Addition of all keys of dict is=',k)
print(d.values())
v=sum(d.values())
print('Addition of all value from given dic=',v)


sys.exit(0)
import sys
d={1:100,2:200,3:300,1:1000,4:400,5:500,3:4000,True:123}
d.popitem()
print(d)

sys.exit(0)

import sys
d={1:100,2:200,3:300,1:1000,4:400,5:500,3:4000,True:123}
print(d)
print(d.get(3))
print(d.keys())
print(d.values())
print(d.items())


sys.exit(0)

import sys
d={1:100,2:200,3:300,1:1000,4:400,5:500,3:4000,True:123}
print(d)
d.clear()
print(d)
sys.exit(0)


d={1:100,2:200,3:300,1:1000,4:400,5:500,3:4000,True:123}
print(d)
print("Lenght of given dic=", len(d))