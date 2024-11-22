Below is an example Python program that demonstrates a dictionary attack for cracking a password. The program uses a list of potential passwords from a file and tries to match them with a given hashed password.

### Code Example

```python
import hashlib

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(hashed_password, dictionary_file):
    """
    Attempts to crack a hashed password using a dictionary attack.
    Parameters:
        hashed_password: The SHA-256 hash of the target password.
        dictionary_file: The file containing potential passwords.
    """
    with open(dictionary_file, 'r') as file:
        for word in file:
            word = word.strip()  # Remove any trailing spaces or newline characters
            if hash_password(word) == hashed_password:
                return word  # Password found
    return None  # Password not found

# Example usage
if __name__ == "__main__":
    # Target password hash (for demonstration, the password is "secret")
    target_password = "secret"
    hashed_password = hash_password(target_password)

    # File containing potential passwords
    dictionary_file = "passwords.txt"

    # Perform dictionary attack
    cracked_password = dictionary_attack(hashed_password, dictionary_file)

    if cracked_password:
        print(f"Password cracked! The password is: {cracked_password}")
    else:
        print("Password not found in the dictionary.")
```

---

### Steps to Use:
1. **Prepare a Dictionary File (`passwords.txt`)**: 
   - Create a text file named `passwords.txt` in the same directory as your script.
   - Add a list of possible passwords, one per line. For example:
     ```
     123456
     password
     secret
     admin
     ```
2. **Run the Code**:
   - The script will compute the SHA-256 hash of each password in the file and compare it to the target hash.

---

### Notes:
1. **Security**: This script is for educational purposes. Unauthorized password cracking is illegal and unethical.
2. **Hashing Algorithm**: The script uses SHA-256, but you can change it to match the hash algorithm of your target password.
3. **Optimization**: For large files or more advanced attacks, consider using multithreading or libraries like `hashcat`.

---

### Example Output:
If `passwords.txt` contains the password `secret`, the output will be:
```
Password cracked! The password is: secret
```

If the password is not in the dictionary file:
```
Password not found in the dictionary.
```
