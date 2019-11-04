from collections import Counter
import pandas as pd

if __name__ == '__main__':
	with open('tempFile.txt', 'r') as f:
		text = f.read()
	res = Counter(text.lower().split(' '))
	res.pop('')
	pd.Series(res).to_csv('wc_result.txt', sep='\t', header=False)