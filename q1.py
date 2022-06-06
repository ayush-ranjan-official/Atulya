list = eval(input("Enter the list :"))

str = input('Enter asc/desc/none :')
if str == 'asc':
    list.sort()
    print(list)
elif str == 'desc':
    list.sort(reverse=True)
    print(list)
elif str == 'none':
    print(list)