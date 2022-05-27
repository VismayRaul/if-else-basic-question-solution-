# a= int(input("enter number : "))
# def see(a):
#     if a%5==0:
#         print("hello")
#     else:
#         print("bye")
# see(a)

# eveoddnum = int(input("enter number"))
# def eve(eveoddnum):
#     if eveoddnum%2==0:
#         print("even")
#     else:
#         print("odd")
# eve(eveoddnum)

# divbysev = int(input("enter no."))
# def div(divbysev): 
#     if divbysev%7==0:
#         print("divisible")
#     else:
#         print("not divisible")
# div(divbysev)

# voterage=int(input("enter age : "))
# def voter(voterage):
#     if voterage < 18:
#         print("not eligible")
#     else:
#         print("eligible")
# voter(voterage)

# userinput= int(input("enter units : "))
# def input(userinput):
#     if userinput<=100:
#         print("0 Rs")
#     elif userinput>=100 and userinput <=200:
#         a= (userinput-100)*5
#         print(a)
#     else:
#         a=(userinput-200)*10+500
#         print(a)
# input(userinput)

# any_number = input("Enter any number : ")
# def num(any_number):
#     print(any_number[len(any_number)-1]," is the last digit of the number.")
# num(any_number)

# enter_number = input("Enter any number : ")
# def enum(enter_number):
#     last_digit = int(enter_number[len(enter_number)-1])
#     if last_digit%3 == 0:
#         print(last_digit," is dividible by 3.")
#     else:
#         print(last_digit," is not divisible by 3.")
# enum(enter_number)

# precentage = int(input("enter percentage"))
# def per(precentage):
#     if precentage>90:
#         print("A")
#     elif precentage>80 and precentage<=90:
#         print("B")
#     elif precentage>=60 and precentage<=80:
#         print("C")
#     else:
#         print("D")
# per(precentage)

# cost_price= int(input("Enter cost price of a bike : "))
# def cost(cost_price):
#     if cost_price >100000:
#         interest = 15
#     elif cost_price>50000 and cost_price<= 100000:
#         interest = 10
#     else:
#         interest = 5
#     tax_payable = (cost_price*interest)/100
#     print(tax_payable," road tax to be paid")
# cost(cost_price)

# leap_year = int(input("enter the year to be checked as leap year"))
# def year(leap_year):
#     if leap_year%4 == 0 and leap_year%100!=0 or leap_year%400 == 0  :
#         print("is a leap year")
#     else :
#         print("not a leap year")
# year(leap_year)

# number_day = int(input("enter no. from 1 t0 7 : "))
# def day(number_day):
#     if number_day == 1:
#         print("1 for sunday")
#     elif number_day == 2:
#         print("2 for monday")
#     elif number_day == 3:
#         print("3 for tuesday")
#     elif number_day == 4:
#         print("4 for wednesday")
#     elif number_day == 5:
#         print("5 for thursday")
#     elif number_day == 6:
#         print("6 for friday")
#     else:
#         print("7 for saturday")
# day(number_day)

# number_entry = int(input("enter number from 1 to 12 : "))
# def enter(number_entry)
#     month_day = ["january 31","feb 29","march 31","april 30","may 31","june 30","july 31","aug 31","sept 30","oct 31","nov 30","dec 31" ]
#     print(month_day[number_entry-1])
# enter(number_entry)

# city_name = input("enter city name")
# def city(city_name):
#     if city_name == "Delhi":
#         print("Red Fort")
#     elif city_name == "Agra":
#         print("Taj Mahal")
#     elif city_name == "Jaipur":
#         print("Jal Mahal")
#     else:
#         print("City not Mentioned")
# city(city_name)

# three_digit_num = input("Enter any number")
# def digit(three_digit_num):
#     index=len(three_digit_num)
#     if index == 3:
#         print(three_digit_num," is 3 digit no.")
#     else:
#         print(three_digit_num," is not a 3 digit no.")
# digit(three_digit_num)

# first_num = int(input("enter first no. : "))
# second_num = int(input("enter second no. : "))
# def num(first_num,second_num):
#     if first_num < second_num:
#         print(first_num, " is smallest number")
#     else:
#         print(second_num, " is smallest number")
# num(first_num,second_num)

# first = int(input("enter first no. : "))
# second = int(input("enter second no. : "))
# def num(first,second):
#     if first > second:
#         print(first," is largest number")
#     else:
#         print(second," is largest number")
# num(first,second)

# finding_no = int(input("Enter any positive or negetive no. : "))
# def find(finding_no):
#     if finding_no<0:
#         print(finding_no," is negative")
#     elif finding_no >0:
#         print(finding_no," is positive")
#     else:
#         print("no. is 0")
# find(finding_no)

# divisible_of = int(input("enter number : "))
# def divid(divisible_of):
#     if divisible_of%2 == 0 and divisible_of%3 == 0:
#         print(divisible_of," is divisible by both 2 & 3")
#     else:
#         print(divisible_of," is not divisible")
# divid(divisible_of)

# first_age = int(input("Enter first age"))
# second_age = int(input("Enter second age"))
# third_age = int(input("Enter third age"))
# forth_age = int(input("Enter forth age"))
# youngest = [first_age, second_age, third_age, forth_age]
# youngest.sort()

# character= input("Enter Character : ")
# def char(character):
#     if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
#         print(character," is a vowel")
#     else:
#         print(character," is not a vowel")
# char(character)

# working_days = int(input("Enter total no. of working days"))
# absent_days = int(input("Enter total no. of absent days"))
# present_day_percent=((working_days-absent_days)/working_days)*100
# # print(present_day_percent)
# def present(present_day_percent):
#     if present_day_percent >= 70:
#         print("applicable")
#     else:
#         print("not applicable")
# present(present_day_percent)

# salary = int(input("Enter salary"))
# years = int(input("Enter years"))
# def bonus_amount(salary,years):
#     if years > 10:
#         bonus=(10*salary)/100
#         print("bonus amount : ",bonus)
#     elif years>=6 and years<=10:
#         bonus=(8*salary)/100
#         print("bonus amount : ",bonus)
#     else:
#         bonus=(5*salary)/100
#         print("bonus amount : ",bonus)
# bonus_amount(salary,years)

# marked_price= int(input("Enter marked price"))
# def disc(marked_price):
#     if marked_price >10000:
#         percent = 20
#     elif marked_price>7000 and marked_price<=10000:
#         percent = 15
#     else:
#         percent = 10
#     discount= (marked_price*percent)/100
#     net_amount = marked_price-discount
#     print(net_amount)
# disc(marked_price)

# percentage = int(input("Enter percentage"))
# def pert(percentage):
#     if percentage<40:
#         print("Failed")
#     elif percentage>=40 and percentage<55:
#         print("Fair")
#     elif percentage>=55 and percentage<65:
#         print("Good")
#     else:
#         print("Excellent")
# pert(percentage)

# first_side = input("Enter first side : ")
# second_side = input("Enter second side : ")
# third_side = input("Enter third side : ")
# def triangle(first_side,second_side,third_side):
#     if first_side == second_side == third_side:
#         print("Equilateral triangle")
#     elif first_side == second_side or second_side == third_side or first_side == third_side :
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")
# triangle(first_side,second_side,third_side)

# first_number = int(input("Enter first number : "))
# operator = input("Enter operator : ")
# second_number = int(input("Enter second number : "))
# def ans(first_number,operator,second_number):
#     if operator == "+":
#         final_ans = first_number+second_number
#         print(final_ans)
#     elif operator == "-":
#         final_ans = first_number-second_number
#         print(final_ans)
#     elif operator == "*":
#         final_ans = first_number*second_number
#         print(final_ans)
#     elif operator == "/":
#         final_ans = first_number/second_number
#         print(final_ans)
#     elif operator == "%":
#         final_ans = first_number%second_number
#         print(final_ans)
#     elif operator == "**":
#         final_ans = first_number**second_number
#         print(final_ans)
#     else:
#         final_ans = first_number//second_number
#         print(final_ans)
# ans(first_number,operator,second_number)
