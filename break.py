number = int(input("What is your number? "))
while number != -1:
    print("Let's get started")
    while True:
        data = input("DATA: ")
        if data == "":
            break
        print(data)
    number = int(input("What is your number? "))
print("Good bye.")
