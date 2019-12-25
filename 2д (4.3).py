import math

e = float(input("ε = "))
l = [0.5]
i = 1
while i <= len(l):
    a = math.cos(l[i-1])
    l.append(a)
    if math.fabs(l[i] - l[i-1]) < e:
        print("Наименьший номер для которого выполяняется условие = " + str(i+1))
        print(l)
        break
    i += 1