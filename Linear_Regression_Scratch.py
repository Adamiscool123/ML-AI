import numpy
import random
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

math_score = df['math score']

english_score = df['reading score']

average = 0

x = math_score

y = english_score

for i in y:
    average+=1

average = average/2


slope = 0
intercept = 0

for i in range(0, 100):

    for i in range(0, 100):

        guess = slope*x[i]+intercept

        error1 = 2*(y[i]-guess)*-x[i]

        error2 = 2*(y[i]-guess)*-1
        
        slope-=(0.0000001*error1)

        intercept-=(0.0000001*error2)

    print(f"Slope: {slope}")

    print(f"Intercept: {intercept}")

    score = 100

    result = slope*score+intercept

    print(f"Student with a math score of {score}% gets a reading score: {result}%")

    print("\n")






