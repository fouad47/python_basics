#args & kwargs
def user_info(name, age=0, city="Tucson"):
    '''This function prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Janet", 58, "Oklahama City")
user_info("Micah")
user_info(age=56, name="Kadeem")

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")


'''

application Function (*args and **kwargs)
This function demonstrates how to handle an unknown number of arguments.

def application(fname, lname, email, company, *args, **kwargs):

*args (non-keyword arguments): This allows the function to accept any number of additional positional arguments. 
They are collected into a tuple named args. For example, application("Jane", "Doe", "jdoe@example.com", "ABC Corp", "arg1", "arg2") 
would result in args being ('arg1', 'arg2').

**kwargs (keyword arguments): This allows the function to accept any number of additional keyword arguments. They are collected 
into a dictionary named kwargs. For example, application("Jane", "Doe", "jdoe@example.com", "ABC Corp", department="HR", 
start_date="2024-01-01") would result in kwargs being {'department': 'HR', 'start_date': '2024-01-01'}.

The code snippet for the application function is incomplete, but its purpose is to show how to define a function that 
can accept a flexible number of arguments. The final print statement shows how to access the explicitly defined arguments 
(fname, lname, company, email).

'''