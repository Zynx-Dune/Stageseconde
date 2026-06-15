import math
a = int(input("côté 1 :"))
b = int(input("côté 2 :"))
c = int(input("côté 3 :"))
d = int((a + b + c)/2)
S = math.sqrt((d*(d-a)*(d-b)*(d-c)))
print(str(S))