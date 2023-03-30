def gen(intg,simu,path,timeslot):
    tp=[]
    for i in range(1,5):

        s="""COM	time	Objecttyp	Order Nr(A)"""+"\n"+"""GEN			"""

        arr_time=[]    
        x=0
        val=0
        while((val)<simu):
            s=s+"\n"+str(val)+"\t"+str(x+1)+"\t"+str(x+1)+"\t"
            arr_time.append(val)
            x=x+1
            if x%intg[i-1]==0:
                val=val+timeslot
        tp.append(len(arr_time))

        savloc=str(path)+"/Data"+str(i)+".txt"
        
        with open(savloc, "w") as f:
            f.write(s)
        
    return "All data files have been generated !",tp

