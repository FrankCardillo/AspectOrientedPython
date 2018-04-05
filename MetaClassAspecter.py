class MetaClassAspecter(type):
    
    # user defines a dict of methods to decorate, 
    # keys are string representations of method names, 
    # values are a list of pre-functions, post-functions, 
    # and the method with any arguments they need
    # EX: {'print': [preFunc('hello'), postFunc('goodBye'), funcToWrap(1, 2, 3)]}

    def __new__(cls, name, bases, dct):
        if dct['userDct']:
            for key in dct['userDct']:
                if dct[key]:
                    dct[key] = cls.decorate(
                        dct[key],
                        dct['userDct'][key][0],
                        dct['userDct'][key][1],
                        dct['userDct'][key][2]
                    )
                else:
                    raise Exception(f'method {key} is not in the class dict, can not decorate')
        return type.__new__(cls, name, bases, dct)

    # can decorate any class/instance methods

    def decorate(cls, funcToWrap, wrapArgs, preFunc=None, postFunc=None):
        if preFunc and callable(preFunc):
            preFunc

        retVal = funcToWrap(wrapArgs)

        if postFunc and callable(postFunc):
            postFunc

        return retVal

class Test(object):
    __metaclass__ = MetaClassAspecter

    userDct = {
            'testFunction': [
                ['I am the test function'],
                lambda self: print('Hello World'),
                lambda self: print('Goodbye World')
            ]
        }

    def testFunction(self, arg1):
        print(arg1)

if __name__ == '__main__':
    ourTest = Test()
    ourTest.testFunction('I am the test function')



# We can't define a generic decorator on the meta class hook.
# It breaks the user's ability to pass arguments to the function when calling it. 
# They would have to know the arguments ahead of time and put them in userDict.
# We'll have to define useful general decorations on the metaclass hook and
# leave the customized instrumenting to dynamic mutation implementation(s)