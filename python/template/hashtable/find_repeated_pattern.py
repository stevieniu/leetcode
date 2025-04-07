memo = {}
memo['00'] = 99
memo['01'] = 98
memo['10'] = 97
memo['11'] = 96

# when n keep decreasing, and the pattern keep changing, what would be the samllest n for each pattern?

# after 96, next n is 95
n = 95
pattern = '10'
n = n % (memo[pattern] - n)
