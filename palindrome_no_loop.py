import re


def strip_punctuation_and_lower(sentence):
    return re.sub(r'[^A-Za-z]', "", sentence).lower()

def is_palindrome(sentence):
    forward_stripped = strip_punctuation_and_lower(sentence)
    reverse_stripped = forward_stripped[::-1]

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
