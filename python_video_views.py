import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#load data set form csv. file
df=pd.read_csv('data.csv')

#Calculate the total views
day50 = df[df['Day'] == 50]

total = day50[['Video 1 views) The sound of my cat mu-ing',
       'Video 2 views) Mew vs Mewtwo: the sequel!',
       'Video 3 views) mu: the meanest greek letter!',
       'Video 4 views) How to get Mew in Pokopia!']].sum(axis=1).values[0]

print(total)

#Create plot of videos' views across 50 days
video=['Video 1 views) The sound of my cat mu-ing',
       'Video 2 views) Mew vs Mewtwo: the sequel!',
       'Video 3 views) mu: the meanest greek letter!',
       'Video 4 views) How to get Mew in Pokopia!']

plt.figure(figsize=(10,6))

for col in video:
    plt.plot(df['Day'], df[col], label=col.split(')')[0])
    
plt.xlabel('Day')
plt.ylabel('videos')
plt.legend()
plt.grid(True)

plt.show()

#Calculate the maximum growth rate of video1
V = df['Video 1 views) The sound of my cat mu-ing']
t = df['Day']

dVdt = np.gradient(V, t, edge_order=2)

m=np.max(dVdt)
print(m)

#Plot the growth rate of video1
V = df['Video 1 views) The sound of my cat mu-ing']
t = df['Day']

dVdt = np.gradient(V, t, edge_order=2)

plt.figure(figsize=(10,6))

plt.plot(t, dVdt, label=('video 1 growth rate'))
    
plt.xlabel('Days')
plt.ylabel('view')
plt.legend()
plt.grid(True)

plt.show()

#Define time and views for video1
t= df['Day']
V = df['Video 1 views) The sound of my cat mu-ing']

def logistic_model(t, a, b, k):
    return a / (1 + np.exp(-k * (t - b)))


f = [6000, 15, 0.4]
p,c = curve_fit(logistic_model, t, V, f)


a, b, k = p
print(f"Parameter a: {a:.3f}")
print(f"Parameter b: {b:.3f}")
print(f"Parameter k: {k:.3f}")

#Plot the time and views of video1
t=df['Day']
V=df['Video 1 views) The sound of my cat mu-ing']

def logistic_model(t,a,b,k):
    return a/(1+np.exp(-k*(t-b)))

f=[6000,15,0.3]
p,c= curve_fit(logistic_model, t, V, f)
a,b,k=p

plt.figure(figsize=(10,6))

plt.scatter(t,V,label='video 1')

T=np.linspace(1,50,100)
plt.plot(T,logistic_model(T,*p),
         label='f(t)')

plt.xlabel('Days')
plt.ylabel('Cumulative Views')
plt.legend()
plt.grid(True)

plt.show()