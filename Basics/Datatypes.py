#Datatypes in python
#int, float, string, list[], tuple(), set{}, dictionary{}, boolen
from datetime import datetime
num = 1 
num1 = 9.0
name = "manisha"

names = ["manisha", "anisha", "tanisha"]
salary = [1000.0, 900, 10]

print(type(num))
print(type(num1))
print(type(name))
print(type(names))
print(names[0])
print(type(salary))
print(type(salary[1]))

#if i want to print the salary of the manisha

print(f"{names[0]} is salary {salary[0]}")


#varaiable representing the library data

total_books = 100   #int
avg_bookrating = 4.5  #float
Name_of_Librarian = 'manisha' #string
is_open = True #boolean
book_names = ['Science', 'oops', 'python', 'DBMS'] #List
Location_Coordinates = (89.8982, -76.21) #tuple
contact_details = {   #Dict
    'phone': '899789636',
    'email': 'ghartimaneesa@gmail.com',
    'address':'Bhaktaput'

}

unique_genres = {'Fiction', 'non-fiction', 'Science-Fiction'} #set

print("Library Information")
print(f"Total books available in library is {total_books}")
print(f"Average book rating is {avg_bookrating}")
print(f"Librarian's Name {Name_of_Librarian}")
print(f"Is library open ? {is_open}")
print(f"List of the book availabe in library {book_names}")
print(f"Locations Cordinantes is {Location_Coordinates}")
print(f"Contact Details of the student is {contact_details}")
print(f"Unique books availabe {unique_genres}")

#Datatype conversion

a = int("10")
b = int('20')
total = a + b
print(total)

#user input

# price = float(input('Enter the price'))
# people = float(input('Enter the total no of the people'))

# print(price)

# individual_price = price/people

# print(f"One need individual has to pay {individual_price}.")


#Find the age of the person



def calculate_age(birthdate_str):
    # Convert the string to a datetime object
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    # Get today's date
    today = datetime.today()
    # Calculate age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate_str = input("Enter your birthdate (yyyy-mm-dd): ")
age = calculate_age(birthdate_str)
print(f"You are {age} years old.")