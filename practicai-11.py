try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b == 0:
        raise ValueError("Division by zero is not allowed")

    print("Result:", a / b)

except ValueError as e:
    print("Error:", e)

except Exception:
    print("An unexpected error occurred")