n = int(input())
k = int(input())
now = 1
before = 0
for i in range(2, n + 1):
    t = now
    now = now + before*k
    before = t

print(now)
