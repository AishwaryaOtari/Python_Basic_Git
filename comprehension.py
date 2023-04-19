

from collections import Counter
l1=[1,2,8,4,5,7,4,6,3,2,5,4,8,5,2,5,1,5,6,8]
c=Counter(l1)
d=c.most_common()
print(d)
l2=[i for i in d]
l3=[i[0]+i[1] for i in d]
print(l3)
print(l2)
import sys
sys.exit(0)
l1=[1,2,8,4,5,7,4,6,3,2,5,4,8,5,2,5,1]
for i in l1:
    n=l1.count(i)
    if n<=1:
        print(i)

import sys
sys.exit(0)
from collections import ChainMap
d1={1:10,2:20,3:30}
d2={4:40,5:50,6:60}
d3={7:70,8:80,9:90}

chain=ChainMap(d1,d2,d3)
print(chain)
print(list(chain.keys()))
print(list(chain.values()))
print(chain.maps)
import sys
sys.exit(0)
from collections import Counter
str1="aishwarya"
c=Counter(str1)
print(c)



import sys
sys.exit(0)
#print("Enter number to check palindrom")
strr=int(input("Enter number to check palindrom"))
if strr<0:
    strr=strr*(-1)
str1=str(strr)
if str1==str1[::-1]:
    print("String is palindrom")
else:
    print("String is not palindrom")