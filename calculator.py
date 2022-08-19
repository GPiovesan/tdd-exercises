def main():
    print("Welcome! \nThis is the tdd calculator!")

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def sum_list(values):
    total = 0
    for v in values:
        total = total + v
    return total

def max_value(values):
    return max(values)

if __name__ == "__main__":
    main()