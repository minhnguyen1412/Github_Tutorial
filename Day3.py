#Basics Data Types:

'''
Các kiểu dữ liệu cơ bản trong Python: bool, None, int, float, str
'''

'''
Topic #0: bool & None
'''
# [] bool: True & False
var_bool = True

# [] type(): Dynamically typed
#print(type(var_bool))

#Numberically, they're evaluated as integers with value 1 (True), 0 (False)
a = 4 + True
#print(a)

b = False
# if b == 0:
#     print ("B is zero")

# [] None: Phần tử Không
var_none = None
# print(type(var_none))

# None is often used as a placeholder for optional or missing value.
# It evaluates as False in conditionals.
# email_address = None #False
email_address = "codex@warhammer.40k"

if email_address:
    print(f"Email address is {email_address}")
else:
    print(f"Email address is empty or {email_address}")


'''
Topic #1: Number (int & float)
'''