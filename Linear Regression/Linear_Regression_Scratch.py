import numpy
import random
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

math_score = df['reading score']

english_score = df['writing score']

x = math_score

y = english_score

average = 0

for i in y:
    average+=i
    
average=average/len(y)

slope = 0
intercept = 0

for n in range(0, 100):
    
    total_sum_average = 0

    model_miss = 0

    for i in range(0, 100):

        guess = slope*x[i]+intercept
        
        total_sum_average+=(y[i]-average)**2
        
        model_miss+=(y[i]-guess)**2

        error1 = 2*(y[i]-guess)*-x[i]

        error2 = 2*(y[i]-guess)*-1
        
        slope-=(0.0000001*error1)

        intercept-=(0.0000001*error2)
        
    if(n == 99):

        print(f"Slope: {slope}")

        print(f"Intercept: {intercept}")

        score = 100

        result = slope*score+intercept

        print(f"Student with a reading score of {score}% gets a writing score: {result}%")
        
        print(f"Dumb guess {total_sum_average}")
        
        print(f"Model miss {model_miss}")
        
        print(f"Model accuracy: {(1-(model_miss/total_sum_average))*100}%")

        print("\n")