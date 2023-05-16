import numpy as np
import pandas as pd
import datetime
import fn
def mainfn(mod,mod1,path):
    
    thrupt=[]
    d_obj = []
    d_time =[]
   
    # Loading data with exit module
    for i in range(0,4):
        path1=path[i]        
        path2=path[i+4]        
        th,obj,time,savecsv=fn.dataextraction(i,mod,path1,path2)        
        d_obj.append(obj)
        d_time.append(time)
        thrupt.append(th)
        dg = pd.DataFrame(savecsv)
        dg.to_csv('data/result'+str(i+1)+'.csv',header=["Time","object","time in min","Total time spent"],index=False)
    # making a copy of data
    actthrpt=[]
    actthrpt=thrupt.copy()
    obj=np.array(d_obj[0])
    obj1=d_obj.copy()
    time1=d_time.copy()
    # making a statistical data
    
    d1=np.transpose(np.array([[pd.DataFrame(d_time[0][:thrupt[0]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d2=np.transpose(np.array([[pd.DataFrame(d_time[1][:thrupt[1]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d3=np.transpose(np.array([[pd.DataFrame(d_time[2][:thrupt[2]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d4=np.transpose(np.array([[pd.DataFrame(d_time[3][:thrupt[3]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    
    # combineing statistical data with other identifiers 
    L=["count","mean","std","min","25%","50%","75%","max"]
    v=np.column_stack((np.array(L),d1,d2,d3,d4))
    arr=["","case 1","case 2","case 3","case 4"]
    v1=np.copy(v)
    a=np.copy(np.array(v[1:,1:]))
    v[1:,1:]=[[str(datetime.timedelta(seconds=int(x))) for  x  in a[i]] for i in range(7)]
    arr=np.row_stack((arr,v))
    
    
    
    labels=["","case 1","case 2","case 3","case 4"]
    dg = pd.DataFrame(arr[1:],columns=labels)
    result =dg
    # Saving statistical data for exit module
    dg.to_csv("data/result.csv",index=False)
    # color prefernces for ploting
    colors=["red","orange","blue","green"]
    del d_obj
    del d_time
    del v
    del arr
    d_obj = []
    d_time =[]
    # Loading data with entry module
    for i in range(0,4):
        path1=path[i]        
        path2=path[i+4]        
        th,obj,time,savecsv=fn.dataextraction(i,mod1,path1,path2)        
        d_obj.append(obj)
        d_time.append(time)
        
    obj=np.array(d_obj[0])
    thrupt=actthrpt
  # making a statistical data for entry module
  
    d1=np.transpose(np.array([[pd.DataFrame(d_time[0][:thrupt[0]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d2=np.transpose(np.array([[pd.DataFrame(d_time[1][:thrupt[1]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d3=np.transpose(np.array([[pd.DataFrame(d_time[2][:thrupt[2]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d4=np.transpose(np.array([[pd.DataFrame(d_time[3][:thrupt[3]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    
  # combineing statistical data with other identifiers for entry module
    L=["count","mean","std","min","25%","50%","75%","max"]
    v=np.column_stack((np.array(L),d1,d2,d3,d4))
    arr=["","case 1","case 2","case 3","case 4"]
    a=np.copy(np.array(v[1:,1:]))
    v[1:,1:]=[[str(datetime.timedelta(seconds=int(x))) for  x  in a[i]] for i in range(7)]
    arr=np.row_stack((arr,v))
       
    dg = pd.DataFrame(arr[1:],columns=labels)
    qresult = dg
    # Saving statistical data for entry module
    dg.to_csv("data/queueresult.csv",index=False)
    
    
    return result,obj1,time1,colors,thrupt,v1,labels,qresult