# Add and remove elements in the tuple
t=(12,22,24,55,78,90,99)
print(t)
ll=list(t)
ll.append(100)
ll.remove(22)
t=tuple(ll)
print(t)
