#!/usr/bin/env python3

class Aspecter(object):
    # fields here

    # string representations of method names
    methodNames = {}

    # some attribute of the class/object you care about and want to look out for
    typeSignifiers = {}

    # list containing registered rules
    rules = []

    # constructor here
    def __init__(self):
        pass

    # static methods
    # @staticmethod decorator

    # instance methods
    # @classmethod decorator

    @classmethod
    def addToMethodNames(self, methodObj):
        self.methodNames[methodObj.__name__] = methodObj

    @classmethod
    def removeFromMethodNames(self, name):
        del self.methodNames[name]

    @classmethod
    def register(self, regex="", inputObjs=(), outputObjs=(),
                 prefunc=None, postfunc=None):
        rule = {"regex":regex, "inputs":inputObjs, "outputs":outputObjs,
                "pre":prefunc, "post":postfunc}
        self.rules.append(rule)
