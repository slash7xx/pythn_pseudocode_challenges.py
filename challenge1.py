test = int(input("Give me a number:"))
test2 = int(input("Another one:"))

def addition(test,test2):    
    return (test + test2)

def subtraction(test,test2):
    return (test - test2)

def division(test,test2):
    return (test / test2)

def Multiplication(test,test2):
    return (test * test2)


print("Multiplication Answer:",Multiplication(test,test2))
print("\nANSWERS:\nAddition Answer:",addition(test,test2))
print("Division Answer:",division(test,test2))
print("Subtraction Answer:",subtraction(test,test2))


