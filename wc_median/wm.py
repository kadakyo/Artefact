import numpy as np

if __name__ == '__main__':
	with open('tempFile.txt', 'r') as f:
		text = f.read()
	text = text.split('\n')

	while True:
		try:
			text.remove('')
		except ValueError:
			break

	result = []
	res = map(lambda x: int(x), text)
	for x, y in enumerate(res):
		result.append(str(np.median(res[:x + 1])))
	result = '\n'.join(result)

	with open('med_result.txt', 'w') as f:
		f.write(result)