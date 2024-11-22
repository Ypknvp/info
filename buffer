from array import array

def simulate_buffer_overflow():
    buffer_size = 10  # Fixed-size buffer
    buffer = array('u', ' ' * buffer_size)  # Unicode character array with fixed size

    user_input = input("Enter a string (simulate overflow): ")
    try:
        # Write user input into the buffer without bounds checking
        for i in range(len(user_input)):
            buffer[i] = user_input[i]
        print("Buffer content:", buffer.tounicode())
    except IndexError:
        print("\nBuffer overflow detected! Input exceeded buffer size.")

if __name__ == "__main__":
    simulate_buffer_overflow()
python buffer_simulation.py
