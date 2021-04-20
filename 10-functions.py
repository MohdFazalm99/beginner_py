def say_hi():
    # in python function is declared using def .
    print("Hello user")


say_hi()


# here we are calling our function

def say_name(name):
    # this is an example of function with parameters
    print("Hello " + name)


say_name("Mike")


def say_age(name, age):
    print("Hello " + name + "you are " + str(age))
# suppose we gave age in integer so we have to use str function so that python will understand that the number is string


say_age("Steve", 45)
say_age("Mike", 36)
