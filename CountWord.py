
def countWord (massage):
    textList = massage.split ()
    result = {}
    for word in textList:
        key = word.lower ()
        key = key.strip ()
        if key in result.keys ():
            result [key] += 1
        else:
            result.update ({key: 1})
    return result
massage = input ("input massage: ")
text = countWord (massage)
print (text)
