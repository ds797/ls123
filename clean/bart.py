import sys
import pandas as pd

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Supply input')
		exit()
	files = sys.argv[1:]
	for input_file in files:
		input_file = input_file[:-4]
		df = pd.read_csv(input_file + '.csv', skiprows=1, index_col=0)
		df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
		df = df.dropna()

		labels = ['16', '24', 'BP', 'CC', 'EM', 'GP', 'MT', 'PL']
		#df = df[df['Exit Station Two-Letter Code'].isin(labels)]
		df = df.loc[labels, df.columns.isin(labels)]
		df = df.round(2)

		print(df)
		df.to_csv(input_file + '-cleaned.csv')
