num = 5
convert = 1
count = 0

for i in range(num):
    print("Interaction:", i)

while count < num:
    print("Counting: ", count)
    count += 1

# Addinf my own idea

for i in range(num):
    if i != convert:
        i += 1
    print("Interaction:", i)
    convert += 1
