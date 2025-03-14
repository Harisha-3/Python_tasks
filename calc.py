num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
ch = int(input("Enter your choice:"))
while(ch != 0):

                if(ch==1):
                        print(num1," ","+"," ",num2," ","="," ",num1+num2)
                if(ch==2):
                        print(num1," ","-"," ",num2," ","="," ",num1-num2)
                if(ch==3):
                        print(num1," ","*"," ",num2," ","="," ",num1*num2)
                if(ch==4):
                        if(num2!=0):
                                print(num1," ","/"," ",num2," ","="," ",num1/num2)
                        else:
                                print("Can't be divisible by 0")
                print("\n******\n")

                ch = int(input("Enter\n 0 -> Exit\n 1 -> Add\n 2 -> Subtract\n 3 -> Multiply\n 4 -> Divide\n >>"))
