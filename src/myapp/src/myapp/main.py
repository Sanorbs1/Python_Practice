from myutils import add, multiply

def main():
    a, b = 3, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")

if __name__ == "__main__":
    main()