#!/usr/bin/python3
mul = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = mul(sentence)
print("length: {:d} - First character: {}".format(length, first))
