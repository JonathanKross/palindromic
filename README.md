# palindrome
## Objectives
After completing this assignment, you should...

- Understand how to manipulate strings
- Understand how strings are related to lists
- Understand recursion
- Be able to strip characters out of strings
- Be able to change the case of strings
- Be able to look at substrings
- Be able to add, commit, and push to GitHub

##Deliverables
- A GitHub repo named palindromic containing at least:
  - A README.md file with a good description of the problem being solved.
  - A Python file named palindrome.py that contains your implementation.
  - A Python file named palindrome_test.py that contains the provided tests.
After your work is complete, make sure to git push your changes up to GitHub. It's a good habit to do this more than once along the way as you're making progress.

Use the homework submission form on the course website to turn in a link to your GitHub repository.

## Normal Mode
Your goal for tonight is to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not by printing "is a palindrome" or "is not a palindrome" in the output.

Letter casing and punctuation do not matter when testing a palindrome. All of the following are valid palindromes:

- stunt nuts
- Lisa Bonet ate no basil.
- A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!
- Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.

### Requirements
- Write your main() function to ask the user for a word/sentence, pass it into the is_palindrome function, and state whether or not the the sentence is palindromic.
- Write your is_palindrome function using recursion.
- Your program must pass all of the tests provided in palindrome_test.py. You should be able to run this with python palindrome_test.py.
- You need a function named is_palindrome that takes a string and returns a boolean (True or False). Your program must use this function.

### Advanced Mode (optional)
- Complete all of the requirements of Normal Mode.
- Make an iterative version of your is_palindrome function (using loops instead of recursion), and ensure it passes the tests too.

###Epic Mode (optional)
Instead of taking the user's input using input(), use Python to read a text file containing multiple lines of text as input.
Use the is_palindrome function to determine if each line is a palindrome, and print output for each individual line that says whether or not it is a palindrome.
Allow the user to provide the name of the text file using command line arguments. For example, instead of running python3 palindrome.py the user would run python3 palindrome.py palindromes.txt to read the file named palindromes.txt. This allows the program to read many different files of potential palindromes.

## Notes
You may want to use the re.sub function to strip out punctuation and spaces. A regular expression pattern you can use to match all non-alphabetical characters is r'[^A-Za-z]'.

