#To read Json file
import json
#To create tables in dataframe
import pandas as pd

#opening Json file
#first we have created a Json file of name 'assignments'
file = open('assignments.json',)

#loading file
data = json.load(file)
data

#creating dataframe table of json file
df = pd.DataFrame(data)
df

#function to calculate BMI
def bmi(a,b):
    return b/((a/100)**2)

#calculating and adding BMI in dataframe
df['BMI']=bmi(df['HeightCm'],df['WeightKg'])

#creating table of given data
table1 = {'BMI Range (kg/m2)':['18.4 and below','18.5 - 24.9','25 - 29.9','30 - 34.9',
                               '35 - 39.9','40 and above'],
          'BMI category':['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 
                           'Severely obese', 'Very severely obese'],
          'Health risk':['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 
                         'High risk','Very high risk']
         }
table1 = pd.DataFrame(table1)
table1

#finding out BMI category and Health Risk for calculated BMI and storing in lists
bmi = df['BMI']
category = []
risk = []
for i in bmi:
    if i<=18.4:
        category.append('Underweight')
        risk.append('Malnutrition risk')
    if 18.5<= i <=24.9:
        category.append('Normal weight')
        risk.append('Low risk')
    if 25<= i <=29.9:
        category.append('Overweight')
        risk.append('Enhanced risk')
    if 30<= i <=34.9:
        category.append('Moderately obese')
        risk.append('Medium risk')
    if 35<= i <=39.9:
        category.append('Severely obese')
        risk.append('High risk')
    if 40<= i :
        category.append('Very Severely obese')
        risk.append('Very High risk')
        
#creating new columns by using previously created lists
df['BMI category']=category
df['Health Risk']=risk
df

#function for conting number of overweight person in table
def count_overweight():
    return df['BMI category'].value_counts().Overweight

#finding out number of overweight person
count_overweight()