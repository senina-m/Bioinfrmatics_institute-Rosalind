filename = "test.txt"
f = open(filename, "r")
data = f.readline().split(" ")
print(data)
f.close()
k = int(data[0])
m = int(data[1])
n = int(data[2])
t = k + n + m

print((k*(k-1)+2/3*m*(m-1)+2*k*(n+m) + n*m)/(t*(t-1)))
