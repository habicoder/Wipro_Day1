pcnt = 0
ncnt = 0
psum = 0
nsum = 0

while True:
        a = int(input("Enter an integer (0 to quit): "))
        
        if a != 0:
            if a > 0:
                pcnt += 1
                psum += a
            else:
                ncnt += 1
                nsum += a
        else:
            break

print("Positive count  =", pcnt)
print("Negative count  =", ncnt)
print("Positive sum    =", psum)
print("Negative sum    =", nsum)