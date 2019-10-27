import HypercliqueMiner 
import pandas as pd

def main():
    data = pd.read_csv('pumsb.dat',sep = ' ',header = None).iloc[:,:-1]
    dataset = data.values.tolist()
    
    print("Enter 1 To Produce Results For The Graphs 1 & 2 (Will Take A Long Duration)")
    print("Enter 2 To Produce Results For The Graph 3 (Will Take A Long Duration)")
    print("Enter 3 To Produce Hyperclique Results For Fixed Thresholds")
    
    inpt = int(input())
    
    if(inpt == 1):
        

        min_supp = [0.45,0.5,0.55,0.60,0.65]
        min_hconf = [0.85,0.90,0.95]
    
        TotalCountData = []
        TotalTimeData = []
        for supp_th in min_supp:
            runOncesupp = []
            runOncetime = []
            runOncesupp.append(supp_th)
            runOncetime.append(supp_th)
            for hconf_th in min_hconf:
                print('min_supp: ',supp_th,' min_hconf: ',hconf_th,sep='')
                count,Time = HypercliqueMiner.HyperCliqueMiner(dataset,supp_th,hconf_th,inpt)
                runOncesupp.append(count)
                runOncetime.append(Time)
                TotalCountData.append(runOncesupp)
                TotalTimeData.append(runOncetime)
    
        TotalCountData = pd.DataFrame(TotalCountData,columns = ['Min_Supp' , 'Count_Hconf1', 'Count_Hconf2','Count_Hconf3'])
        print(TotalCountData)
    
        print()
    
        
        TotalTimeData = pd.DataFrame(TotalTimeData,columns = ['Min_Supp' , 'Count_Hconf1', 'Count_Hconf2','Count_Hconf3'])
        print(TotalTimeData)
        
    elif(inpt == 3):
        
        print("Enter Support Threshold")
        min_supp = float(input())
        print("Enter Hconfidence Threshold")
        min_hconf = float(input())
        HypercliqueMiner.HyperCliqueMiner(dataset,min_supp,min_hconf,inpt)
        
    elif(inpt == 2):
        datasize = [4904,9808,14712,19616,24520,29424,34328,39232,44136,49046]
        timedata = []
        for dsize in datasize:
            tempdata = []
            for i in range(0,dsize):
                tempdata.append(dataset[i])
            
            count,Time = HypercliqueMiner.HyperCliqueMiner(tempdata,0.5,0.95,1)
            timedata.append(Time)
        print(datasize)
        print(timedata)
    else:
        
        print("Invalid Input")
    
if __name__ == "__main__":
    main()