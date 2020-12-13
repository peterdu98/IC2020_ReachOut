# ReachOut app

ReachOut is a mobile/tablet app aiming to identify students who are suffering from the mental illness for offering supports from their teachers. Within 24 hours of the Image Cup Hackathon - Australia, we (a team of 4 members) offer the minimal and user-friendly design with simple and lighweight achitecture powered by Azure for the app.

## Our goal

We offer the solution for helping either teachers or social workers to connect with students who are suffering from their mental illness during the pandmic period.

## How can we do that?

1. We use average grade and attendence rate with number of enroled units per student to analyse whether a particular student is suffering from mental issues.
2. With that information, we let the instruction provider know list of those students and their basic information for the direct connection. 

## Project Showcase

<p float="left" align="center">
  <img src="https://github.com/peterdu98/IC2020_ReachOut/blob/main/screenshots/Dashboard.png" width="250" />
  <img src="https://github.com/peterdu98/IC2020_ReachOut/blob/main/screenshots/Students.png" width="250" />
  <img src="https://github.com/peterdu98/IC2020_ReachOut/blob/main/screenshots/Student.png" width="250" />
</p>

## Presentation

The architect solution is hosted at [Vimeo](https://vimeo.com/490302037)


## Suggestion for TechStack

1. Azure Load Balancer for controlling bandwith of the server
2. Azure SQL for storing data and getting data
3. Azure Pipeline with Github for maintaining versions of the app
4. Flask should be used for the backend API
5. Azure PowerApp or ReactNative should be used for the frontend of the app

## Future suggestion

1. Reach can integrate with Canvas for improving student engagement during the studying period.
2. The app is also able to have an open feature connecting social workers with students.
3. Importantly, a private chat room should be implemented to improve the interaction between teacher and students

## Conclusion

Overall, we believe that our app will truly improve the quality of education with a uniquely student centralised approach. We believe that ReachOut will be a great assistance for instruction providers who want to help their students and students who are in need of support.

## How to run our Python data generation?

```
# Installation
git clone https://github.com/peterdu98/IC2020_ReachOut.git
pip install requirements.txt

# Data generation
python generate_data.py
python model.py

# Plotting (note that the data needs to be generated first)
python attendance_plot.py
python units_plot.py
```
