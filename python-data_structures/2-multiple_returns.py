#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    new_sent = list(sentence)


    if sentence == "":
        return None
    else:
        print("Length: {:d} - First character: {}".format(length, new_sent[0]))
    