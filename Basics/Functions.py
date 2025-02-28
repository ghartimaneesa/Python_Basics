#Block of statements that perform the specific task
#function can be used multiple times to perform the same task
# Benefits:
#1.No of lines decreases and reduandancy also decreases

#types of fucntion in python
# 1.Built-in Function
# 2.User defined Function

def cal_sum(a,b):
    sum = a + b
 
    return sum
print(cal_sum(1,2))
cal_sum(9,0)


#create a function that calculates the average if three numbers

def avg(a,b,c):
    avg1 = (a+b+c)/3
    return avg1
print(avg(2,4,6))

#Default Parameter
#Assingning a default value to parameter, which is used when no arguement is passed

def cal_prod (a=9,b=0):
    prod = a * b
    return prod
print(cal_prod())


# #WAF to print the length of a list(list is the parameter)
cities = ['kathmandu', 'bhaktapur', 'dharan']
print(len(cities))
name = ['srk','aryan','manisha','anisha']
def cities_len(list):
    print(len(list))

cities_len(cities)

def name_len(l1):
    print(len(l1))
name_len(name)

# #WAF to print the elements of a list in a single line.(list is the parameter)

name1 = ['manisa','anisa','manish','hari']

def print_listelements(list):
    for item in list:
        print(item,end=" ")
print_listelements(name1)

#WAF to find the factorial of n.(n is the parameter)

def fact(n):
    facto = 1
    for i in range(1, n+1):
        facto *=i
    return facto
num  = int(input("Enter Number:"))
print(fact(num))

#WAF to convert the usd into npr

def usd_conversion(usd_value):
    npr_value = usd_value * 135
    print(usd_value,"USD =",npr_value,"NPR")

usd = int(input("Enter the usd value"))
usd_conversion(usd)

#WAF that takes the number input and if that number is odd then it should return string "ODD" ELSE "EVEN"

def cal_odd_even(a):
    if a % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
num = int(input("Enter the number:"))
cal_odd_even(num)