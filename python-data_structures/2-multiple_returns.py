#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)

    length = len(sentence)

    new_sent = list(sentence)
    
    return (length, new_sent[0])
     