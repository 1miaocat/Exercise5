mydict = {"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
keylist = ['brand', 'year']

def removekeys(dict, keys):
    for i in keys:
        dict.pop(i)
    return mydict

print(removekeys(mydict, keylist))
