import re


def strip_punctuation_and_lower(sentence):
    return re.sub(r'[^A-Za-z]', "", sentence).lower()

def is_palindrome(sentence):
    front = 0
    end = -1
    length = len(sentence)

    while length > 0:

        if sentence[front] != sentence[end]:
            print("That's not a palindrome.")
            return False

        else:
            front += 1
            end -= 1
            length -=2

    print("That's a palindrome.")
    return True


def main():
    user_input = input("Please give me a string and I'll see if it's a palindrome. ")
    stripped_user_input = strip_punctuation_and_lower(user_input)
    is_palindrome(stripped_user_input)

if __name__ == '__main__':
    main()
