import random
import os

greetings = [
    "Hello, World!",
    "こんにちは、世界！",
    "Hola, Mundo!",
    "Bonjour, le monde!"
]

print(random.choice(greetings))

# 実行回数の記録
count_file = "count.txt"

# ファイルが存在していなければ初期化
if not os.path.exists(count_file):
    with open(count_file, "w") as f:
        f.write("0")

# 実行回数を読み取り、+1して保存
with open(count_file, "r") as f:
    count = int(f.read())

count += 1

with open(count_file, "w") as f:
    f.write(str(count))

print(f"Executed {count} times.")
