from re import I


dictionary = {"I":"Tôi", "You":"Bạn, các bạn", "It":"Nó", 
    "He":"Anh ấy, ông ấy, cậu ấy", "She":"Cô ấy, bà ấy, chị ấy",
    "We":"Chúng tôi, chúng ta", "They":"Họ, chúng nó"
    }

def translate (word):
    i = 0
    for key, value in dictionary.items ():
        if key == word:
            print (key + ": " + value)
            i = 1
            break
    if i == 0:
        print ("Xin lỗi! Từ điển không có từ bạn cần tìm.")

yourWord = input ("Nhập từ bạn cần tra: ")
translate (yourWord)
