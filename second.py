import pandas as pd

# Create sample data
data = {
    "Product Name": ["Product A", "Product B", "Product C", "Product D"],
    "Price": [500, 1200, 800, 300],
    "Discount": [60, 5, 30, 8],
    "Rating": [4.5, 2.5, 3.8, 2.0]
}

df = pd.DataFrame(data)
print(df)
