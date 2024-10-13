#function: Block of code pefrom a specifc and well-defined task
#cons: code reuse and program device into subtsask
#2 types of function: Built-in nad user-defined

def function1():
    print("This is function1")

def function2():
    print("This is function2")

function1()
function2()


def function3():
    print("This is outer function3")
    def function4():
        print("This is inner function4")
    function4()

function3()
