from functools import wraps


def sample_decorator1(func):
    def inner_func(*args, **kwargs):
        print(">>>>>")
        ret = func(*args, **kwargs)
        print("<<<<<")
        return ret
    return inner_func


def sample_decorator2(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        print(">>>>>")
        ret = func(*args, **kwargs)
        print("<<<<<")
        return ret
    return inner_func


@sample_decorator1
def myFunc1(text):
    print("now start myFunc1")
    return text


@sample_decorator2
def myFunc2(text):
    print("Now start myFunc2")
    return text


print(myFunc1("Hey!"))
print(myFunc2("Hey!"))


class Decoration:
    def __init__(self):
        pass

    @sample_decorator1
    def func1(self):
        print("This is Decoration.func1()")

    def decorator1(func):
        def inner_func(*args, **kwargs):
            print(">>>>>")
            ret = func(*args, **kwargs)
            print("<<<<<")
            return ret
        return inner_func

    @decorator1
    def func2(self, *args, **kwargs):
        print("This is Decoration.func2()")


decoration = Decoration()
decoration.func1()
decoration.func2()
