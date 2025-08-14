def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")  # Optional: ignore case and spaces
    return cleaned_text == cleaned_text[::-1]

# Example usage
ipstring = input('Enter a string: ')
if is_palindrome(ipstring):
    print(f"'{ipstring}' is a palindrome.")
else:
    print(f"'{ipstring}' is not a palindrome.")
'''op
Enter a string: palindrome
'palindrome' is not a palindrome.'''
