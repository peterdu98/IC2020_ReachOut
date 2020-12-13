import csv
import random
import ast


COURSES = ['COS10001', 'STA10001', 'STA20001', 'STA30001']
NAMES 	= ['William', 'James', 'Harper', 'Mason', 'Evelyn', 'Ella', 'Jackson', 'Avery', 'Jack', 'Scarlett', 'Madison', 'Eleanor', 'Wyatt']
MONTHS 	= [(3, 6), (9, 12), (15, 18)]

if __name__ == '__main__':
	
	with open('./data/data.csv', 'w', newline='') as csvfile:
		csv_writer = csv.writer(csvfile)

		header = ['StudentID', 'CourseID', 'FirstName', 'LastName', 'Email', 'Phone', 'CurrentYear', 'AvgAttendance', 'AvgGrade', 'CourseAvgAttendance', 'Grade', 'NumCurUnits']
		csv_writer.writerow(header)

		for student_id in range(50):
			# FirstName
			fname = NAMES[random.randint(0, len(NAMES) - 1)]

			# LastName
			lname = fname
			while lname == fname:
				lname = NAMES[random.randint(0, len(NAMES) - 1)]

			# Email (lowercase + @student.uni.edu.au)
			email = '{}{}@student.uni.edu.au'.format(fname.lower(), lname.lower())

			# Phone (04 + random 7 digits)
			phone = '04'
			for _ in range(7):
				phone += str(random.randint(0, 9))

			# CurrentYear (random from 1-3)
			year = random.randint(1, 3)

			# AvgAttendance
			max_attend = random.choice(MONTHS[year - 1]) * 4
			avg_attend = round(random.randint(max_attend // 4, max_attend) / max_attend, 2)

			# AvgGrade (random from 50 - 100)
			avg_grade = round(random.uniform(50, 100), 2)

			# Concat basic info
			info = [fname, lname, email, phone, year, avg_attend, avg_grade]

			# Choose course
			num_courses = random.randint(2, 4)
			for num in range(num_courses):
				# Course ID
				course_id = COURSES[num]

				# CourseAvgAttendance
				monthly_attend = random.randint(1, 4) * 3 / 12

				# Grade (random from 50 - 100)
				grade = round(random.uniform(50, 100), 2)

				# Write to csv
				row = [student_id + 1, course_id] + info + [monthly_attend, grade, num_courses]

				csv_writer.writerow(row)


		

		

