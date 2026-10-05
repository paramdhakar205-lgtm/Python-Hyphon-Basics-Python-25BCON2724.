num = int(input("Enter a number: "))

is_pronic = False

for i in range(num + 1):
    if i * (i + 1) == num:
        is_pronic = True
        break

if is_pronic:
    print("Pronic Number")
else:
    print("Not a Pronic Number")