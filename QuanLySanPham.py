# Product database, dictionary chứa danh sách sản phẩm gồm ID và tên
productDatabase = {
            101:'SMART WATCH',
            102:'PHONE',
            103:'PLAYSTATION',
            104:'LAPTOP',
            105:'MUSIC PLAYER',
            106:'TABLET' 
           }

def modifyProduct (productDB, prodID, prodName):
    if prodID in productDB.keys ():
        productDB[prodID] = prodName
    else:
        productDB.update ({prodID:prodName})

def delProduct (productDB, prodID):
    if prodID in productDB.keys ():
        del productDatabase[prodID]
    else:
        print ("ProductID does not exist.")
        return

option = "Y"
action = ""

# Vòng lặp lựa chọn, N: thoát khỏi vòng lặp, Y: thực hiện yêu cầu sau đó hỏi lại, khác: thoát.
while option == "y" or option == "Y":
    print ("Do you want to modify your list?")
    option = input ("Your option (Y/N): ")
    if option == "n" or option == "N": 
        break
    elif option == "y" or option == "Y":
        # Thực hiện yêu cầu, lặp lại câu hỏi nếu lựa chọn sai.
        print ("What do you want to do?")
        while True:
            action = input ("Your choice? (a = add, m = modify, d = delete): ")
            if action == "a":
                print ("Add new item.")
                # Cho người dùng nhập product ID, nếu đã có thì nhập lại, chưa có thì nhập tiếp product name.
                while True:
                    prodID = int (input ("Input new product ID: "))
                    if prodID in productDatabase.keys ():
                        print ("This product ID has already been used.")
                    else:
                        break
                prodName = input ("Input new product name: ")
                # gọi hàm modifyProduct để thêm mới, sau đó thoát vòng lặp lựa chọn action.
                modifyProduct (productDatabase, prodID, prodName)
                break
            elif action == "m":
                print ("Modify an item.")
                # Cho người dùng nhập ID, nếu đúng thì nhập tiếp tên mới.
                while True:
                    prodID = int (input ("Input product ID: "))
                    if prodID not in productDatabase.keys ():
                        print ("This product ID does not exist.")
                    else:
                        break
                prodName = input ("Input new product name to replace: ")
                # gọi hàm modifyProduct để sửa, sau đó thoát vòng lặp lựa chọn action.
                modifyProduct (productDatabase, prodID, prodName)
                break
            elif action == "d":
                print ("Delete an item.")
                # Cho người dùng nhập ID, đúng thì thoát vòng lặp
                while True:
                    prodID = int (input ("Input product ID to delete: "))
                    if prodID not in productDatabase.keys ():
                        print ("This product ID does not exist.")
                    else:
                        break
                # Gọi hàm delProduct để xóa
                delProduct (productDatabase, prodID)
                break
            else:
                print ("Please, input your choice!")
    else:
        print ("Invalid value.")
        break

print ("Your product list")
for item in productDatabase.keys ():
    print ("ProdID:", item, "Name:", productDatabase[item])
