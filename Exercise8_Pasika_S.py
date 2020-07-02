usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "oobeamzzoo" and passwordInput == "1234":
    print("Welcome to 168 Shop!!!")
    print('Please select the products.')
    print("1.Coca-Cola (bottle)     : 18 THB")
    print("2.Singha Beer (bottle)   : 80 THB")
    print("3.Drinking Water (bottle): 10 THB")
    selectedProduct = int(input(">>"))
    if   selectedProduct == 1:
        qty1 = int(input("How's many bottle?"))
        print("total :",18 * qty1)
    elif  selectedProduct == 2:
        qty2 = int(input("How's many bottle?"))
        print("total :", 80 * qty2)
    elif  selectedProduct == 3:
        qty3 = int(input("How's many bottle?"))
        print("total :", 10 * qty3)
else : print("ERROR!!!")