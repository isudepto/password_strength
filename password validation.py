def strength(user):
    result = {}
    
    if len(user) >= 8:
        result["length"] = True
    else:
        result["length"] = False
    
    digit = False
    uppercase = False
    special_char = False
    
    for i in user:
        if i.isupper():
            uppercase = True
        if i.isdigit():
            digit = True
        if not i.isalnum():
            special_char = True
    
    result["digit"] = digit
    result["uppercase"] = uppercase
    result["special_char"] = special_char
    
    if all(result.values()):
        return "strong password"
    else:
        return "weak password"

user_input = input("Enter the password: ")
valid = strength(user_input)
print(valid)
