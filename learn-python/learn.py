

def askUserInput():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return int(input("Enter your choice: "))

def calculateAddition():
    return first + second;
def calculateSubtraction():
    return first - second;
def calculateMultiply():
    return first * second;
def calculateDivide():
    return first / second;

# Main method to run program
if __name__ == '__main__':
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    # start loop
    while True:
        # ask user input
        result = askUserInput()
        if(result == 1):
            print("Addition: ", calculateAddition())
        elif(result == 2):
            print("Subtraction: ", calculateSubtraction())
        elif(result == 3):
            print("Multiply: ", calculateMultiply())
        elif(result == 4):
            print("Divide: ", calculateDivide())
        else:
            print("Exit")
            break
        
            
        
    

    


    
