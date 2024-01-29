def is_valid_parentheses(s: str) -> bool:
    li = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in brackets:
            if not li or li.pop() != brackets[char]:
                return False
        else:
            li.append(char)
    return not li
    
s=input("Enter parenthesis string")
if is_valid_parentheses(s):
    print("Valid")
else:
    print("Invalid")
 