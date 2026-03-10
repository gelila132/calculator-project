print("******Calculator********")
while True:
     num1=input("Enter first number: ")
     num2=input("Enter second number: ")
     if num1.isdigit() and num2.isdigit():
         num1=int(num1)
         num2=int(num2)
         print("Select operation:")
         print("1.Addition")
         print("2.Subtraction")
         print("3.Multiplication")
         print("4.Division")
         print("5.Exit")    
         choice=int(input())
         if choice==1:
             print("The sum is:", num1+num2)
         elif choice==2:
             print("The difference is:", num1-num2)      
         elif choice==3:
             print("The product is:", num1*num2) 
         elif choice==4:
             if num2==0:
                 print("Division by 0 is not allowed")
             else:
                 print("The quotient is:", num1/num2)

         elif choice==5:
             print("Calculator Closed")
             break
         else:
             print("Invalid Input")
     else:
             print("Invalid Input. Please input a number.")


