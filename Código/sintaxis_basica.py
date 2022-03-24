def hello_name(name:str)->None:
    """ This is a function that prints a greeting. """

    print(f"Hello, {name}!")
    return None


user_name = input("What is your name?: ") # Ingreso TEAMmates

# Call the function "hello_name" with the argument "user_name".
hello_name(user_name)  # Hello, TEAMmates!
