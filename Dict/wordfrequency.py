ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

d = {}

words = ss.split()

for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 0

print(d)