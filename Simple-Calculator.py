#Calculator: Addition, Subtraction, Multiplication, Division

#This function adds two number:
def add(x,y):
    return x+y

#This function subtracts two numbers:
def substract(x,y):
    return x-y

#This function multiplies two numbers:
def multiply(x,y):
    return x*y

#This function divides two values  
def divide(x,y):
    return x/y

print("Select Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    #take input from users
    choice = input("Enter Choice(1/2/3/4): ")
     
    # Check if the choice is one of the four options or not
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

        
        #Check if the user want another calculation or not
        #then we will break the while loop if answer is "no"

        next_calculation = input("Do you want to solve another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
            print("Invalid Input")

            


    