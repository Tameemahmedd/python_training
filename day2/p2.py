li=list(input("Enter the list of numbers: "))
dict={}
for num in li:
    if num==" ":
        continue
    dict[num]=li.count(num)
print(dict)