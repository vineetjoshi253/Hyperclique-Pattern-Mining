import pandas as pd
import matplotlib.pyplot as plt

print("Enter 1 For Confidence - Pruning Graph")
print("Enter 2 For Confidence/Support - Time Graph")
print("Enter 3 For Data Size - Time Graph")

inpt = int(input())

if(inpt == 1):
    data = pd.read_csv("CountOutput.csv")
    columns = data.columns.tolist()

    X = data[columns[0]].tolist()
    Y1 = data[columns[1]].tolist() 
    Y2 = data[columns[2]].tolist()
    Y3 = data[columns[3]].tolist()

    plt.plot(X,Y1,marker='o',label="min_hconf = 0.85")
    plt.plot(X,Y2,marker='o',label="min_hconf = 0.90")
    plt.plot(X,Y3,marker='o',label="min_hconf = 0.95")

    plt.legend(loc='upper right')
    plt.title("Confidence-Pruning Effect", fontsize=16, fontweight='bold')
    plt.xlabel("Minimum Support Thresholds")
    plt.ylabel("Number Of Hyperclique Patterns")
    plt.show()

elif(inpt == 2):
    data = pd.read_csv("TimeOutput.csv")
    columns = data.columns.tolist()

    X = data[columns[0]].tolist()
    Y1 = data[columns[1]].tolist() 
    Y2 = data[columns[2]].tolist()
    Y3 = data[columns[3]].tolist()

    plt.plot(X,Y1,marker='o',label="min_hconf = 0.85")
    plt.plot(X,Y2,marker='o',label="min_hconf = 0.90")
    plt.plot(X,Y3,marker='o',label="min_hconf = 0.95")

    plt.legend(loc='upper right')
    #plt.title("Confidence-Pruning Effect", fontsize=16, fontweight='bold')
    plt.title("Confidence - Execution Time Effect", fontsize=16, fontweight='bold')
    plt.xlabel("Minimum Support Thresholds")
    plt.ylabel("Execution Time (S)")
    plt.show()

elif(inpt == 3):
    data = pd.read_csv("SizeOutput.csv")
    columns = data.columns.tolist()

    X = data[columns[0]].tolist()
    Y = data[columns[1]].tolist() 
    
    plt.plot(X,Y,marker='o',label="min_hconf = 0.95,min_supp = 0.5")
    
    plt.legend(loc='upper left')
    #plt.title("Confidence-Pruning Effect", fontsize=16, fontweight='bold')
    plt.title("Data Size - Execution Time ", fontsize=16, fontweight='bold')
    plt.xlabel("Datasize")
    plt.ylabel("Execution Time (S)")
    plt.show()

else:
    print("Invalid Input")    
