import pandas as pd


df = pd.read_json("tasks.json")


print("===== DATASET =====")
print(df)

print("\n===== FIRST ROWS =====")
print(df.head())

print("\n===== NUMBER OF TASKS =====")
print(len(df))

print("\n===== COLUMNS =====")
print(df.columns)

print("\n===== INFORMATION =====")
print(df.info())