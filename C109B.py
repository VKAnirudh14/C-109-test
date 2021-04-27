import csv
import pandas as pd 
import statistics

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)
print("Mean and Median  Of Height Is {},{} and {}% ",format(height_mean,height_median))
print("Mean and Median  Of Weight Is {},{} and {}% ",format(weight_mean,weight_median))