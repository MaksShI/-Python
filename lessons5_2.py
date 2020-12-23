# 2.	Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

# 10 = A
# 11 = B
# 12 = C
# 13 = D
# 14 = E
# 15 = F
a = deque()
b = deque()
j = deque()

while True:
    h = input('Вводите числа первого слагаемого ,  "q"  - переход ко торому слагаемому: ')
    if h == 'q':
        break
    else:
        a.append(h)
print(a)
while True:
    h = input('Вводите числа второго слагаемого ,  "q"  - сложение: ')
    if h == 'q':
        break
    else:
        b.append(h)
print(b)

count = 0

i = 0
max_num = 0
if len(a) > len(b):
    max_num = len(a)
else:
    max_num = len(b)
while i != max_num:
    if len(a) == 0 or len(b) == 0:
        s = a[i] + b[i] + count
        if s < 10:
            j.appendleft(s)
        else:
            if s == 10:
                s = 'A'
                j.appendleft(s)
            elif s == 11:
                s = 'B'
                j.appendleft(s)
            elif s == 12:
                s = 'C'
                j.appendleft(s)
            elif s == 13:
                s = 'D'
                j.appendleft(s)
            elif s == 14:
                s = 'E'
                j.appendleft(s)
            elif s == 15:
                s = 'F'
                j.appendleft(s)
            else:
                count = s - 15
                j.appendleft('F')
                if count == 10:
                    count = 'A'
                elif count == 11:
                    count = 'B'
                elif count == 12:
                    count = 'C'
                elif count == 13:
                    count = 'D'
                elif count == 14:
                    count = 'E'
                else:
                    count = 'F'
                break
            break
        break

    if a[i] == 'A':
        a[i] = 10
    elif a[i] == 'B':
        a[i] = 11
    elif a[i] == 'C':
        a[i] = 12
    elif a[i] == 'D':
        a[i] = 13
    elif a[i] == 'E':
        a[i] = 14
    else:
        a[i] = 15
    if b[i] == 'A':
        b[i] = 10
    elif b[i] == 'B':
        b[i] = 11
    elif b[i] == 'C':
        b[i] = 12
    elif b[i] == 'D':
        b[i] = 13
    elif b[i] == 'E':
        b[i] = 14
    else:
        b[i] = 15
    if count == 'A':
        count = 10
    elif count == 'B':
        count = 11
    elif count == 'C':
        count = 12
    elif count == 'D':
        count = 13
    elif count == 'E':
        count = 14
    else:
        count = 15
    s = a[i] + b[i] + count
    if s < 10:
        j.appendleft(s)
    else:
        if s == 10:
            s = 'A'
            j.appendleft(s)
        elif s == 11:
            s = 'B'
            j.appendleft(s)
        elif s == 12:
            s = 'C'
            j.appendleft(s)
        elif s == 13:
            s = 'D'
            j.appendleft(s)
        elif s == 14:
            s = 'E'
            j.appendleft(s)
        elif s == 15:
            s = 'F'
            j.appendleft(s)
        else:
            count = s - 15
            j.appendleft('F')
            if count == 10:
                count = 'A'
            elif count == 11:
                count = 'B'
            elif count == 12:
                count = 'C'
            elif count == 13:
                count = 'D'
            elif count == 14:
                count = 'E'
            else:
                count = 'F'
            i += 1
print(s)
print()
