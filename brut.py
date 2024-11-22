from collections import Counter

# Function to decrypt Caesar cipher using brute force
def caesar_brute_force(ciphertext):
    print("\nBrute Force Decryption:")
    for key in range(1, 26):  # Try all possible shifts
        decrypted = "".join(
            chr((ord(char) - 65 - key) % 26 + 65) if char.isupper() else
            chr((ord(char) - 97 - key) % 26 + 97) if char.islower() else char
            for char in ciphertext
        )
        print(f"Key {key}: {decrypted}")

# Function to decrypt Caesar cipher using frequency analysis
def caesar_frequency_analysis(ciphertext):
    # English letter frequency in descending order
    freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    # Count letter frequency in ciphertext
    letters_only = [char.upper() for char in ciphertext if char.isalpha()]
    letter_counts = Counter(letters_only)
    most_common_letter = letter_counts.most_common(1)[0][0]  # Most frequent letter in ciphertext

    # Assume the most frequent letter corresponds to 'E' (most common in English)
    assumed_shift = (ord(most_common_letter) - ord('E')) % 26

    print("\nFrequency Analysis Decryption:")
    decrypted = "".join(
        chr((ord(char) - 65 - assumed_shift) % 26 + 65) if char.isupper() else
        chr((ord(char) - 97 - assumed_shift) % 26 + 97) if char.islower() else char
        for char in ciphertext
    )
    print(f"Assumed shift: {assumed_shift}")
    print(f"Decrypted Text: {decrypted}")

# Main function to get user input and perform decryption
def main():
    ciphertext = input("Enter the Caesar cipher text: ")

    print("\nChoose decryption method:")
    print("1. Brute Force")
    print("2. Frequency Analysis")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        caesar_brute_force(ciphertext)
    elif choice == "2":
        caesar_frequency_analysis(ciphertext)
    else:
        print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
