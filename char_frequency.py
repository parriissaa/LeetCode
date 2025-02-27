def get_char_frequency(input_string):
    # Create an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Update frequency count in dictionary
        # If character exists, increment count, else set to 1
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    return frequency_dict

# Example usage
if __name__ == "__main__":
    # Get input from user
    text = input("Enter a string: ")
    
    # Get character frequencies
    result = get_char_frequency(text)
    
    # Print the character-frequency pairs
    print("\nCharacter frequencies:")
    for char, freq in result.items():
        print(f"'{char}': {freq}") 