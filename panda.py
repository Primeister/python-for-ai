import pandas as pd

data = {
    "names": ["Prime", "Rick", "Carl"],
    "ages": [23, 45, 13]
}

df = pd.DataFrame({
    "name": data["names"],
    "age": data["ages"]
})

print(df)