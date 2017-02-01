lst = [1, [2, 3], 4, [[6, 7]]]
def flatten(x):
    new_list=[]
    for i in x:
        if isinstance(i, list):
            for y in i:
                if isinstance(y, list):
                    new_list+=flatten(y)
                else:
                    new_list.append(y)
        else:
            new_list.append(i)
    return new_list

print (flatten(lst))
