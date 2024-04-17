celcius=[23,25,28,30,40]
fahren=[0,0,0,0,0]
j=0
for i in celcius:
    x=i*1.8 + 32
    fahren[j]=x
    j+=1
print('Celcius   = ' , celcius)
print('Fahren    = ' , fahren)