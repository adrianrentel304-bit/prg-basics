import time

seconds = int(input("Enter seconds for countdown: "))

while seconds > 0:
    if seconds <= 5:
        words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}
        print(words[seconds])
    else:
        print(seconds)
    time.sleep(1)
    seconds -= 1
print("Time's up!")