import random
import os

greetings = [
    "Greetings, human.",
    "System online. Hello, World!",
    "01001000 01100101 01101100 01101100 01101111!",
    "🧠 Booting AI module... Hello!"
]

print(random.choice(greetings))

# 実行回数を記録（前と同じ）
count_file = "count.txt"
if not os.path.exists(count_file):
    with open(count_file, "w") as f:
        f.write("0")

with open(count_file, "r") as f:
    count = int(f.read())

count += 1

with open(count_file, "w") as f:
    f.write(str(count))

print(f"Execution number: {count}. All systems nominal.")
