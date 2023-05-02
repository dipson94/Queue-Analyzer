import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf,GLib
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, 'pyfiles/')
from queuemod import qmod
from datagen import gen
from compare import mainfn
import depend

# Arriaval data generator
def datagenerator(case):
    persons=[]
    persons.append(int(builder.get_object("int").get_property("text")))
    persons.append(int(builder.get_object("int1").get_property("text")))
    persons.append(int(builder.get_object("int2").get_property("text")))
    persons.append(int(builder.get_object("int3").get_property("text")))
    time_slot=int(builder.get_object("timeslot").get_property("text"))
    Simulation_time=int(builder.get_object("simu").get_property("text"))
    path=str(builder.get_object("dirselect").get_filename())
    status,tp=gen(persons,Simulation_time,path,time_slot)
    datagenresults="""				Case 1		Case 2		Case 3 	Case 4

Total People	   """+str(tp[0])+"""		   """+str(tp[1])+"""		    """+str(tp[2])+"""		   """+str(tp[3])+"""	"""
    builder.get_object("datagenresults").set_property("label",datagenresults)
    builder.get_object("status").set_property("label",status)

def zcom(t1,t2,path):
    stat,d_obj,d_time,colors,thrupt,v,labels,qresult=mainfn(int(t1),int(t2),path)
    label1=builder.get_object("result")
    label1.set_property("label", stat)
    label2=builder.get_object("Dwell")
    label2.set_property("label", "Total Dwell Time Statistics")
    label3=builder.get_object("result1")
    label3.set_property("label", qresult)
    label4=builder.get_object("Queue")
    label4.set_property("label", "Queue Time Statistics")
    drw=builder.get_object("drw")
    fig, ax = plt.subplots(figsize=(16, 9))
    for i in range(0,4):
        ax.plot(d_obj[i],d_time[i],color=colors[i],label=labels[i])
        ax.plot(np.linspace(0,thrupt[i], thrupt[i]),[int(v[1][i+1])]*len(np.linspace(0,thrupt[i], thrupt[i])),color=colors[i],linestyle='--')
        
    ax.set_xlabel('Number of People')
    ax.set_ylabel('Time spent in sec')
    ax.legend()
    ax.grid(True)
    fig.savefig('data/plot.png', dpi=(1000/fig.get_figwidth()))
    
    pixbuf = GdkPixbuf.Pixbuf.new_from_file("data/plot.png")
    drw.set_from_pixbuf(pixbuf)
    builder.get_object("plot").set_property("label","Generated from Dwell Time")
    v=qmod()
    ls=[[0 for _ in range(20)] for _ in range(4)]
    for x in range(0,4):
        ls[x]=list(int(i) for i in (v[x+1]))
    fig,ax = plt.subplots(figsize=(16, 9))
    ax.bar(v[0], ls[0], color=colors[0],label=labels[0])
    ax.bar(v[0], ls[1],bottom=ls[0], color=colors[1],label=labels[1])
    ax.bar(v[0], ls[2], bottom=[sum(x) for x in zip(ls[0], ls[1])], color=colors[2],label=labels[2])
    ax.bar(v[0], ls[3], bottom=[sum(x) for x in zip(ls[0], ls[1],ls[2])], color=colors[3],label=labels[3])
    for i, v in enumerate(ls[0]):
        if v != 0:
            ax.text(i, v/2, str(v), ha='center', va='center')
        if ls[1][i] != 0:
            ax.text(i, v+ls[1][i]/2, str(ls[1][i]), ha='center', va='center')
        if ls[2][i] != 0:
            ax.text(i, v+ls[1][i]+ls[2][i]/2, str(ls[2][i]), ha='center', va='center')
        if ls[3][i] != 0:
            ax.text(i, v+ls[1][i]+ls[2][i]+ls[3][i]/2, str(ls[3][i]), ha='center', va='center')
    ax.set_title('Stack bar graph of waiting time at modules')
    ax.set_xlabel('\nModules')
    ax.set_ylabel('Waiting Time/ Case')
    ax.legend()
    fig.savefig('data/plotq.png', dpi=(1000/fig.get_figwidth()))
    modq=builder.get_object("modq")
    pixq = GdkPixbuf.Pixbuf.new_from_file("data/plotq.png")
    modq.set_from_pixbuf(pixq)
    builder.get_object("qplot").set_property("label","Stack bar graph of waiting time at modules")
    builder.get_object("qlegend").set_property("label",depend.qlegend)


def on_button_clicked(case):
    folder_name = 'data'
    if not os.path.exists(folder_name):
      os.makedirs(folder_name)
    path=[]
    txt1=builder.get_object("txt1")
    t1=txt1.get_property("text")
    txt2=builder.get_object("txt2")
    t2=txt2.get_property("text")
    path.append(builder.get_object("t1").get_filename())    # .tra files
    path.append(builder.get_object("t2").get_filename())
    path.append(builder.get_object("t3").get_filename())
    path.append(builder.get_object("t4").get_filename())
    path.append(builder.get_object("d1").get_filename())    # .txt files
    path.append(builder.get_object("d2").get_filename())
    path.append(builder.get_object("d3").get_filename())
    path.append(builder.get_object("d4").get_filename())
    zcom(t1,t2,path)

builder = Gtk.Builder()
builder.add_from_string(depend.xml)
builder.connect_signals({"on_button_clicked": on_button_clicked,"datagenerator":datagenerator})
datagen= builder.get_object("datagen")
window = builder.get_object("my_window")
window.set_title("Vaccination center Simulation")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon(depend.pixbuf)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()