"""

We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

records1 = [
  ["Paul",     "enter"],
  ["Pauline",  "exit"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Martha",   "exit"],
  ["Joe",      "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Joe",      "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Joe",      "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Joe",      "enter"],
  ["Joe",      "enter"],
  ["Martha",   "exit"],
  ["Joe",      "exit"], [Joe,]
  ["Joe",      "exit"]
]
exit. enter
Expected output: ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]

Other test cases:

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],

]

Expected output: ["Paul"], ["Paul"]

records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"],
]

Expected output: ["Raj", "Paul"], ["Paul"]

All Test Cases:
mismatches(records1) => ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]
mismatches(records2) => [], []
mismatches(records3) => ["Paul"], ["Paul"]
mismatches(records4) => ["Raj", "Paul"], ["Paul"]

n: length of the badge records array

"""
from typing import List
import collections
def logging(records: List[List[str]]) -> List[List[str]]:
    collections1, collections2 = set(), set()
    mapping = collections.defaultdict(list)
    for name, op in records:
        mapping[name].append(op)

    for name in mapping:
        prev = ''
        for action in mapping[name][::-1]:
            if (prev == '' or prev == 'enter') and action == 'enter': # enter / enter or enter / '' => collections1
                collections1.add(name)
            prev = action
        prev = ''
        for action in mapping[name]:
            if (prev == '' or prev == 'exit') and action == 'exit':  # '' / exit or exit / exit
                collections2.add(name)
            prev = action

    return [list(collections1), list(collections2)]

def logging(records: List[List[str]]) -> List[List[str]]:
    room = set()
    enter = set()
    exit = set()
    for name, type in records:
        if type == 'enter':
            if name not in  room:
                room.add(name)
            else:
                enter.add(name)
        else:
            if name not in room:
                exit.add(name)
            else:
                room.remove(name)
    enter.update(room)
    return [list(enter), list(exit)]
records1 = [
    ["Paul", "enter"],
    ["Pauline", "exit"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Martha", "exit"],
    ["Joe", "enter"],
    ["Martha", "enter"],
    ["Steve", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Joe", "enter"],
    ["Curtis", "exit"],
    ["Curtis", "enter"],
    ["Joe", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"],
    ["Joe", "enter"],
    ["Joe", "enter"],
    ["Martha", "exit"],
    ["Joe", "exit"],
    ["Joe", "exit"],
]
records2 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
]
records3 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]
records4 = [
    ["Raj", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
    ["Raj", "enter"],
]
print(logging(records3))
