def is_palindrome(text):
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove all spaces and convert to lowercase for case-insensitive comparison
    cleaned_text = text.replace(" ", "").lower()
    
    # Reverse the cleaned string using slicing
    reversed_text = cleaned_text[::-1]
    
    # Compare the cleaned string with its reverse
    bot = False
    if cleaned_text == reversed_text:
        bot = True
        # return True
    else:
        bot = False
    return bot 
    # return cleaned_text == reversed_text


def main():
    """Main function to run the palindrome checker."""
    # Get input from the user
    user_input = input("Enter a string: ")
    
    # Store the cleaned version for display
    # cleaned_input = user_input.replace(" ", "").lower()
    # reversed_string = cleaned_input[::-1]
    ans = is_palindrome(user_input)    
    # Check if the input is a palindrome
    if ans:
        print(f"'{user_input}' is a palindrome")
    else:
        print(f"'{user_input}' is not a palindrome")
    
    # Display the processed strings for verification
    # print(f"Cleaned String: {cleaned_input}")
    # print(f"Reversed String: {reversed_string}")


# Entry point of the program
if __name__ == "__main__":
    main()