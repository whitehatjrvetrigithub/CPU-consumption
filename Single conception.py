import matplotlib.pyplot as plt
import psutil as p
app_name_list = []
app_name_percentage_list = []
count = 0
for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name,'--cpu_usage : ', cpu_usage)
        app_name_list.append(name)
        app_name_percentage_list.append(cpu_usage)
maxnumber=max(app_name_percentage_list)
print(maxnumber)
indexmax=app_name_percentage_list.index(maxnumber)
print(indexmax)

minnumber=min(app_name_percentage_list)
print(minnumber)
indexmin=app_name_percentage_list.index(minnumber)
print(indexmin)

maxname=app_name_list[indexmax]
minname=app_name_list[indexmin]
applist=[maxname,minname]
app_percent=[maxnumber,minnumber]
plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(applist,app_percent,width=0.6
,color=("purple", "green", "red", "blue", "orange", "pink"))
plt.show()