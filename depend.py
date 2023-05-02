import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf,GLib
import base64
# Icon image data in base64 to avoid external dependency
image_data = "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"
# Decode the Base64 string
decoded_data = base64.b64decode(image_data)
# Using image loader
loader = GdkPixbuf.PixbufLoader.new()
loader.write(decoded_data)
loader.close()
pixbuf = loader.get_pixbuf()
# GTK GUI in xml stored as Raw string, embedded to avoid external dependency
xml="""<interface>
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
