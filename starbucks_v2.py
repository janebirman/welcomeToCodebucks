import turtle
import math

class Starbucks:
    def __init__(self):
        self.itemizedReceipt = []
        self.sizesOfDrinks = 0

    def setBalance(self, balance=0.0):
        """Set the customer's starting balance."""
        self.balance = balance

    def addItemToReceipt(self, drinkName):
        self.itemizedReceipt.append(drinkName)

    def getOrderName(self, drinkName):
        self.drinkName = drinkName


    def checkIfInStock(self, drinkName):
        print(drinkName)
        if (drinkName=="Drip coffee") or (drinkName=="Latte") or (drinkName=="Vanilla Latte") or (drinkName=="Cappuccino") or (drinkName=="Mocha") or (drinkName=="Green tea") or (drinkName=="Chai Latte") or (drinkName=="Caramel Frappuccino") or (drinkName=="Mocha Frappuccino") or (drinkName=="Green tea Frappuccino"):
            #if drinkName in itemizedReceipt:
            #    print("You have already ordered this drink!")
            #    return True
            #else:
            self.addItemToReceipt(drinkName)
            return True
        else:
            print("Sorry, we do not sell that item. Let's go back to the menu!")
            return False

    def getDrinkSize(self, drinkSize):
        self.drinkSize = drinkSize
        if((drinkSize=="tall") or (drinkSize=="grande") or (drinkSize=="venti")):
            sizesOfDrinks=0
            if (drinkSize == "tall"):
                #sizesOfDrinks = sizesOfDrinks + 1;
                return 1
            if (drinkSize == "grande"):
                #sizesOfDrinks = sizesOfDrinks + 2;
                return 2
            if (drinkSize == "venti"):
                #sizesOfDrinks = sizesOfDrinks + 3;
                return 3
            #return int(sizesOfDrinks)
        else:
            print("Sorry, we do not have that size. I will assume you wanted a tall.")
            return False

    def printReceipt(self):
        print(*self.itemizedReceipt, sep='\n')





def main():
    myOrder = Starbucks()
    done = False
    print("Welcome to Starbucks! Here is the menu:")
    print("1. Drip coffee\n2. Latte\n3. Vanilla Latte\n4. Cappuccino\n5. Mocha\n6. Green tea\n7. Chai Latte\n8. Caramel Frappuccino\n9. Mocha Frappuccino\n10. Green tea Frappuccino\n")
    print("Your size options are tall, grande, and venti.\n")
    numberOfItems=0
    sizesOfDrinks=0
    while not done:
        action = input("""\nWhat would you like to do now?
            Order a drink (o), pay for drink (pay), print receipt (pr),
            quit (q)?
            """)

        if action == "o":
            drinkName = input("What drink would you like?")
            myOrder.getOrderName(drinkName)
            myOrder.checkIfInStock(drinkName)
            drinkSize = input("What size would you like?")
            sizesOfDrinks = sizesOfDrinks + myOrder.getDrinkSize(drinkSize)
            numberOfItems = numberOfItems + 1

        elif action == "pay":
            if numberOfItems< 1:
                print("You must order something if you want to pay!")
                continue
            else:
                print("Press pr to see your receipt.")
        elif action == "pr":
            print("Your items are")
            myOrder.printReceipt()

            price = ((numberOfItems+sizesOfDrinks)*3)
            print("Your total is: $",price)
        elif action == "q":
            print("Enjoy your order!")
            break
        else:
            print("Sorry, I didn't understand that.")

if __name__ == '__main__':
    main()
