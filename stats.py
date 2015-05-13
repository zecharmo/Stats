import pandas as pd
import scipy.stats

data = '''Region, Alcohol, Tobacco 
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# Split data by lines

data = data.splitlines()

# Split data on commas

data = [i.split(', ') for i in data]

# Convert data into pandas DataFrame

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

# Convert integers into floating point numbers

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

Calculate the mean, median, mode, range, variance, and standard deviation of the dataset

al_mean = df['Alcohol'].mean() 
to_mean = df['Tobacco'].mean() 

al_median = df['Alcohol'].median()
to_median = df['Tobacco'].median() 

al_mode = scipy.stats(df['Alcohol'])
to_mode = scipy.stats(df['Tobacco'])

al_range = max(df['Alcohol']) - min(df['Alcohol'])
to_range = max(df['Tobacco']) - min(df['Tobacco'])

al_variance = df['Alcohol'].var()
to_variance = df['Tobacco'].var()

al_st_dev = df['Alcohol'].std()
to_st_dev = df['Tobacco'].std()

print "The mean for the Alcohol and Tobacco dataset is ", al_mean, "and", to_mean
print "The median for the Alcohol and Tobacco dataset is ", al_median, "and", to_median
print "The mode for the Alcohol and Tobacco dataset is ", al_mode, "and", to_mode
print "The range for the Alcohol and Tobacco dataset is ", al_range, "and", to_range
print "The variance for the Alcohol and Tobacco dataset is ", al_variance, "and", to_variance
print "The standard deviation for the Alcohol and Tobacco dataset is ", al_st_dev, "and", to_st_dev
