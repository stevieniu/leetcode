state = 0b111
subsets = state
print(bin(subsets))
while subsets:
    subsets = (subsets - 1) & state
    print(bin(subsets))