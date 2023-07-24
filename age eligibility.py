Age=int(input("Enter your age : "))
if Age<18:
    print("You are a minor")
elif Age>=18 and Age<65:
    print("You are an adult")
elif Age>=65:
    print("You are a senior")
