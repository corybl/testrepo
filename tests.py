introduction = "This is a calculator that can do addition and subtraction. \n \n"

proceed = "yes"
answer = "hello"

def add(a, b):
    return int(a) + int(b)

def subtract(a, b):
    return int(a) - int(b)
    
def multiply(a, b):
    return int(a) * int(b)

with open("test.txt" , "w") as f:
        f.write(introduction)

while proceed == "yes":

    opr = input("\nGive me your choice of operator : ")

    while opr != "+" and opr != "-" and opr != "*":
        print("\nOperator needs to be +, - or *")
        opr = input("Give me your choice of operator : ")
     
    num1 = input("\nGive me a first number : ")
    num2 = input("\nGive me a second number : ")

    if(opr == "+"):
        answer = str(add(num1, num2))
        print("\n" + str(num1) + " " + opr + " " + str(num2) + " = " + answer)
        with open("test.txt" , "a") as f:
            f.write(str(num1) + " " + opr + " " + str(num2) + " = " + answer + "\n")

    elif(opr == "-"):
        answer = str(subtract(num1, num2))
        print("\n" + str(num1) + " " + opr + " " + str(num2) + " = " + str(subtract(int(num1), int(num2))))
        with open("test.txt" , "a") as f:
            f.write(str(num1) + " " + opr + " " + str(num2) + " = " + answer + "\n")

    elif(opr == "*"):
        answer = str(multiply(num1, num2))
        print("\n" + str(num1) + " " + opr + " " + str(num2) + " = " + str(multiply(int(num1), int(num2))))
        with open("test.txt" , "a") as f:
            f.write(str(num1) + " " + opr + " " + str(num2) + " = " + answer + "\n")

    proceed = input("\nWould you like to continue ? : ")