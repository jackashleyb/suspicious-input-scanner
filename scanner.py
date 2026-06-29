user_input = input("Enter text to scan: ")

if "OR 1=1" in user_input.upper():
    print("Possible SQL Injection detected")
else:
    print("No threats detected")

