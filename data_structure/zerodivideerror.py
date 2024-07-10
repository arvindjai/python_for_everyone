def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero")
quotent = safe_divide(5,0)
print(quotent)