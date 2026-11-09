import pandas as pd
import random

random.seed(42)

data = []

for i in range(300):
    files_changed = random.randint(1, 20)
    lines_changed = random.randint(10, 600)
    tests_touched = random.randint(0, 15)
    hour = random.randint(0, 23)

    failed = 0

    if files_changed > 12 and tests_touched < 3:
        failed = 1
    elif lines_changed > 450 and tests_touched == 0:
        failed = 1
    elif random.random() < 0.15:
        failed = 1

    data.append([
        files_changed,
        lines_changed,
        tests_touched,
        hour,
        failed
    ])

df = pd.DataFrame(data, columns=[
    "files_changed",
    "lines_changed",
    "tests_touched",
    "hour",
    "failed"
])

df.to_csv("ml/builds.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("Total records:", len(df))