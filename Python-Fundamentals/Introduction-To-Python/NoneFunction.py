# in Python, a function can return None either explicitly or implicitly.
#A simple example of a function that returns None explicitly:


def checkPositiveNumber(number):
    if number > 0:
        return number
    else:
        return None

result = checkPositiveNumber(-5)
print(result)

#implicit

def checkNumber(number):
    if number > 0:
        return number+1
    if number<0:
        return number-1

result = checkNumber(0)
print(result)
