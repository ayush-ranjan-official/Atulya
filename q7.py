my_list = eval(input('Enter the list :'))
freq = {}
for item in my_list:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1
a=0
b=0
for key, value in freq.items():
    if value > a:
        a=value
        b=key
print("Element with maximum frequency :",b)