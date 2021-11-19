'''
Function returns number of credit card where only 4 last characters are visible.
Example:
    credit_card('1234 5678 9012 3456') returns '**** **** **** 3456'
    credit_card('12342 567 9012 3423856') returns -1
Note:
    - length of credit card number must be 16 characters otherwise returns -1
'''

def credit_card(number: str) -> str:
    buf = number.replace(' ', '')
    return -1 if len(buf) != 16 else '{0} {0} {0} {1}'.format('****',buf[12:])
