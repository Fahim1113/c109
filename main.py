import random
import statistics
import plotly.figure_factory as ff

arr = []

for i in range(0, 1000):
  a = random.randint(1, 6)
  b = random.randint(1, 6)
  arr.append(a + b)



# mean = sum(arr)/len(arr)
mean = statistics.mean(arr)
sd = statistics.stdev(arr)
median = statistics.median(arr)
mode = statistics.mode(arr)

firstSDStart, firstSDEnd = mean-sd, mean+sd
listOfDataWithinFirstSD = [result for result in arr if result>firstSDStart and result < firstSDEnd]

secondSDStart, secondSDEnd = mean-(sd*2), mean+(sd*2)
listOfDataWithinSecondSD = [result for result in arr if result > secondSDStart and result < secondSDEnd]

thirdSDStart, thirdSDEnd = mean-(sd*3), mean+(sd*3)
listOfDataWithinThirdSD = [result for result in arr if result > thirdSDStart and result < thirdSDEnd]

print("{}% of data lies within 1 standard deviation".format(len(listOfDataWithinFirstSD)*100.0/len(arr)))
print("{}% of data lies within 2 standard deviation".format(len(listOfDataWithinSecondSD)*100.0/len(arr)))
print("{}% of data lies within 3 standard deviation".format(len(listOfDataWithinThirdSD)*100.0/len(arr)))

print("mean:", mean, "\nstandard deviation:", sd, "\nmedain:", median,"\nmode:", mode)

fig = ff.create_distplot([arr],["Dice distrobution plot"], show_hist=False)
# fig.show()