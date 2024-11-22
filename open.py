To run the provided OpenSSL commands, you do not need to write them in code (such as Python or Java). These commands are executed directly in the terminal or command line interface. Here’s how to run them:

### Steps to Execute the OpenSSL Commands:

1. **Install OpenSSL:**
   Ensure that OpenSSL is installed on your system. You can check this by running the following command in your terminal:
   
   ```bash
   openssl version
   ```

   If OpenSSL is not installed, you can install it using the following methods:

   - **On Windows**: Download and install OpenSSL from [https://slproweb.com/products/Win32OpenSSL.html](https://slproweb.com/products/Win32OpenSSL.html) or use a package manager like `Chocolatey`.
   - **On Linux**: Install it using the package manager, e.g. for Ubuntu:
     ```bash
     sudo apt-get install openssl
     ```
   - **On macOS**: Install it using Homebrew:
     ```bash
     brew install openssl
     ```

2. **Run Commands in Terminal/Command Prompt:**
   Open your **command prompt** (on Windows) or **terminal** (on Linux/macOS), and execute the following steps one by one. Here’s a breakdown of the commands and how to run them:

### Command Breakdown and Execution

#### **Step 1: Create a Plaintext File**
   - Create a file called `plain.txt` with your name and registration number:
     ```bash
     echo "YourName RegNo" > plain.txt
     ```

#### **Step 2: AES Encryption**
   - Encrypt the file using AES-128-CBC:
     ```bash
     openssl aes-128-cbc -e -in plain.txt -out cipher.bin -k "password" -nosalt
     ```

   - **Display the encrypted file** (in hexadecimal format):
     ```bash
     xxd cipher.bin
     ```

#### **Step 3: AES Decryption**
   - Decrypt the file:
     ```bash
     openssl aes-128-cbc -d -in cipher.bin -out pt.txt -k "password" -nosalt
     ```

   - **Display the decrypted content**:
     ```bash
     cat pt.txt
     ```

#### **Step 4: RSA Key Generation**
   - Generate an RSA private key:
     ```bash
     openssl genrsa -out pvtkey.pem
     ```

   - Generate an RSA public key from the private key:
     ```bash
     openssl rsa -pubout -in pvtkey.pem -out pubkey.pem
     ```

   - Display the private key in hexadecimal format:
     ```bash
     openssl rsa -text -in pvtkey.pem
     ```

#### **Step 5: RSA Encryption**
   - Encrypt the `plain.txt` file using the RSA public key:
     ```bash
     openssl rsautl -encrypt -in plain.txt -pubin -inkey pubkey.pem -out c1.bin
     ```

   - **Display the encrypted content**:
     ```bash
     xxd c1.bin
     ```

#### **Step 6: RSA Decryption**
   - Decrypt the RSA-encrypted file using the private key:
     ```bash
     openssl rsautl -decrypt -in c1.bin -inkey pvtkey.pem -out dec1.txt
     ```

   - **Display the decrypted file**:
     ```bash
     cat dec1.txt
     ```

#### **Step 7: Generate MD5 and SHA256 Hashes**
   - Generate an MD5 hash of `plain.txt`:
     ```bash
     openssl md5 plain.txt
     ```

   - Generate a SHA256 hash of `plain.txt`:
     ```bash
     openssl sha256 plain.txt
     ```

#### **Step 8: Digital Signature**
   - Generate a digital signature using SHA-1 and RSA:
     ```bash
     openssl dgst -sha1 -sign pvtkey.pem -out s.bin plain.txt
     ```

   - Verify the signature using the public key:
     ```bash
     openssl dgst -sha1 -verify pubkey.pem -signature s.bin plain.txt
     ```

---

### Important Notes:
- **No Imports**: Unlike programming languages like Python, Java, or C, the OpenSSL commands are executed directly in the terminal. There is no need for imports or setting up a script.
- **Password for Encryption**: In the commands where AES encryption is involved (`-k "password"`), replace `"password"` with your own passphrase for encryption.
- **Permissions**: Ensure you have the appropriate permissions to read/write files on your system, especially when creating, encrypting, or decrypting files.
- **File Paths**: If your files are located in different directories, ensure to specify the correct file paths when running the commands.

Let me know if you need further details!
