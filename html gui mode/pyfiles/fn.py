"""
only useful idenfiers from decoded .tra file
* FLAGS corresponds to time in seconds, which makes sense to the module and object event
* ETT+ corresponds to modules number in the Dosimis model
* BST+ corresponds to the current event.
* B+ and B- corresponds to entry and exit of object respectively
* OID- corresponds to object
identifiers from data.txt file
* Objecttyp corresponds to object
* COM corresponds to arrival time

"""
import numpy as np
import pandas as pd
import csv

def dataextraction(case,mod,path1,path2):
 # The data from .tra file is extracted with slicing and wrote to input.csv file
    dg=pd.DataFrame()

    array = list(csv.reader(path1.splitlines(), delimiter=' '))
    
    array[2].append("0")
    array[2].append("0")
    with open('data/input'+str(case+1)+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(array[2:])
    
        
    # Total time, list of module, list of objects, throughtput time and arrival intervel stored to variables

    df =pd.DataFrame(pd.read_csv('data/input'+str(case+1)+'.csv')) # tra file dataframe
    df=df.fillna(0)
    df=df[df['BST+']=='B-']  # slicing tra file dataframe based on event object module exit
    
    # New data frame formed with time,object corresponding to desired module
    ar=np.array(list(csv.reader(path2.splitlines(), delimiter='\t')))

    arvl = pd.DataFrame(ar[2:],columns=["COM","time","Objecttyp","Order Nr(A)"]) #loading Arrival dataframe
    arvl=arvl.fillna(0)
    arvl.to_csv("temp.csv",index=None)
    
    
  
    data1=np.array(df[df["ETT+"]==mod]['FLAGS']).astype(int)  # module exit time array
    data2=np.array(df[df["ETT+"]==mod]['OID-']).astype(int)   # object array 
    data3=data1/60
    data3=[int(x) for x in data3] # module exit time array in minutes
    arvl =pd.DataFrame(pd.read_csv('temp.csv'))
    data4=data1-np.array(arvl[arvl["Objecttyp"].isin(np.array(df[df["ETT+"]==mod]['OID-'].astype(float)))]["COM"]).astype(int)  # total time spent by object in the system
   
    
    result=np.column_stack((data1,data2,data3,data4)) # dataframe to write to csv 
    return len(data4),data2,data4,result
