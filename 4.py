def wordfrequencies(mylist):
    res = {}
    for i in my_list:
        for word in i.split():
            res.setdefault(word, 0)
            res[word] += 1
        return res

print(wordfrequencies(['hello, world', 'the world is round', 'round is the world']))
