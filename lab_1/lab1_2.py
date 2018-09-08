def easy(n):
    if n == 1 or n == 2:
        return True
    if n > 0:
        for i in range(2, n//2+1):
            if n % i == 0:
                return False
                break
        return True
#Находим простое число
                
l = input().split(',')
n, c, v, k, ch, nch, p = [], [], [], [], [], [], []
#в контексте данной задачи рациональные и вещественные числа не имеют разницы
#Добавил проверку, является ли символ числом
#Также я считал, что все целые числа относятся к вещественным
#n -натуральные, с - целые, r - рациональные, v - вещественные
#k - комплексные, ch - четные, nch - нечетные, p - простые
f = True
f1 = True
for i in l:
    try:
        complex(i)
    except:
        f = False
    if f != False:
        a = complex(i)
        if a.imag != 0:
            k.append(a)
        if a.real.is_integer():
            a = int(a.real)
            v.append(a)
            c.append(a)
            if a > 0:
                n.append(a)
            if f1 == easy(a):
                p.append(a)
            if a % 2 == 0:
                ch.append(a)
            else:
                nch.append(a)
        else:
            v.append(a.real)

print("Натуральные: ", ' '.join(str(i) for i in n))
print("целые:       ", ' '.join(str(i) for i in c))
print("вещественные:", ' '.join(str(i) for i in v))
print("комплексные: ", ' '.join(str(i) for i in k))
print("четные:      ", ' '.join(str(i) for i in ch))
print("нечётные:    ", ' '.join(str(i) for i in nch))
print("простые:     ", ' '.join(str(i) for i in p))
        
        
