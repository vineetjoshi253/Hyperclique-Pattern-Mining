import time

#Threshold Values Of Support And Hconfidence
min_supp =  0.0
min_hconf = 0.0

#Global Dic. To Maintain The Support And Hconfidence Of Itemsets
SuppData = {}
HconfData = {}

#Function To Create Candidate Itemsets Of Size-1
def createC1(dataset):
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    C1 = list(map(frozenset,C1))
    return C1

#Function To Calculate The Hconfidence Of A Candidate Using Glabal Support Dic.
def hconf(Data,candidate):
    candidate = list(candidate)
    mini = 999
    for item in candidate:
        SuppIndi = SuppData[frozenset([item])]
        Supp = SuppData[frozenset(candidate)]
        conf = Supp/SuppIndi
        mini = min(mini,conf)
    return mini

#Function To Update The Glabal Hconfidence Dic.
def hconfGen(Data,Ck,K):
    hconf_count = {}
    if K == 1:
        for candidate in Ck:
            hconf_count[candidate] = 1
    else:
        for candidate in Ck:
            hconf_count[candidate] = hconf(Data,candidate) 
    HconfData.update(hconf_count)
    return hconf_count

#Function To Calculate The Support Of Candidate Itemsets Of Size K
def suppGen(Data,Ck):
    numItems = float(len(Data))
    supp_count = {}
    for transaction in Data:
        for candidate in Ck:
            if candidate.issubset(transaction):
                if not candidate in supp_count: supp_count[candidate] = 1
                else : supp_count[candidate] += 1
    for key in supp_count:
        supp_count[key] = supp_count[key]/numItems
        
    SuppData.update(supp_count)
    return supp_count

#Function To Check If An Itemset Follows Cross-Support Property Or Not.
def CrossSupport(Itemset):
    Itemset = list(Itemset)
    if(len(Itemset)==1):
        return True
    else:
        for i in range(len(Itemset)):
            for j in range(i+1,len(Itemset)):
                
                if(SuppData[frozenset([Itemset[i]])] * min_hconf > SuppData[frozenset([Itemset[j]])]):
                    return False
        return True


#Function To Prune Itemsets According To The Support Property.
def PruneSupport(Data,Ck,K):
    supp_count = suppGen(Data,Ck)
    Lk = []
    for key in supp_count:
        if supp_count[key] >= min_supp: 
            Lk.insert(0,key)
    return Lk,supp_count

#Function To Prune Itemsets According To The Hconfidence Property.
def PruneHconf(Data,Ck,K):
    hconf_count = hconfGen(Data,Ck,K)
    Lk = []
    for key in hconf_count:
        if hconf_count[key] >= min_hconf and CrossSupport(key): 
            Lk.insert(0,key)
    return Lk,hconf_count

#Generate Candidates Of Size K using Frequent Itemset Of Size K-1.
def apriori_gen(Lk, k): 
    candList = []
    for i in range(len(Lk)):
        for j in range(i+1, len(Lk)):
            #Extract the first k-2 items from each list.
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            
            L1.sort(); L2.sort()
            #If the k-2 items are equal then take the unione of both the initial sets.
            if L1==L2: 
                candList.append(Lk[i] | Lk[j])        
    return candList

def HyperCliqueMiner(data,minsupp,minhconf,inpt):
    global dataset 
    global min_supp
    global min_hconf
    
    dataset = data
    min_supp = minsupp
    min_hconf = minhconf
    
    Data= list(map(set,dataset))  
    K = 1
    start_time = time.time()
    C1 = createC1(dataset)
    L1,SuppData = PruneSupport(Data,C1,K)
    L1,hconff = PruneHconf(Data,L1,K)
    HCP = []
    HCP.append(L1)
    
    K+=1
    Ck = C1;Lk = L1
    while(len(Ck)!=0):
        Ck = apriori_gen(Lk,K)
        Lk,supp = PruneSupport(Data,Ck,K)
        SuppData.update(supp)
        Lk,hconff = PruneHconf(Data,Lk,K)
        HCP.append(Lk)
        K+=1

    finalTime = time.time() - start_time
    K=1
    count = 0
    
    if(inpt == 3):
        for LK in HCP:
            print('HCP Of Size: ',K,sep="")
            for itemsets in LK:
                print(list(itemsets))
            count+=1
            K+=1
        print()
    else:
        for LK in HCP:
            for itemsets in LK:
                count+=1
        return count,finalTime