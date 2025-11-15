# Q 1: Given students = {'Alice': 88, 'Bob': 73, 'Cara': 95, 'Dan': 80}, print the names of students who scored above 80.

students = {
    'Alice': 88,
    'Bob': 73,
    'Cara': 95,
    'Dan': 80
    }

for key,value in students.items():
    if value > 80:
        print(key)

print()
print()

# Q 2: Add a new entry 'Ella': 91 to the dictionary above and print the updated dictionary.

students["Ella"] = 91

print(students)

print()
print()

# Q 3: Reverse the key-value pairs in the dictionary above so scores are keys and names are values. Print the result.

reversed_students = {}

for key,value in students.items():
    reversed_students[value] = key

print(reversed_students)

print()
print()

# Q 4: Given employee = {'name': 'John', 'hire_year': 2020, 'dept': 'IT'}, change the department to 'HR' and print the dictionary.

employee = {
    'name': 'John',
    'hire_year': 2020,
    'dept': 'IT'
    }

print(employee)

employee['dept'] = "HR"

print(employee)

print()
print()

# Q 5: For prices = {'apple': 0.99, 'orange': 1.29, 'banana': 0.59}, print all keys in alphabetical order.

prices = {'apple': 0.99,
          'orange': 1.29,
          'banana': 0.59
          }

for key in sorted(prices):
    print(key)