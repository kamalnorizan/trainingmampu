import time

print(time.perf_counter())
print(time.localtime())
print(time.asctime(time.localtime()))

#formated date
strdate = time.strftime("%d-%m-%Y",time.localtime())
print('formated date: '+strdate)

#formated time
strtime = time.strftime("%H:%M:%S",time.localtime())
print('formated time: '+strtime)


#formated timestamp
strtimestamp = time.strftime("%d-%m-%Y %H:%M:%S",time.localtime())
print('formated timestamp: '+strtimestamp)

