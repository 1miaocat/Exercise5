def findvalue(mydict,val):
    for i in mydict.items():
        # for j in val:
            if val == i[1]:
                print(i)
v = 2
d = {'a' : 1, 'b': 2, 'c': 2, 'd': 4}

findvalue(d,v)

def findvalue(mydict, val):
    mylist =[]
    for key in mydict.keys():
        if val == mydict[key]:
            mylist.append(key)
        return mylist
