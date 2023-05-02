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

def dataextraction(case,mod,path1,path2):
 # The data from .tra file is extracted with slicing and wrote to input.csv file
  dg=pd.DataFrame()
  file_path = path1
  with open(file_path, "r") as file:
      contents = file.readlines()
      array = []      
      for line in contents[3:]:
          elements = line.strip().split()
          array.append([element for element in elements])      
      title = contents[2].strip().split()      
      title_array = [element for element in title]      
      title_array.append("0")
      title_array.append("0")
      dg = pd.DataFrame(array)  
  dg.to_csv('pyfiles/input'+str(case+1)+'.csv',header=title_array,index=False)
     
  # Total time, list of module, list of objects, throughtput time and arrival intervel stored to variables
  
  df =pd.DataFrame(pd.read_csv('pyfiles/input'+str(case+1)+'.csv')) # tra file dataframe
  df=df.fillna(0)
  df=df[df['BST+']=='B-']  # slicing tra file dataframe based on event object module exit

  # New data frame formed with time,object corresponding to desired module
  arvl = pd.read_csv(path2, sep='\t') #loading Arrival dataframe
  arvl=arvl.fillna(0)
  data1=np.array(df[df["ETT+"]==mod]['FLAGS']).astype(int)  # module exit time array
  data2=np.array(df[df["ETT+"]==mod]['OID-']).astype(int)   # object array 
  data3=data1/60
  data3=[int(x) for x in data3] # module exit time array in minutes
  data4=data1-np.array(arvl[arvl["Objecttyp"].isin(np.array(df[df["ETT+"]==mod]['OID-'].astype(float)))]["COM"]).astype(int)  # total time spent by object in the system
  result=np.column_stack((data1,data2,data3,data4)) # dataframe to write to csv 
  return len(data4),data2,data4,result
