
import pandas as pd
import matplotlib.pyplot as plt

COURSE = 'COS10001'

if __name__ == '__main__':
	# Read data
	data = pd.read_csv('./data/data.csv')
	data = data[data['CourseID'] == 'COS10001']['NumCurUnits'].values

	# Prepare data for plot
	x = [1, 2, 3, 4]
	height = [0, 0, 0, 0]
	for num_unit in data:
		height[num_unit - 1] += 1

	# Plot
	plt.figure(figsize=(10, 8))
	plt.bar(x, height)
	for i, v in enumerate(height):
		plt.text(x[i] - 0.04, v + 0.08, str(v), fontdict={"size": 16, "weight": "bold"})

	plt.xticks(x, fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlabel("Number of enrolled units", fontdict={"size": 24})
	plt.ylabel("Number of students", fontdict={"size": 24})
	plt.show()
