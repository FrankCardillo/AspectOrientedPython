def wrapper(func, args):
    func(*args)

class MetaClassAspecter(type):
    def __new__ (cls, name, bases, dct, **aspectOptions):
        try:
            if aspectOptions['onNew']:
                wrapper(aspectOptions['aspect'], aspectOptions['arguments'])
        except AttributeError:
            print("Please be sure to add these class parameters: aspect, arguments, onInit, onNew")
        return type . __new__ ( cls , name , bases , dct )
    def __init__ (cls, name, bases, dct, **aspectOptions):
        try:
            if aspectOptions['onInit']:
                wrapper(aspectOptions['aspect'], aspectOptions['arguments'])
        except AttributeError:
            print("Please be sure to add these class parameters: aspect, arguments, onInit, onNew")
        super (MetaClassAspecter, cls).__init__(name, bases, dct)




def funTime(oneArg, twoArg, threeArg):
    print("Hello world! I have been meta thinged")
    print(oneArg)
    print(twoArg)
    print(threeArg)

class Foo(metaclass=MetaClassAspecter, aspect=funTime, arguments=["I'm the first", "I'm the second", "I'm the third"], onInit=False, onNew=True):
    def __init__(self):
        print("Foo has been initialized")


if __name__ == "__main__":
    myVar = Foo()