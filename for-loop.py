# Iterate over a list
students = ["Ronwald", "Michaella", "Lorein", "Denmark"]
for student in students:
    print(student)

print("================================")
# using range() to generate numbers
for i in range(5):
    print(i)

print("")
for i in range(2, 9):
    print(i)
print(" ")
for i in range(2, 10, 2):
    print(i)

print("====================================")
# Iterate over string
for char in "Hello World":
    print(char)

print("====================================")
# With indec using enumerate()
for index, student in enumerate(students):
    print(f"{index}:{student}")

print("===============================================")
print(" ")
print(" While LOOP")
print("    Repeats while condition is TRUE ")

print(" Example")

print("Counting up")

num = 0

while num <= 10:
    print(num)
    num += 1

print("User input validation")
print(" ")
age = int(input("Enter Your Age(must be positibe): "))
while age <= 0:
    print("Invalid! Must Be Positive. ")
    age = int(input("Enter your age"))
print(f"you are {age} years old")

passcode = int(input("Enter Passcode(number only!: "))
while passcode != 143:
    print("wrong passcode.")
    passcode = int(input("Try again: "))
print("Welcome!")


print("===============================================")
print("Loop Control Statement")
print("     break : Exits Loops immediately")
print("     continue : Skips the rest of the current  iteration and go to the next ")
print(
    "     else : runs when the loop finishes all iterations (not interrupted by - break -"
)
print(" ")
print("Example")
print(" ")
print("break")
for i in range(10):
    if i == 5:
        break
    print(i)
