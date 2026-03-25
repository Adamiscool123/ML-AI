import numpy
import random
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

reading_score = df['reading score']

english_score = df['writing score']

size = int(len(reading_score))

train = int(size*0.7)

validation = int((size*0.15)+train)

testing = int((size*0.15)+validation)

x1 = reading_score.iloc[:train].to_numpy()

y1 = english_score.iloc[:train].to_numpy()

average = 0

for i in y1:
    average+=i
    
average=average/len(y1)

slope = 0
intercept = 0

# TRAINING LOOP
for n in range(0, 100):
    # Gradient Descent Step (Using the first 100 or len(x1))
    guess = (slope * x1) + intercept
    
    # Derivatives of MSE
    error_slope = numpy.mean(-2 * x1 * (y1 - guess)) + (2 * 0.000000000001 * slope)
    error_int = numpy.mean(-2 * (y1 - guess))
    
    # Update weights
    slope -= (0.00001 * error_slope)
    intercept -= (0.00001 * error_int)

# FINAL TESTING
test_x = reading_score.iloc[validation : testing].to_numpy()
test_y = english_score.iloc[validation : testing].to_numpy()
# It's often better to calculate the average of the TEST set for R-squared
test_average = test_y.mean() 

total_sum_average = 0
model_miss = 0

guess = (slope * test_x) + intercept

total_sum_average = numpy.sum((test_y - test_average)**2)
model_miss = numpy.sum((test_y - guess)**2) + (0.000000000001 * slope**2)

accuracy = (1 - (model_miss / total_sum_average)) * 100

print(f"Final Model accuracy: {accuracy:.2f}%")

score = 100

result = slope*score+intercept

print(f"Student with a reading score of {score}% gets a writing score: {result}%")

print(f"Dumb guess {total_sum_average}")

print(f"Model miss {model_miss}")

print(f"Model accuracy: {(1-(model_miss/total_sum_average))*100}%")