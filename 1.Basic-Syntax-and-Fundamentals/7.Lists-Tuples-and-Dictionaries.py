fruits = ["Banana", "Cherry", "Apple"]
appleVar = "Apple"
fruits.append("Orange")
print(fruits)
print(fruits[0])
print(fruits[-1])

for i in range(len(fruits)):
    if appleVar == fruits[i]:
        print(f"Found: {fruits[i]} in index {[i]}")
        break
    else:
        print(fruits[i])
