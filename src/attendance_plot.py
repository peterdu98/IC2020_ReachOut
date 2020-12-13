
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

COURSE = 'COS10001'


if __name__ == '__main__':
	# Read data
	data = pd.read_csv('./data/data.csv')
	data = data[data['CourseID'] == 'COS10001']['CourseAvgAttendance'].values

	# Plot
	plt.figure(figsize=(10, 8))
	sns.distplot(data, kde=True, rug=False)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlabel("Average Attendance", fontdict={"size": 24})
	plt.ylabel("Density", fontdict={"size": 24})

	plt.show()

