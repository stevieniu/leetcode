state = 0b110
subset = state

while subset:
    print(subset, bin(subset))
    subset = (subset - 1) & state
    