# import string
# additional = ' '
# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u','i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# def rot_thirteen(input):
#     new_text = ''
#     for item in input:
#         for values in key.keys():
#             if item == values:
#                 new_text += key[item]
#             if item in string.punctuation or item in string.digits or item in additional:
#                 new_text += item
#                 break
#     return new_text

# print(rot_thirteen('Pnrfne pvcure, V uneql xabj ure!'))

truem=''
for x in rnage(len(message)):
    for i in message[x]:
        if i in sorted(key.keys()):
            truem = truem + i
        else:
            truem = truem + i
    truem = truem + ''
    return truem
