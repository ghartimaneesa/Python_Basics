#Recurion
#When a function call itself repeatedly

def show(n):
    if n == -1:
        return
    print(n)
    show(n-1)
show(9)


def show(n):
    if n == -1:
        return
    print(n)
    show(n-1)
    print("END")
show(9)


def fact(n):
    if n == 0 or n==1 :
        return 1
    else:
        return fact(n-1) * n
num = int(input("Enter the number that you want to find the factorial of:"))
print(fact(num))

#write a recursion number to calculate the sum of first n natural numbers

def sum_n(n):
    if n == 0:
        return 0
  
    return sum_n(n-1) + n
intputs = int(input('Enter the numbers'))
print(sum_n(intputs))


#write the recursion function to print all elements in a list



def print_list(list, idx=0):
    
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ['apple', 'banaana']
print_list(fruits)