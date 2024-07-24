import pandas as pd
import sys

if __name__ == '__main__':
	for file in sys.argv[1:]:
		df = pd.read_csv(file, index_col=0)
		df = df.sort_index(axis=0).sort_index(axis=1)
		df.loc['Sum'] = df.sum()
		print(df)
		df.to_csv(file + '-summed.csv')
