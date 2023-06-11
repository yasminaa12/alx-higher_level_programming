#!/usr/bin/python3
def multiple_returns(sentence):
    mytuple = ()
    if len(sentence) == 0:
        mytuple = 0, "None"
    else:
        mytuple = len(sentence), sentence[0]
    return mytuple
