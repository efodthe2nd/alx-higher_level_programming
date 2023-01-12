#!/usr/bin/python3
combsi =[]
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combsi.append((x, y))

print(combsi)
combs =[]
combs = [y for r in combsi for y in r]
print(combs)
i = len(combs) - 1
while i > 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(combs[j], combs[j + 1]))
        if combs[j] > combs[j + 1]:
            print("Switch")
            temp = combs[j]
            combs[j] = combs[j + 1]
            combs[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        for k in combs:
            print(k, end="")
        print()

    print("END OF ROUND")
    i -= 1

for k in combs:
    print(k, end=", ")

print()
