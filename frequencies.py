"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newList = []
    for item in items:
        newList.append(str(item))
    for item in newList:
        frequencies[item] = newList.count(item)
    return frequencies
