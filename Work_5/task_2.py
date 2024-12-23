import numpy as np
import matplotlib.pyplot as plt 
import scipy

def show_data(years, hares, lynxes, carrots):
    plt.figure(figsize=(10,6))
    plt.plot(years, hares, label='Hare', marker='o')
    plt.plot(years, lynxes, label='Lynx', marker='o')
    plt.plot(years, carrots, label='Carrot', marker='o')
    plt.title('Changes in Hare, Lynx and Carrot populations (1900-1920)')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_mean_std(types, labels):
    for i in range(len(types)):
        print(f"{labels[i]} mean = {np.mean(types[i])}, std = {np.std(types[i])}")
        
def print_max(types, labels):
    for i in range(len(types)):
        print(f"{labels[i]} max = {np.max(types[i])} in the {years[np.argmax(types[i])]}")

def print_by_the_year(types, labels, threshold = 50000):
    for i in range(len(types)):
        over = types[i] > threshold
        year_over = years[over]
        print(f"The {labels[i]} was more than {threshold} in {year_over} years.")

def print_top2_min(types, labels):
    for i in range(len(types)):
        min = np.argsort(types[i])[:2]
        year_min = years[min]
        print(f"{labels[i]} - top 2 years with the smallest population: {year_min}")                
        
def print_hare_lynx(years, hares, lynxes):
    hare_grad = np.gradient(hares)
    lynx_grad = np.gradient(lynxes)
    plt.figure(figsize=(10,6))
    plt.plot(years, hare_grad, label='Change in Hare population', marker='o')
    plt.plot(years, lynx_grad, label='Change in Lynx population', marker='o')
    plt.title('Changes in Hare and Lynx populations (1900-1920)')
    plt.xlabel('Year')
    plt.ylabel('Change in Count')
    plt.legend()
    plt.grid(True)
    plt.show()
    corr_matrix = np.corrcoef(hare_grad, lynx_grad)[0,1]
    print(f"Correlation between Hare and Lynx populations: {corr_matrix}")



data = np.loadtxt("D:\\GitHub\\data_analysis\\populations.txt")
years = data[:,0]
hares = data[:,1]
lynxes = data[:,2]
carrots = data[:,3]
show_data(years, hares, lynxes, carrots)

types = [hares, lynxes, carrots]
labels = ['Hare', 'Lynx', 'Carrot']
print_max(types, labels)
print_by_the_year(types, labels)
print_top2_min(types, labels)
print_hare_lynx(years, hares, lynxes)