import pandas as pd
import statistics

data = pd.read_csv('data.csv')
data = data["math score"].tolist()

mean = statistics.mean(data)
standardDeviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

FirstDevStart = mean - standardDeviation
FirstDevEnd = mean + standardDeviation
list_firstDev = [result for result in data if result> FirstDevStart and result<FirstDevEnd]
FirstDevPercentage = "{} % of Data lies in First Deviation".format(len(list_firstDev)*100/len(data))
print(FirstDevPercentage)

SecondDevStart = mean-2*standardDeviation
SecondDevEnd = mean + 2*standardDeviation
list_secondDev = [result for result in data if result> SecondDevStart and result<SecondDevEnd]
SecondDevPercentage = "{} % of data lies in Second Deviation".format(len(list_secondDev)*100/len(data))
print(SecondDevPercentage)

ThirdDevStart = mean-3*standardDeviation
ThirdDevEnd = mean + 3*standardDeviation
list_thirdDev = [result for result in data if result>ThirdDevStart and result<ThirdDevEnd]
ThirdDevPercentage = "{} % of data lies in Third Deviation".format(len(list_thirdDev)*100/len(data))
print(ThirdDevPercentage)