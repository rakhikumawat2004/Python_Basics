'''def apply_operation(x, y, operation_func):
        return operation_func(x, y)

def add(a, b):
        return a + b

result = apply_operation(5, 3, add)
print(result) # Output: 8

def create_multiplier(factor):
        def multiplier(number):
            return number * factor
        return multiplier

double = create_multiplier(2)
print(double(5)) # Output: 10'''

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)