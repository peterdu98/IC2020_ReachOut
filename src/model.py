
import pandas as pd
import numpy as np

MESSAGES 		= {
	'low_avg_attend': 'This student currently has low attendance rate compared to other students.',
	'low_grade': 'This student has a lower grade compared to his/her average of previous units.',
	'few_unit_low_attend': 'This student does not have many units this semester, but he/she still has low attendance on average.',
	'high_attend_low_grade': 'This student might be overloaded with many units.'
}
COURSES 			= ['COS10001', 'STA10001', 'STA20001', 'STA30001']
FREQ_THRESHOLD 		= 0.7
UNITS_THRESHOLD 	= 2

# Input	 -> Student data
# Output -> StudentID - CourseID - Comments


if __name__ == '__main__':
	data = pd.read_csv('./data/data.csv')

	# Get average attendance for each course
	course_info = dict()
	for course in COURSES:
		avg_attend = data[data['CourseID'] == course]['CourseAvgAttendance'].mean()
		course_info[course] = { 'avg_attend': avg_attend }

	result = []
	for student_id in data['StudentID'].unique():
		student = data[data['StudentID'] == student_id]
		for row in student[['CourseID', 'AvgAttendance', 'AvgGrade', 'CourseAvgAttendance', 'Grade', 'NumCurUnits']].values:
			comments = []
			course_id, avg_attend, avg_grade, course_avg_attend, grade, num_courses = row

			if avg_grade < grade:
				comments.append(MESSAGES['low_grade'])
			
			if course_avg_attend < course_info[course_id]['avg_attend']:
				if num_courses < UNITS_THRESHOLD:
					comments.append(MESSAGES['few_unit_low_attend'])
				else:
					comments.append(MESSAGES['low_avg_attend'])

			if num_courses > UNITS_THRESHOLD and course_avg_attend > FREQ_THRESHOLD and avg_grade < grade:
				comments.append(MESSAGES['high_attend_low_grade'])

			result.append((student_id, course_id, "\n".join(comments)))

	result = pd.DataFrame(result, columns=['StudentID', 'CourseID', 'comments'])
	result.to_csv('./data/comments.csv')




