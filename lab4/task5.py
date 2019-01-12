def capitalize(chr):
    return chr.capitalize()

def recur(plist):
    ls=[]
    for st in plist:
        if isinstance(st, list):
            ls.append(recur(st))
        else:
            ls.append(st.upper())
    return ls

ls=['kulwant', 'singh' ,['kulawnt', 'singh']]
print(recur(ls))

def iter(item):
    if(isinstance(item, list)):
        return list(map(iter, item))
    return item.upper()

print(list(map(iter, ls)))

