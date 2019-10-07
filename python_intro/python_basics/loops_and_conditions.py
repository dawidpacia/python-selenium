a = 0

while True:
    a += 1  # a = a + 1, *=, /=. -=
    print(a)
    if a is 10:
        break

b_list = [0, 1]

for element in b_list:
    print(element)

for element in range(1, 10, 2):  # print from 1 to 9, every 2nd element
    print(element)

a = 1
b = 0

if a > b:
    print("{} larger than {}".format(a, b))  # printing with variables
elif b == a:
    print("{} equal to {}".format(a, b))
else:
    print("{} smaller than {}".format(a, b))

a_list = [1, 2, 3]

for element in a_list:
    if element == 1:
        print("TRUE")
        break

if 1 in a_list:  # equivalent to for above
    print("TRUE")
