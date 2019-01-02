# # define a function isPalindrome which takes a string as input and returns True if it is a
# # palindrome and false if it is not a palindrome

# for e.g 
# isPalindrome("naman")  ---  True
# isPalindrome("horse")  ---  False

######## SOLUTION 1#####################
def is_Palindrome(str):
    reverse_str = str[::-1]
    if str==reverse_str:
        return True
    else:
        return False


def is_Palindrome2(str):
    reverse_str = str[::-1]
    if str==reverse_str:
        return True
    return False

def is_Palindrome3(str):
    return str == str[::-1]
    

input_string  = input("Please enter a string :- ").strip().lower()
print(is_Palindrome(input_string))
print(f"function 2 : --- {is_Palindrome2(input_string)}")
print(f"function 3 : --- {is_Palindrome3(input_string)}")


