
def countWord (massage):
    textList = massage.split ()
    result = {}
    for word in textList:
        key = word.lower ()
        key = key.strip ()
        if key in result.keys ():
            result [key] = result [key] + 1
        else:
            result.update ({key: 1})
        # if key in result.keys ():
        #     result.get(key) + 1
        # else:
        #     result.update ({key : 0})
    return result
massage = input ("input massage: ")
text = countWord (massage)
print (text)

# result = {"I":"Tôi", "You":"Bạn"}
# result.update ("I")
# print (result)