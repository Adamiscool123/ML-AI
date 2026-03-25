import numpy
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

math = df["math score"]
reading = df["reading score"]
writing = df["writing score"]

x1 = math

x2 = reading

y = writing

math_slope = 0

reading_slope = 0

intercept = 0

size = int(len(writing))

training = int(size*0.70)

validation = int((size*0.15)+training)

test = int((size*0.15)+validation)

average = 0

for i in y:
    average+=i

average = average/int(len(y))

for n in range(0, 100):
    for i in range(training):
        guess = ((math_slope*x1[i])+(reading_slope*x2[i]))+intercept

        error_math_slope = -2*x1[i]*(y[i]-guess)

        error_reading_slope = -2*x2[i]*(y[i]-guess)

        error_intercept = -2*(y[i]-guess)

        math_slope-=(0.00001*error_math_slope)

        reading_slope-=(0.00001*error_reading_slope)

        intercept-=(0.00001*error_intercept)

x1_training = math.iloc[training : validation]

x2_training = reading.iloc[training : validation]

y1_training = writing.iloc[training : validation]

total_sum_average = 0

miss = 0

for i in range(training, validation):
    guess = ((math_slope*x1_training[i])+(reading_slope*x2_training[i]))+intercept

    total_sum_average+=(y[i]-average)**2

    miss+=(y[i]-guess)**2

accuracy = (1 - (miss / total_sum_average)) * 100

print(f"Final Model accuracy: {accuracy:.2f}%")

math_score = 100

reading_score = 80

result = ((math_slope*math_score)+(reading_slope*reading_score))+intercept

print(f"Student with a reading score of {reading_score}% and a math score of {math_score}% gets a writing score: {result}%")

print(f"Dumb guess {total_sum_average}")

print(f"Model miss {miss}")

print(f"Model accuracy: {(1-(miss/total_sum_average))*100}%")