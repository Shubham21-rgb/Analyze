import json
import pandas as pd

def main():
    # Read the data
    df = pd.read_excel('data.xlsx')

    # Compute revenue
    df['revenue'] = df['units'] * df['price']

    # Drop rows with NaN values
    df.dropna(inplace=True)

    # Convert to JSON
    result = df.to_json(orient='records')

    # Write to file
    with open('result.json', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
