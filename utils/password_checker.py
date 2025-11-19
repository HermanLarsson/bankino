import hashlib

# take a user inputted password and userid
personnummer = input("Enter personnummer: ")
user_password = input("Enter password: ")

# hash it
hash = hashlib.new("SHA256")
hash.update(user_password.encode())

hashed_password = hash.hexdigest()

print(hashed_password)

# check the hashed password to the hashed password of that user in the db. 