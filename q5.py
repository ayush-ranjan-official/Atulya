l = eval(input("Enter the list :"))
a = 0

for i in range(99):
    for j in range(i + 1, 100):
        if l[i]==l[j]:
            a=l[i]
            # As it is given that only 1 number repeats itself
            break
print(a)
