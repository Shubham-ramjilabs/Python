def divide_numbers(numerator, denominator):
    try:
        print("Trying to divide...")
        result = numerator / denominator
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError!")
        result = None
    except TypeError:
        print("Caught a TypeError!")
        result = None
    else:
        print("Division was successful!")
    finally:
        print("Execution of finally block!")
    return result

# Testing the function
print(divide_numbers(10, 2))  # Normal case
print(divide_numbers(10, 0))  # ZeroDivisionError
print(divide_numbers(10, 'a'))  # TypeError
