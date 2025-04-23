Project Title: How Do Lecture Days Affect My Daily Physical Activity?
Motivation
Since I began attending classes at Sabancı University, I have observed that my daily activity levels vary depending on whether I have lectures. On days with classes, I commute to campus, walk between buildings, and generally move more. This project aims to explore how my academic schedule influences my physical activity by analyzing my personal health data.

Data Source
I will use my own fitness data, collected through the Health app on my smartphone and smartwatch. The dataset includes various metrics such as active energy burned (calories), sleep activity, heart rate, and more. For this project, I will primarily focus on active energy burned as an indicator of daily activity.
The data will be exported in XML format and processed to extract relevant records. I will cross-reference these with my lecture schedule, which I extracted from the university academic portal.

Data Analysis
To investigate the relationship between lecture days and activity, I will follow these steps:

Data Collection and Cleaning
I will filter my activity data to cover the period between September 2024 and April 2025. Each date will be labeled as either a lecture day or non-lecture day based on my course schedule.

Exploratory Data Analysis (EDA)
I will use visual tools such as histograms, boxplots, and time series plots to explore how daily activity (in terms of calories burned) changes between lecture and non-lecture days.

Hypothesis Testing
To assess whether the differences are statistically significant, I will apply a t-test comparing calorie values on lecture days vs. non-lecture days.

Machine Learning
I will attempt to build a basic classifier (e.g., logistic regression or decision tree) to predict whether a day was a lecture day using only activity metrics like calorie burn.

Findings
This project will help answer the following:

Do I burn significantly more calories on days I have lectures?

Is there a clear distributional difference in daily activity between lecture and non-lecture days?

How strongly does my class schedule influence my physical movement?

Can activity data alone predict whether I had classes?

Limitations and Future Work
Limitations:
The data comes from a 2 devices and may have measurement errors. The study doesn’t currently factor in external variables like weather or exam stress.

Future Work:
I plan to expand the dataset over a longer time frame, incorporate additional activity metrics (e.g., steps, heart rate, sleep), and possibly include qualitative logs like mood or energy level for richer context.

