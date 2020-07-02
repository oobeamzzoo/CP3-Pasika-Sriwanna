usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "12" and passwordInput == "1234":
    print("Welcome to 168 Shop!!!")
    print('Please select the products.')
    print("1.Coca-Cola (bottle)     : 18 THB")
    print("2.Singha Beer (bottle)   : 80 THB")
    print("3.Drinking Water (bottle): 10 THB")
    selectedProduct = int(input(">>"))
    if   selectedProduct == 1:
        price1 = 18
        quantity1 = int(input("How's many bottle?"))
        result1 = price1 * quantity1
        print("total :", result1)
    elif  selectedProduct == 2:
        price2 = 80
        quantity2 = int(input("How's many bottle?"))
        result2 = price2 * quantity2
        print("total :", result2)
    elif  selectedProduct == 3:
        price3 = 10
        quantity3 = int(input("How's many bottle?"))
        result3 = price3 * quantity3
        print("total :", result3)
else : print("ERROR!!!")