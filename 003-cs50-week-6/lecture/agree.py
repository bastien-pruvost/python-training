user_response = input("Do you agree ? ").lower()
agreed_response = ["y", "yes"]

if user_response in agreed_response:
    print("Agreed.")
else:
    print("Not agreed.")
