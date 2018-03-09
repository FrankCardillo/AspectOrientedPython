#!/usr/bin/env python3

class Aspecter(object):
    # fields here

    # string representations of method names
    methodNames = {}

    # some attribute of the class/object you care about and want to look out for
    typeSignifiers = {}

    # constructor here

    # static methods
    # @staticmethod decorator

    # instance methods

    # add to and remove from methodNames methods

    def addToMethodNames(self, methodObj):
        self.methodNames[methodObj.__name__] = methodObj

    def removeFromMethodNames(self, name):
        del self.methodNames[name]