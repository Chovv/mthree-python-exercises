
bill = 0
while bill <= 0:
    bill = float(input("Bill amount: $"))
    if bill <= 0:
        print("Bill must be greater than zero")

tip_percent = -1
while tip_percent < 0:
    tip_percent = float(input("Tip percentage %: "))
    if tip_percent < 0:
        print("Tip percentage can't be negative")

people = 0
while people <= 0:
    people = int(input("How many people splitting? "))
    if people <= 0:
        print("Must be at least 1 person")


tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people


print("\n------- Breakdown -------")
print(f"Bill: ${bill:.2f}")
print(f"Tip ({tip_percent:.1f}%): ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
if people > 1:
    print(f"Per person: ${per_person:.2f} (split {people} ways)")