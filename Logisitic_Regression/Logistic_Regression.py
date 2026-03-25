import pandas as pd
import numpy
import math

df = pd.read_csv("StudentsPerformance.csv")

reading = df["reading score"]

size = int(len(reading))

train = int(size*0.70)

validate = int((size*0.15)+train)

test = int((size*0.15)+validate)

# Subtract the mean and divide by the standard deviation
reading = (df["reading score"] - df["reading score"].mean()) / df["reading score"].std()

df["writing score"] = numpy.where(df["writing score"] >= 60, 1, 0)

writing = df["writing score"]

x = reading

y = writing

x_train = x.iloc[:train].to_numpy()

y_train = y.iloc[:train].to_numpy()

slope = 1

intercept = -1

for n in range(0, 10000):

    equation_slope = (slope*x_train)+intercept

    guess = (1/(1+(numpy.e)**-equation_slope))

    error_slope = numpy.mean(x_train*(guess - y_train))+(0.0001*slope)

    error_intercept = numpy.mean(guess - y_train)

    slope-=(0.01*error_slope)

    intercept-=(0.01*error_intercept)

x_validate = x.iloc[train:validate].to_numpy()

y_validate = y.iloc[train:validate].to_numpy()

equation_slope = (slope*x_validate)+intercept

guess = (1/(1+(numpy.e)**-equation_slope))

accuracy = -(y_validate*numpy.log(guess)+(1-y_validate)*numpy.log(1-guess))

predictions = numpy.where(guess >= 0.50, 1, 0)

true_accuracy = numpy.mean(predictions == y_validate) * 100

print(f"Real Accuracy: {true_accuracy}%")

print(f"Accuracy: {numpy.mean(accuracy)}")

print(f"Slope: {slope}")

print(f"Intercept: {intercept}")

reading_score = 0.7

equation_slope = (slope*reading_score)+intercept

guess = (1/(1+(math.e)**-equation_slope))

result = ""

if(guess >= 0.50):
    result = "Pass"
else:
    result = "Fail"

print(f"If you get a reading score of {reading_score*100}%, you will {result} on your writing test")