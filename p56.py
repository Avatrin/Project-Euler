maxi = 0
import time
start = time.time()
for i in range(90,100):
    for j in range(90,100):
        ab = i**j
        sumi= sum([int(k) for k in str(ab)])
        if sumi>maxi:
            maxi = sumi
print(maxi)
end = time.time()

print(end-start)
