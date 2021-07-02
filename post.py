w = [5,4,8,2,6,9,1,2,4,6,8]
k = 4

n = len(w)
t = k*[0]
w.sort(reverse=True)
for wi in w:
    ind = t.index(min(t))
    t[ind] += wi
print(w)
print(t)
print(max(t))