x=2.0
s=1.0
for k in range(10):
    s=0.5*(s+x/s)
    print(f"value at each itteration {k} is:",s)
print(s)
