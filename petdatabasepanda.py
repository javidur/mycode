import pandas as pd

pet1 = {"name" : "Bowie", "age" : 2, "species" : "dog"}
pet2 = {"name" : "Peach", "age" : 1, "species" : "cat"}
pet3 = {"name" : "Misty", "age" : 4, "species" : "cat"}
pet4 = {"name" : "Sheldon", "age" : 3, "species" : "turtle"}

pets_df = pd.DataFrame([pet1, pet2, pet3, pet4])

print(pets_df.head())

print(pets_df.info())

print(pets_df.shape)
