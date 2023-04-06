import random 
import statistics
import pandas as pd 
import csv 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 

# initialising the data 
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
print("original population mean", population_mean)
print("original standard deviation of data", population_stdev)

# collecting random number of values and repeating the process to get sample data 
def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        randomindex = random.randint(0, len(data) - 1)
        value = data[randomindex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean 

meanlist = []
for i in range(1, 100):
    setofmeans = random_set_of_means(30)
    meanlist.append(setofmeans)

samplemean = statistics.mean(meanlist)
sampledev = statistics.stdev(meanlist)
print("sample data mean", samplemean)
print("sample data standard deviation", sampledev)

# finding first, second and third standard deviations 
first_start, first_end = samplemean - sampledev, samplemean + sampledev
second_start, second_end = samplemean - (2*sampledev), samplemean + (2*sampledev)
third_start, third_end = samplemean - (3*sampledev), samplemean + (3*sampledev)
print("std1", first_start, first_end)
print("std2", second_start, second_end)
print("std3", third_start, third_end)

# creating a fig and plotting the data 
fig = ff.create_distplot([meanlist], ["reading time"], show_hist=False)
# adding traces 
fig.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.17], mode='lines', name="sample mean"))
fig.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x = [first_start, first_start], y = [0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x = [second_start, second_start], y = [0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x = [second_end, second_end], y = [0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x = [third_start, third_start], y = [0, 0.17], mode='lines', name="mean"))
fig.add_trace(go.Scatter(x = [third_end, third_end], y = [0, 0.17], mode='lines', name="mean"))
# passing show figure to display the figure 
fig.show()