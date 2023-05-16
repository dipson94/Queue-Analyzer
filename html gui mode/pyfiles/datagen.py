def gen(persons,Simulation_time,path,time_slot):
    tp=[] # total people per case
    for i in range(1,5):
        # initialize raw string
        s="""COM	time	Objecttyp	Order Nr(A)"""+"\n"+"""GEN			"""

        arr_time=[]    
        x=0
        value=0
        while((value)<Simulation_time):
            s=s+"\n"+str(value)+"\t"+str(x+1)+"\t"+str(x+1)+"\t"
            arr_time.append(value)
            x=x+1
            if x%persons[i-1]==0:
                value=value+time_slot
        tp.append(len(arr_time))

        save_location=str(path)+"/Data"+str(i)+".txt"
        
        with open(save_location, "w") as f:
            f.write(s)
        
    return "All data files have been generated !",tp

