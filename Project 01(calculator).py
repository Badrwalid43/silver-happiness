while True:
    #1- input first number
    while True:
        try:
            first_number = float(input("enter first number: "))
            break
        except ValueError:
            print("invalid input. please enter a numeric value")
    #2- input operation type
    operation = input("enter operation type: ")
    
  
  #3- input second number
    while True:
        try:
            second_number = float(input("enter second number: "))
            break
        except ValueError:
            print("invalid input. please enter a numeric value")
   
  
  #4- print the result
    if operation == "+":
        print(first_number + second_number)
    elif operation == "-":
        print(first_number - second_number)
    elif operation == "/":
        print(first_number / second_number)
    elif operation == "*":
        print(first_number * second_number)
    else:
        print("error")

    #5- ask for repeat
    repeat = input('do you want to perform another operation (y/n): ')
    if repeat == 'n':
        break
print('program exited')
