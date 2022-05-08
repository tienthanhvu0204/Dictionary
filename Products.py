products = {
            'SMART WATCH': 550,
            'PHONE' : 1000,
            'PLAYSTATION': 500,
            'LAPTOP' : 1550,
            'MUSIC PLAYER' : 600,
            'TABLET' : 400 
           }
def displayProducts (price):
    i = 0
    for key, value in products.items():
        if value <= price:
            print (key, ":", value)
        else:
            i += 1
            continue
    if i == len (products): print ("No item has price lower than your request.")
    return

price = int (input ("Input price: "))
displayProducts (price)
