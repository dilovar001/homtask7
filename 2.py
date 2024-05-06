list1 = ["Emma", "Jone", "", "Kelly", None, "Eric", ""]
list2 = []

for i in list1:
    if i:
        list2.append(i)

print(list2)