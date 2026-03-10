# print("*******MENU*******")
# menu={1:"Cookies , $5,
#       2:"Chips , $3",
#       3:"Soda , $2"}
# print(menu)
# print("Input the nos to select the items:")
# print("done if completed")
# selected=[]
# total=0

# while True:
#     choice=input()
#     if choice.isdigit():
#      choice=int(choice)
#      if choice==1:
#             total+=5
#             print("You have selected",menu[choice])
#             selected.append(menu[choice])
#      elif choice==2:
#             total+=3
#             print("You have selected",menu[choice])
#             selected.append(menu[choice])
#      elif choice==3:
#             total+=2
#             print("You have selected",menu[choice])
#             selected.append(menu[choice])
#     elif choice=="done":
#      print("Your order is completed")
#      print("You selected:", selected)
#      print("Total cost: $", total)
#      break
#     else:print("Invalid input. Please enter a number or 'done'.")

# print("******Calculator********")
# while True:
#     num1=input("Enter first number: ")
#     num2=input("Enter second number: ")
#     if num1.isdigit() and num2.isdigit():
#         num1=int(num1)
#         num2=int(num2)
#         print("Select operation:")
#         print("1.Addition")
#         print("2.Subtraction")
#         print("3.Multiplication")
#         print("4.Division")
#         print("5.Exit")    
#         choice=int(input())
#         if choice==1:
#             print("The sum is:", num1+num2)
#         elif choice==2:
#             print("The difference is:", num1-num2)      
#         elif choice==3:
#             print("The product is:", num1*num2) 
#         elif choice==4:
#             if num2==0:
#                 print("Division by 0 is not allowed")
#             else:
#                 print("The quotient is:", num1/num2)

#         elif choice==5:
#             print("Calculator Closed")
#             break
#         else:
#             print("Invalid Input")
#     else:
#             print("Invalid Input. Please input a number.")


