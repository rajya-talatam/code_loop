"""
Your Input and output must look something like this

Input: list1 = [12, -7, 5, 64, -14] Output: 12, 5, 64
Input: list2 = [12, 14, -95, 3] Output: [12, 14, 3]
"""
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
newlist = []
for i in list1:
    if i > 0:
        newlist.append(i)
newlist1 = [str(element) for element in newlist]


new_list = []
for j in list2:
    if j > 0:
        new_list.append(j)
print(",".join(newlist1))
print(new_list)