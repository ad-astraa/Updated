def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        return "invalidd"

def decimal_to_binary(decimal_num):
    try:
        decimal_num = int(decimal_num)
        binary = bin(decimal_num).replace("0b", "")
        return binary
    except ValueError:
        return "invalid!!"

def binary_A(bin1, bin2):
    try:
        decimal_sum = int(bin1, 2) + int(bin2, 2)
        binary_sum = bin(decimal_sum).replace("0b", "")
        return binary_sum
    except ValueError:
        return "girl pls"

def binary_S(bin1, bin2):
    try:
        decimal_diff = int(bin1, 2) - int(bin2, 2)
        binary_diff = bin(decimal_diff).replace("0b", "") if decimal_diff >= 0 else "-" + bin(abs(decimal_diff)).replace("0b", "")
        return binary_diff
    except ValueError:
        return "invaalid"

def binary_M(bin1, bin2):
    try:
        decimal_prod = int(bin1, 2) * int(bin2, 2)
        binary_prod = bin(decimal_prod).replace("0b", "")
        return binary_prod
    except ValueError:
        return "no"

def binary_D(bin1, bin2):
    try:
        if int(bin2, 2) == 0:
            return "Division by zero error"
        decimal_quotient = int(bin1, 2) // int(bin2, 2)
        binary_quotient = bin(decimal_quotient).replace("0b", "")
        return binary_quotient
    except ValueError:
        return "Invaliddd"

def bitwise_operations(a, b):
    try:
        a = int(a, 2)
        b = int(b, 2)
        operations = {
            "AND": bin(a & b).replace("0b", ""),
            "OR": bin(a | b).replace("0b", ""),
            "XOR": bin(a ^ b).replace("0b", ""),
            "NOT A": bin(~a & 0xFFFFFFFF).replace("0b", ""),
            "NOT B": bin(~b & 0xFFFFFFFF).replace("0b", ""),
            "A << 2": bin(a << 2).replace("0b", ""),
            "A >> 2": bin(a >> 2).replace("0b", ""),
            "B << 2": bin(b << 2).replace("0b", ""),
            "B >> 2": bin(b >> 2).replace("0b", "")
        }
        return operations
    except ValueError:
        return "INVALID"

def menu():
    print("Binary Operations Menu")
    print("1. Binary to Decimal Conversion")
    print("2. Decimal to Binary Conversion")
    print("3. Binary Addition")
    print("4. Binary Subtraction")
    print("5. Binary Multiplication")
    print("6. Binary Division")
    print("7. Bitwise Operations")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Choose : ")
        if choice == '1':
            binary_str = input("Enter b number: ")
            print(f"d representation: {binary_to_decimal(binary_str)}")
        elif choice == '2':
            decimal_num = input("Enter d number: ")
            print(f"b representation: {decimal_to_binary(decimal_num)}")
        elif choice == '3':
            bin1 = input("Enter first b number: ")
            bin2 = input("Enter second b number: ")
            print(f"Sum of {bin1} and {bin2} is: {binary_A(bin1, bin2)}")
        elif choice == '4':
            bin1 = input("Enter first b number: ")
            bin2 = input("Enter second b number: ")
            print(f"Difference of {bin1} and {bin2} is: {binary_S(bin1, bin2)}")
        elif choice == '5':
            bin1 = input("Enter first b number: ")
            bin2 = input("Enter second b number: ")
            print(f"Product of {bin1} and {bin2} is: {binary_M(bin1, bin2)}")
        elif choice == '6':
            bin1 = input("Enter first b number: ")
            bin2 = input("Enter second b number: ")
            print(f"Quotient of {bin1} divided by {bin2} is: {binary_division(bin1, bin2)}")
        elif choice == '7':
            bin1 = input("Enter first b number: ")
            bin2 = input("Enter second b number: ")
            results = bitwise_operations(bin1, bin2)
            if isinstance(results, dict):
                for op, res in results.items():
                    print(f"Bitwise {op} of {bin1} and {bin2}: {res}")
            else:
                print(results)
        elif choice == '0':
            print("OK LEAVING BYEE!")
            break
        else:
            print("no idk bro.")

if __name__ == "__main__":
    main()
