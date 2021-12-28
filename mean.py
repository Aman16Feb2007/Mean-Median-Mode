import csv

with open('Height-Weight.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
fileData.pop(0)
# print(fileData)

newData = []
for i in range(len(fileData)):
    n_num = fileData[i][2]
    newData.append(float(n_num))
    

# print(newData)
n = len(newData)
total = 0

for x in newData:
    total += x

mean = total/n
print('Mean is : {}'.format(mean))