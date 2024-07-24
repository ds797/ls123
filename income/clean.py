import sys
import pandas as pd

if __name__ == '__main__':
	for file in sys.argv[1:]:
		print('\nAnalyzing', file, '...')
		df = pd.read_csv(file, skiprows=1)
		df = df.rename(columns={'Geographic Area Name': 'City', 'Estimate!!Households!!Mean income (dollars)': 'Mean Income'})
		df = df.loc[:, ['City', 'Mean Income']]

		print(df[df['City'] == 'San Francisco city, California'])
