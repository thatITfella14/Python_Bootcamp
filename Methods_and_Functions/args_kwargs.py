# the below given function adds two numbers and return 5% of the total sum

def myfunc(a,b):
    return (a+b) * 0.05

print(myfunc(40,60))

print()

# now what if we want to add more than two numbers and return 5% of the total sum??

# we can use *args to pass multiple arguments to the function

def new_func(*args):
    return sum(args) * 0.05

print(new_func(40,60,80)) # output: 9.0

print()

# conventionaly we use "*args" keyword, however, instead of "args" you can use any name such as "*spam" or "*eggs" or "*dog" as long as it starts with "*"

# another example of *args

def function_a(*args):
    for items in args:
        print(items)

function_a(1,2,3,4,5,6,7,8,9,10)

print()

# *kwargs keyword is used to pass multiple keyword arguments to the function where "kwargs" is short for "keyword arguments".

def function_b(**kwargs):
    if "fruit" in kwargs:
        print("My choice of fruit is {}.".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")

function_b(fruit = "banana", veggie = "carrot")