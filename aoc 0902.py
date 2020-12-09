magicnumber = REDACTED

# Input from line-broken text to list of numbers
f = open("input_09.txt", 'r')
l = f.read().split('\n')
f.close()
a = list(map(int, l))


# Subsequence sum basics: creating a second array of sums, like
# ssarray = [sum(a[0:1]), sum(a[0:2]), sum(a[0:3]) ... ]
# lets us create any subsequence sum just by subtracting two numbers,
# e.g. the sum of all elements from element 32 to element 553 is just ssarray[553] - ssarray[32].

# Create ssarray:
ssarray = []
summa = 0
for i in range(len(a)):
    summa = summa + a[i]
    ssarray.append( summa )

# To find our exact number from answer 1, a naive search is enough, O(n^2) ~ 1 mio operations.

target_start, target_stop = 0, 0
for i in range(len(a)):
    for j in range(i): # the subsequence must be at least 2 numbers long
        #print("{}:{}".format(j,i))
        if ssarray[i] - ssarray[j] == magicnumber:
            target_start = j
            target_stop = i
            print("hi")
            break
    else:
        continue # continue if the inner loop completed
    break # breaks if the inner loop broke

smol = min(a[target_start:target_stop])
lorg = max(a[target_start:target_stop])

print("Answer is {} from {}+{} in range \[{}, {}\)".format(smol+lorg, smol, lorg, target_start, target_stop))