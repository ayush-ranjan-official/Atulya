s = input("Enter the string without inverted commas:")
a=0
for i in s:
    if i.isnumeric():
        a+=int(i)
print(a)