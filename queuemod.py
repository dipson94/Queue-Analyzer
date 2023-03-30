
import numpy as np
import pandas as pd

def fn(case):

    df =pd.DataFrame(pd.read_csv('pyfiles/input'+str(case)+'.csv',low_memory=False))
    b_plus=df[df['BST+']=='B+']
    b_minus=df[df['BST+']=='B-']
    mod=list(set(b_plus['ETT+']))
    modlis=[1,4,5,6,7,8,9,10,11,22,12,13,14,15,16,17,21,18,19,23]
    dict=['ein','An','L1','Reg','L2','PreV_e','PreV_1','PreV_2','PreV_3','PreV_4','PreV_a','L3','Vacc_e','Vacc_1','Vacc_2','Vacc_3','Vacc_4','Vacc_a','L4','aus']
    values =[[x for x in dict]for _ in range(0,1)]
    values.append([0 for _ in range(0,len(modlis))])
    values=np.transpose(np.array(values))
    
    for x in mod:
        nw1=b_minus[b_minus['ETT+']==x]
        nw2=b_plus[b_plus['ETT+']==x] 

        max_diff = np.ptp(np.abs((np.array(nw1[['FLAGS']]).flatten())-np.array(nw2[nw2['OID-'].isin(nw1['OID-'])]['FLAGS'])))
       
        t=np.argwhere(np.array(modlis) == x)[0][0]
    
        values[t][1]=int(max_diff/60)
        
    return values

def qmod():
    a=[]
    mod=[]
    for i in range(0,4):
        temp=fn(i+1)
        a.append(temp[:,1])
        mod=temp[:,0]
    v=np.vstack((mod,a))
    dg = pd.DataFrame(np.transpose(v))
    dg.to_csv('pyfiles/queue.csv',header=["Module","1","2","3","4"],index=False)
    return v
