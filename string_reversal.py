def reverse_string(input_string):
    # Return the reversed string using string slicing
    return input_string[::-1]

# Example usage
if __name__ == "__main__":
    # Get input from user
    text = input("Enter a string: ")
    
    # Get reversed string
    result = reverse_string(text)
    
    # Print the original and reversed string
    print(f"\nOriginal string: {text}")
    print(f"Reversed string: {result}") 