import bcrypt


# In a real application, this should be stored securely in a database
stored_hash = None

def register_user():
    global stored_hash
    print("Enter a username: ")
    name = input()
    print("Enter a password: ")
    password = input()

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    stored_hash = hashed_password

    print(f"User {name} registered successfully!")

def login_user():

    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:

        print("Enter username: ")
        name = input()
        print("Enter password: ")
        password = input()

        if stored_hash is None:
            print("No user registered yet.")
            return

    # Check the provided password against the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print("Login successful!")
            break
        else:
            attempts +=1
            print("Login failed. Incorrect password.")

    if attempts == max_attempts:
        print("Login Failed. Maximum attempts reached")
