# import libraries
import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_1samp
from scipy.stats import binom_test
from scipy.stats import binomtest

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

print(heart.info())
print(heart.heart_disease.value_counts())

#1 subset yes_hd cholesterol
chol_yes_hd = yes_hd.chol

#2 patients with heart disease have cholesterol higher than 240?
print('Chol yes_hd mean:', np.mean(chol_yes_hd))

#3 Do people with heart disease have high cholesterol levels (greater than or equal to 240 mg/dl) on average?
# Null: People with heart disease have an average cholesterol level equal to 240 mg/dl
# Alternative: People with heart disease have an average cholesterol level that is greater than 240 mg/dl

#4 run null hypothesis test and print p-value
tstat, pval = ttest_1samp(chol_yes_hd, 240)
print('P-value patients with HD:',pval/2)
print('According to p-val less than the threshold 5%, indicates that the null hypothesis is significant, which means that patients with heart disease are likely to have a cholesterol level above 240 mg/dl, but since the null hipothesis is True, it means we have a Type I Error')

#5 run same test for null hypothesis with patient not diagnosed with heart disease
# subset no_hd cholesterol
chol_no_hd = no_hd.chol
#2 patients without heart disease have cholesterol higher than 240?
print('Chol no_hd mean:', np.mean(chol_no_hd))
tstat, pval = ttest_1samp(chol_no_hd, 240)
print('P-value patients without HD:',pval/2)
print('The outcome of p-value (is not significant) evidencing that its unlikely that patients without heart disease have a cholesterol level higher than 240 mg/dl')

#6 number of patients in the dataset
num_patients = len(heart)
print('Num patients in dataset (num of observ.):', num_patients)

#7 Proportion of Fasting Blood Sugar (fbs) above 120 mg/dl patients
num_highfbs_patients = np.sum(heart.fbs == 1)
print('Num of patients with high level of fbs:', num_highfbs_patients)

#8 About 8% of US population has diabetes. Calculate 8% of the sample size
print('8% of sample (303 patients):', int(num_patients * .08))

print('Proportion high fbs in sample:', (num_highfbs_patients / num_patients).round(4) *100)
print('The dataset sample shows high fbs patients represents roughly 15% of the sample population, and almost doble od the US average of 8%.')

#9-10 Does this sample come from a population in which the rate of fbs > 120 mg/dl is equal to 8%?
# Null: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl
# Alternative: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl
null_p = 0.08
# pval = binom_test(45, num_patients, p=null_p, alternative='greater')
pval = binomtest(num_highfbs_patients, num_patients, p=null_p, alternative='greater').pvalue
print('P-value:', pval)
print('The outcome suggest that this sample likely comes from a population where ore than 8% of people have fbs > 120 mg/dl.')
