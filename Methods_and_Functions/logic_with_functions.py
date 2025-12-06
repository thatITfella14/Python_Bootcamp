def even_check(number):
    return number % 2 == 0

print(even_check(21)) # Output : False

print()

print(even_check(20)) # Output: True

print()

# RETURN TRUE IF ANY NUMBER IS EVEN IN THE LIST

def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass

my_list = [1,3,5,13,17,27,2,15,93]

print(check_even_list(my_list))

print()

# In the above given example what if we wanted to return "False"? A begginer would make a mistake "else: return False"
# Why is this wrong??? Because think of return as a breakout statement. If you put return False that means anytime there's an Odd number it'll breakout without checking the rest of the numbers in that list. So if a first number in the list is an Odd number the function will return False without checking rest of the numbers in the list. For example in list_a = [1,3,4,6] will return False because the first number is an Odd number, however, it should return True because there's an even number in the given list. This is why we use "pass" and not return False.

# Below given is how you return a False:

def check_even_num_in_list(number_list):
    for num in number_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

list_1 = [1,3,5,6]

print(check_even_num_in_list(list_1)) # Output: True; because there's an even number in the list

print()

list_2 = [1,7,9,11]

print(check_even_num_in_list(list_2)) # Output: False; because there's no even numbers in the list. Unlike previously this'd return "False" instead of returning nothing.

print()

# Now in the example below instead of returning True or False, we want to return all even numbers from a list should they exist, if none found there return nothing.

def return_even(provided_list):
    even_numbers = [] # this is a placeholder list
    for num in provided_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

list_a = [1,3,5,19,11,93,75]

print(return_even(list_a)) # the output will be none since there's no even numbers in the list

print()

list_b = [13,17,4,19,16,39,49,50,74,148,61]

print(return_even(list_b)) # the output will be a list of even numbers