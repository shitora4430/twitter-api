line_count = 0
with open('tweets.csv') as f:
    for line in f:
        line_count += 1

print(line_count)
