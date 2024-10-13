#passing function as argument

def getValue(function, value):
    return function(value)

result = getValue(lambda x: x*2,10)
print (result)
    
