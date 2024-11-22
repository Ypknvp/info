import hashlib

# Function to calculate SHA-1 hash
def encrypt_this_string(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

# Take user input and display the hash
user_input = input('Enter a string: ')
print(f"HashCode Generated by SHA-1 for:\n{user_input} : {encrypt_this_string(user_input)}")