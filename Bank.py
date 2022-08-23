class ATM:
    def __init__(self,cardnumber,pin):
        cardnumber = 123
        pin = 321
        self.cardnumber = cardnumber
        self.pin = pin
    def checkBalance(self,number,pin1):
        print(self.cardnumber)
        if number == self.cardnumber and pin1 == self.pin :
            print("Your balance is 10000")
        else:
            print("Not your account.")

account1 = ATM(123,321)

account1.checkBalance(123,321)


