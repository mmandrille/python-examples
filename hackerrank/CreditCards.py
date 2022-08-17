'''
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
'''

import re
# Globals
CreditCards = [
    "4253625879615786",
    "4424424424442444",
    "5122-2368-7954-3214",
    "42536258796157867", #17 digits in card number → Invalid 
    "4424444424442444", #Consecutive digits are repeating 4 or more times → Invalid
    "5122-2368-7954 - 3214", #Separators other than '-' are used → Invalid
    "44244x4424442444", #Contains non digit characters → Invalid
    "0525362587961578", #Doesn't start with 4, 5 or 6 → Invalid
]

# Compile Regular expression only once:
cred_controller = re.compile("^[456]\d{3}(-)?\d{4}(-)?\d{4}(-)?\d{4}$")
no_repeat = r"(\d)\1\1\1"

def valid_credit_card(cred_number):
    if cred_controller.match(cred_number):
        if not re.search(no_repeat, cred_number.replace("-", "")):
            return True

# Run!
if __name__ == '__main__':
    # Get Cards:
    for cc in CreditCards:
        if valid_credit_card(cc):
            print("Valid")
        else:
            print("Invalid")