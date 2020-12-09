
# Input from line-broken text to list of numbers
f = open("input_09.txt", 'r')
l = f.read().split('\n')
f.close()
a = list(map(int, l))


# O(x^2) where x is the size of look-back, 25*25=625, basically inconsequential. No need to be fancy, just look-back naively.

for i in range (25, len(a)):
    if a[i] in [x+y for x in a[i-25:i] for y in a[i-25:i] if x is not y]:
        pass #this is ok
    else:
        print("Number {} at index {} is not a sum of previous 25 numbers.".format(a[i], i))
        break

