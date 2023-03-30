import numpy as np
import pandas as pd
import datetime
import fn
def mainfn(mod,mod1,path):
    
    thrupt=[]
    d_obj = []
    d_time =[]
    

    for i in range(0,4):
        path1=path[i]
        
        path2=path[i+4]
        
        th,obj,time=fn.dataextraction(i,mod,path1,path2)
        
        d_obj.append(obj)
        d_time.append(time)
        thrupt.append(th)
    
    actthrpt=[]
    actthrpt=thrupt.copy()
    obj=np.array(d_obj[0])
    D=np.array([[0 for _ in range(5)] for _ in range(8)])
    obj1=d_obj.copy()
    time1=d_time.copy()
    
    d1=np.transpose(np.array([[pd.DataFrame(d_time[0][:thrupt[0]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d2=np.transpose(np.array([[pd.DataFrame(d_time[1][:thrupt[1]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d3=np.transpose(np.array([[pd.DataFrame(d_time[2][:thrupt[2]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d4=np.transpose(np.array([[pd.DataFrame(d_time[3][:thrupt[3]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    L=["count","mean","std","min","25%","50%","75%","max"]
    v=np.column_stack((np.array(L),d1,d2,d3,d4))
    arr=["","case 1","case 2","case 3","case 4"]
    v1=np.copy(v)
    a=np.copy(np.array(v[1:,1:]))
    v[1:,1:]=[[str(datetime.timedelta(seconds=int(x))) for  x  in a[i]] for i in range(7)]
    arr=np.row_stack((arr,v))
    
    result = ""
    for row in arr:
      for col in row:
        if len(col)<20:
          if col=="mean":
            result=result+col+" "*(18-len(col))  
          if col=="std":
            result=result+col+" "*(22-len(col))            
          else:
            if col!="mean":
              result=result+col+" "*(20-len(col))
        else:
          result=result+col
      result=result+"\n\n"
    
    labels=["case 1","case 2","case 3","case 4"]
    dg = pd.DataFrame(arr)
    dg.to_csv("pyfiles/result.csv",index=False)
    
    colors=["red","orange","blue","green"]
    del d_obj
    del d_time
    del v
    del arr
    d_obj = []
    d_time =[]
    
    for i in range(0,4):
        path1=path[i]
        
        path2=path[i+4]
        
        th,obj,time=fn.dataextraction(i,mod1,path1,path2)
        
        d_obj.append(obj)
        d_time.append(time)
        
    
 
    obj=np.array(d_obj[0])
    D=np.array([[0 for _ in range(5)] for _ in range(8)])
    thrupt=actthrpt
    d1=np.transpose(np.array([[pd.DataFrame(d_time[0][:thrupt[0]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d2=np.transpose(np.array([[pd.DataFrame(d_time[1][:thrupt[1]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d3=np.transpose(np.array([[pd.DataFrame(d_time[2][:thrupt[2]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    d4=np.transpose(np.array([[pd.DataFrame(d_time[3][:thrupt[3]]).describe(include="all")] for _ in range(1)])).ravel().astype(int)
    L=["count","mean","std","min","25%","50%","75%","max"]
    v=np.column_stack((np.array(L),d1,d2,d3,d4))
    arr=["","case 1","case 2","case 3","case 4"]
    a=np.copy(np.array(v[1:,1:]))
    v[1:,1:]=[[str(datetime.timedelta(seconds=int(x))) for  x  in a[i]] for i in range(7)]
    arr=np.row_stack((arr,v))
    qresult = ""
    for row in arr:
      for col in row:
        if len(col)<20:
          if col=="mean":
            qresult=qresult+col+" "*(18-len(col))  
          if col=="std":
            qresult=qresult+col+" "*(22-len(col))            
          else:
            if col!="mean":
              qresult=qresult+col+" "*(20-len(col))
              
        else:
          qresult=qresult+col
          
      qresult=qresult+"\n\n"
    
    dg = pd.DataFrame(arr)
    dg.to_csv("pyfiles/queueresult.csv",index=False)
    
    
    return result,obj1,time1,colors,thrupt,v1,labels,qresult
