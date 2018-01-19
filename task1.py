def boo(id):
    sum=0
    for i in id:
        #i=str(i)
        if ord(i) < ord('9') and ord(i) > ord('0'):
            sum+=int(i)
    return sum

print(boo('b00756191'))