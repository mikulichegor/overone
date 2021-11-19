'''
Function to check if word is a palindrome.
Example:
    is_palindrome('abcba') returns True
    is_palindrome('abcd') returns False
Note:
    - spaces before and after word are removed
'''
def is_palindrome(word: str) -> bool:
    return word.strip() == word.strip()[::-1]


