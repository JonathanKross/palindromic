import re


def strip_punctuation_and_lower(text):
    return re.sub(r'[^A-Za-z]', "", text).lower()

def reverse_string(text):
    if len(text) == 0:
         return ''
    return reverse_string(text[1:]) + text[0]

def is_palindrome(text):
    forward_stripped = strip_punctuation_and_lower(text)
    reverse_stripped = strip_punctuation_and_lower(reverse_string(text))

    if forward_stripped == reverse_stripped:
        print("That's a palindrome.")
        return True

    elif forward_stripped != reverse_stripped:
        print("That's not a palindrome.")
        return False

def main():
    user_input = input("Please give me a string and I'll see if it's a palindrome. ")
    stripped_user_input = strip_punctuation_and_lower(user_input)
    is_palindrome(stripped_user_input)

if __name__ == '__main__':
    main()
