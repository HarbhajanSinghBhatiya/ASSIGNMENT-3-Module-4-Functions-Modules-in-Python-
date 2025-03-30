def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number = int(input("Enter a number: "))

fact_result = factorial(number)
print(f"The factorial of {number} is: {fact_result}")
