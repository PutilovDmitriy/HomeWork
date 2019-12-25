import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
e = float(input("e = "))
f = float(input("f = "))

p1 = float((a + b + c)/2)
print(p1)
p2 = float((a + d + e)/2)
print(p2)
p3 = float((d + b + f)/2)
print(p3)
p4 = float((c + e + f)/2)
print(p4)

s1 = float(math.sqrt(p1*(p1-a)*(p1-b)*(p1-c)))
print(s1)
s2 = float(math.sqrt(p2*(p2-a)*(p2-d)*(p2-e)))
print(s2)
s3 = float(math.sqrt(p3*(p3-d)*(p3-b)*(p3-f)))
print(s3)
s4 = float(math.sqrt(p4*(p4-c)*(p4-e)*(p4-f)))
print(s4)

if s1 == s2:
    reply = True
elif s1 == s3:
    reply = True
elif s1 == s4:
    reply = True
elif s2 == s3:
    reply = True
elif s2 == s4:
    reply = True
elif s3 == s4:
    reply = True
else:
    reply = False

print(reply)