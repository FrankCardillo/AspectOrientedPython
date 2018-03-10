#!/usr/bin/env python3

class Aspecter(object):
    # fields here

    # relationship between rules and methodNames needs to be clearer
    # Esp. for adding/removing, weaving/unweaving
    # string representations of method names
    methodNames = {}

    # some attribute of the class/object you care about and want to look out for
    typeSignifiers = {}

    # list containing registered rules
    rules = {}

    # constructor here
    def __init__(self):
        pass

    # static methods
    # @staticmethod decorator

    def addToMethodNames(self, methodObj):
        self.methodNames[methodObj.__name__] = methodObj
        # adding rules

    def removeFromMethodNames(self, name):
        del self.methodNames[name]
        # deleting rules

    def register(self, ruleName, regex="", inputObjs=(), outputObjs=(),
                 prefunc=None, postfunc=None):
        rule = {"name": ruleName, "regex":regex, "inputs":inputObjs, "outputs":outputObjs,
                "pre":prefunc, "post":postfunc}
        self.rules[ruleName] = rule

    ### pseudocode
    # def around(self, codeToAcceptOrReject, condition):
    #     if condition:
    #         codeToAcceptOrReject
    #         advice
    #     else:
    #         different advice
    #         # don't run codeToAcceptOrReject

    def isIntercepted(name):
        

