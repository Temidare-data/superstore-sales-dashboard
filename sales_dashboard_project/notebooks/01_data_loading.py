import pandas as pd

# Load the dataset
df = pd.read_csv('data/superstore.csv', encoding='latin1')

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumns:", df.columns.tolist())