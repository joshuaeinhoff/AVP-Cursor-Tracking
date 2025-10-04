import pandas as pd
import json

filename = '742853_case1.json'
csvname = '742853_case1.csv'
with open(filename, 'r') as f:
    data = json.load(f)

#print(data)
df = pd.DataFrame(data, columns=["DetectionName", "x", "y", "frame"])
df.head()
pivot = df.pivot_table(
    index="frame",
    columns="DetectionName",
    values=["x", "y"],
    aggfunc=list,
)
pivot = pivot.map(lambda v: v if isinstance(v, list) else [])

pivot.columns = [f"{a}{b}" for a, b in pivot.columns]
pivot = pivot.reset_index()
mask = (
    pivot["xAvatar"].apply(lambda v: len(v) == 1) &
    pivot["yAvatar"].apply(lambda v: len(v) == 1) &
    pivot["xCursor"].apply(lambda v: len(v) == 1) &
    pivot["yCursor"].apply(lambda v: len(v) == 1)
)
clean = pivot[mask].copy()
for col in ["xAvatar", "yAvatar", "xCursor", "yCursor"]:
    clean[col] = clean[col].str[0]
clean.to_csv(csvname, index=False)
print(clean.head())
