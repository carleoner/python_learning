from itertools import product

priceData = {
        "Banana": 2,
        "Bread": 4
    }

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add item, press Q to quit: ")
        if details == 'A':
            product = input("Enter product: ")
            if product in priceData.keys():
                quantity = int(input("Enter quantity: "))
                buyingData.update({product: quantity})
            else:
                print("Product not found")
        elif details == 'Q':
            enterDetails = False
        else:
            print("Pleas enter a correct option")
    return buyingData

def getPrice(product, quantity):
    subtotal = priceData[product] * quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal

def getDiscount(billAmount, membership):
    billAmountprimo = billAmount
    discount = 0
    if billAmount >= 25:
        if membership == "gold":
            billAmount *= 0.80
            discount = 20
        elif membership == "silver":
            billAmount *= 0.90
            discount = 10
        elif membership == "bronze":
            billAmount *= 0.95
            discount = 5
        print(str(discount) + '% off for ' + str(membership) + ' membership on total amount: ' + str(billAmountprimo))
    else:
        print("No discount on amount less than $25")
    return billAmount

def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += int(getPrice(key, int(value)))
    billAmount = getDiscount(billAmount, membership)
    print("Amount to pay: $" + str(billAmount))



buyingData = enterProducts()
membership = input("Enter your membership option (gold / silver / bronze): ")
makeBill(buyingData, membership)