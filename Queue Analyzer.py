import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf
from compare import mainfn
import numpy as np
import matplotlib.pyplot as plt
from queuemod import qmod
from datagen import gen
import os
xml="""<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.38.2 -->
<interface>
  <requires lib="gtk+" version="3.24"/>
  <object class="GtkFileFilter" id="tra">
    <patterns>
      <pattern>*.tra</pattern>
    </patterns>
  </object>
  <object class="GtkFileFilter" id="txt">
    <patterns>
      <pattern>*.txt</pattern>
    </patterns>
  </object>
  <object class="GtkWindow" id="my_window">
    <property name="can-focus">False</property>
    <property name="resizable">False</property>
    <property name="window-position">center</property>
    <property name="default-width">1440</property>
    <property name="default-height">810</property>
    <property name="icon">i.ico</property>
    <property name="urgency-hint">True</property>
    <property name="gravity">center</property>
    <property name="has-resize-grip">True</property>
    <child>
      <object class="GtkScrolledWindow">
        <property name="visible">True</property>
        <property name="can-focus">True</property>
        <property name="shadow-type">in</property>
        <child>
          <object class="GtkViewport">
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <child>
              <object class="GtkFixed">
                <property name="visible">True</property>
                <property name="can-focus">False</property>
                <child>
                  <object class="GtkLabel">
                    <property name="name">label</property>
                    <property name="width-request">50</property>
                    <property name="height-request">170</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="label" translatable="yes">Case 1


Case 2


Case 3


Case 4</property>
                  </object>
                  <packing>
                    <property name="x">76</property>
                    <property name="y">233</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="t2">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="filter">tra</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">276</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="t3">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="filter">tra</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">325</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="t4">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="filter">tra</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">374</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel">
                    <property name="name">label</property>
                    <property name="width-request">50</property>
                    <property name="height-request">170</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="label" translatable="yes">Case 1


Case 2


Case 3


Case 4</property>
                  </object>
                  <packing>
                    <property name="x">67</property>
                    <property name="y">445</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="d1">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="halign">start</property>
                    <property name="filter">txt</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">440</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="d2">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="filter">txt</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">489</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="d3">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="filter">txt</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">538</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="d4">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="filter">txt</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">587</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="txt1">
                    <property name="width-request">98</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Only enter integer</property>
                    <property name="width-chars">10</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">238</property>
                    <property name="y">643</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="txt2">
                    <property name="name">dfewg</property>
                    <property name="width-request">98</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Only enter integer</property>
                    <property name="width-chars">10</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">237</property>
                    <property name="y">694</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel">
                    <property name="width-request">227</property>
                    <property name="height-request">80</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="label" translatable="yes">enter the module at object exits


 enter the module at object enters</property>
                  </object>
                  <packing>
                    <property name="y">641</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="gen">
                    <property name="label" translatable="yes">Generate  Statistics</property>
                    <property name="width-request">165</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="receives-default">True</property>
                    <property name="halign">center</property>
                    <property name="valign">center</property>
                    <signal name="clicked" handler="on_button_clicked" swapped="no"/>
                  </object>
                  <packing>
                    <property name="x">169</property>
                    <property name="y">749</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="result">
                    <property name="width-request">300</property>
                    <property name="height-request">300</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                  <packing>
                    <property name="x">369</property>
                    <property name="y">44</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="int">
                    <property name="width-request">50</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="width-chars">5</property>
                    <property name="primary-icon-tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">7</property>
                    <property name="y">25</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButton" id="datagen">
                    <property name="label" translatable="yes">Data Gen</property>
                    <property name="width-request">95</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="receives-default">True</property>
                    <signal name="clicked" handler="datagenerator" swapped="no"/>
                  </object>
                  <packing>
                    <property name="x">255</property>
                    <property name="y">25</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="simu">
                    <property name="width-request">60</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">simulation time</property>
                    <property name="width-chars">7</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">6</property>
                    <property name="y">67</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="dirselect">
                    <property name="width-request">164</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="tooltip-text" translatable="yes">Select Folder to Save Files</property>
                    <property name="action">select-folder</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">180</property>
                    <property name="y">67</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="int1">
                    <property name="width-request">58</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="width-chars">5</property>
                    <property name="primary-icon-tooltip-markup" translatable="yes">Persons/slot</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">69</property>
                    <property name="y">25</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="int2">
                    <property name="width-request">58</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="width-chars">5</property>
                    <property name="primary-icon-tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">131</property>
                    <property name="y">25</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="int3">
                    <property name="width-request">58</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="width-chars">5</property>
                    <property name="primary-icon-tooltip-text" translatable="yes">Persons/slot</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">193</property>
                    <property name="y">25</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="result1">
                    <property name="width-request">300</property>
                    <property name="height-request">300</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                  <packing>
                    <property name="x">865</property>
                    <property name="y">44</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel">
                    <property name="width-request">50</property>
                    <property name="height-request">110</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="label" translatable="yes">Select .tra files</property>
                    <property name="angle">90</property>
                    <attributes>
                      <attribute name="weight" value="bold"/>
                      <attribute name="scale" value="1"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">13</property>
                    <property name="y">271</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel">
                    <property name="width-request">50</property>
                    <property name="height-request">111</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="label" translatable="yes">Select .txt files</property>
                    <property name="angle">90</property>
                    <attributes>
                      <attribute name="weight" value="bold"/>
                      <attribute name="scale" value="1"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">13</property>
                    <property name="y">478</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel">
                    <property name="name">label</property>
                    <property name="width-request">181</property>
                    <property name="height-request">30</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <property name="label" translatable="yes">Case 1       Case 2       Case 3       Case 4</property>
                  </object>
                  <packing>
                    <property name="x">12</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="status">
                    <property name="width-request">260</property>
                    <property name="height-request">25</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <attributes>
                      <attribute name="foreground" value="#08a6ffff0000"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">37</property>
                    <property name="y">105</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="Dwell">
                    <property name="width-request">176</property>
                    <property name="height-request">20</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <attributes>
                      <attribute name="foreground" value="#08a6ffff0000"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">457</property>
                    <property name="y">10</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="Queue">
                    <property name="width-request">150</property>
                    <property name="height-request">20</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <attributes>
                      <attribute name="foreground" value="#08a6ffff0000"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">960</property>
                    <property name="y">11</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkImage" id="drw">
                    <property name="width-request">1000</property>
                    <property name="height-request">562</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                  <packing>
                    <property name="x">349</property>
                    <property name="y">393</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="plot">
                    <property name="width-request">260</property>
                    <property name="height-request">25</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <attributes>
                      <attribute name="foreground" value="#08a6ffff0000"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">704</property>
                    <property name="y">354</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkImage" id="modq">
                    <property name="width-request">1000</property>
                    <property name="height-request">562</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                  <packing>
                    <property name="x">351</property>
                    <property name="y">1031</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="qlegend">
                    <property name="width-request">300</property>
                    <property name="height-request">700</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                  <packing>
                    <property name="x">26</property>
                    <property name="y">1030</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="qplot">
                    <property name="width-request">325</property>
                    <property name="height-request">25</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                    <attributes>
                      <attribute name="foreground" value="#08a6ffff0000"/>
                    </attributes>
                  </object>
                  <packing>
                    <property name="x">770</property>
                    <property name="y">986</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="timeslot">
                    <property name="width-request">74</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="tooltip-text" translatable="yes">Enter the time between each slots</property>
                    <property name="width-chars">7</property>
                    <property name="input-purpose">number</property>
                  </object>
                  <packing>
                    <property name="x">91</property>
                    <property name="y">67</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkFileChooserButton" id="t1">
                    <property name="width-request">200</property>
                    <property name="height-request">34</property>
                    <property name="visible">True</property>
                    <property name="can-focus">True</property>
                    <property name="filter">tra</property>
                    <property name="show-hidden">True</property>
                    <property name="title" translatable="yes">Case 1</property>
                  </object>
                  <packing>
                    <property name="x">134</property>
                    <property name="y">227</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="datagenresults">
                    <property name="width-request">360</property>
                    <property name="height-request">80</property>
                    <property name="visible">True</property>
                    <property name="can-focus">False</property>
                  </object>
                  <packing>
                    <property name="y">137</property>
                  </packing>
                </child>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>"""
folder_name = 'pyfiles'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
def datagenerator(case):
    intg=[]
    intg.append(int(builder.get_object("int").get_property("text")))
    intg.append(int(builder.get_object("int1").get_property("text")))
    intg.append(int(builder.get_object("int2").get_property("text")))
    intg.append(int(builder.get_object("int3").get_property("text")))
    timeslot=int(builder.get_object("timeslot").get_property("text"))
    simu=int(builder.get_object("simu").get_property("text"))
    path=str(builder.get_object("dirselect").get_filename())
    status,tp=gen(intg,simu,path,timeslot)
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
    fig.savefig('pyfiles/plot.png', dpi=(1000/fig.get_figwidth()))
    
    pixbuf = GdkPixbuf.Pixbuf.new_from_file("pyfiles/plot.png")
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
    fig.savefig('pyfiles/plotq.png', dpi=(1000/fig.get_figwidth()))
    modq=builder.get_object("modq")
    pixq = GdkPixbuf.Pixbuf.new_from_file("pyfiles/plotq.png")
    modq.set_from_pixbuf(pixq)
    builder.get_object("qplot").set_property("label","Stack bar graph of waiting time at modules")
    builder.get_object("qlegend").set_property("label","""ein 		Entrance

An 			Sign Up

L1 			Lane 

Reg 		Registration

L2 			Lane 2

PreV_e 	Pre Vaccination Enter

PreV_1	Pre Vaccination Counter 1

PreV_2	Pre Vaccination Counter 2

PreV_3	Pre Vaccination Counter 3

PreV_4	Pre Vaccination Counter 4

PreV_a	Pre Vaccination Exit

L3			Lane 3

Vacc_e 	Vaccination Entrance

Vacc_1 	Vaccination Counter 1

Vacc_2 	Vaccination Counter 2

Vacc_3 	Vaccination Counter 3

Vacc_4 	Vaccination Counter 4

Vacc_a 	Vaccination Exit

L4 			Lane 4

aus 		Exit""")


def on_button_clicked(case):
    path=[]
    txt1=builder.get_object("txt1")
    t1=txt1.get_property("text")
    txt2=builder.get_object("txt2")
    t2=txt2.get_property("text")
    path.append(builder.get_object("t1").get_filename()) #tra file
    path.append(builder.get_object("t2").get_filename())
    path.append(builder.get_object("t3").get_filename())
    path.append(builder.get_object("t4").get_filename())
    path.append(builder.get_object("d1").get_filename())
    path.append(builder.get_object("d2").get_filename())
    path.append(builder.get_object("d3").get_filename())
    path.append(builder.get_object("d4").get_filename())
    zcom(t1,t2,path)

builder = Gtk.Builder()
builder.add_from_string(xml)
builder.connect_signals({"on_button_clicked": on_button_clicked,"datagenerator":datagenerator})
datagen= builder.get_object("datagen")
window = builder.get_object("my_window")
window.set_title("Vaccination center Simulation")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon_from_file("depend/i.ico")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()