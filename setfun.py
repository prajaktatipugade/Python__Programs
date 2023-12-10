s1q={1,2,3,4,"prajakta"}
s2e={1,2,4,8,9}
s1q.add(4)
print(s1q)
z=s1q.difference(s2e)
print(z)
z=s1q.intersection(s2e)
print(z)
z=s1q.union(s2e)
print(z)
s2e.pop()
print(s2e)

s2e.remove(2)
print(s2e)
