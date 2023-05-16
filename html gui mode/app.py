
from flask import Flask, render_template,request
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import csv
import os

import numpy as np
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
pyfiles_path = os.path.join(script_dir, 'pyfiles')
sys.path.insert(0, pyfiles_path)
from queuemod import qmod
from datagen import gen
from compare import mainfn

folder_name = 'data'
if not os.path.exists(folder_name):
      os.makedirs(folder_name)
app = Flask(__name__)
@app.route('/')
@app.route('/upload', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'analysis' in request.form:
            tra=[]
            txt=[]
            for i in range(0,4):
                tra.append(request.files["tra"+str(i+1)].read().decode('utf-8') )
            for i in range(0,4):
                txt.append(request.files["txt"+str(i+1)].read().decode('utf-8') )
            entrymod=int(request.form.get('entry'))
            exitmod=int(request.form.get('exit'))
            
            folder_name = 'data'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            for i in range(0,4):
                tra.append(txt[i])
            stat,d_obj,d_time,colors,thrupt,v,labels,qresult=mainfn(exitmod,entrymod,tra)
            t1 = stat.to_html(index=False)
            t2 = qresult.to_html(index=False)
            
            for i in range(0,4):
                plt.plot(d_obj[i],d_time[i],color=colors[i],label=labels[i])
                plt.plot(np.linspace(0,thrupt[i], thrupt[i]),[int(v[1][i+1])]*len(np.linspace(0,thrupt[i], thrupt[i])),color=colors[i],linestyle='--')
                
            plt.xlabel('Number of People')
            plt.ylabel('Time spent in sec')
            plt.legend()
            plt.grid(True)
            plt.title("Total Dwell Time")
            plt.savefig('data/plot.png')
            plot_img = BytesIO()
            plt.savefig(plot_img, format='png')
            plot_img.seek(0)
            plot1_url = base64.b64encode(plot_img.getvalue()).decode()
            plt.close() 
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
            plot2_img = BytesIO()
            plt.savefig(plot2_img, format='png')
            plot2_img.seek(0)
            plot2_url = base64.b64encode(plot2_img.getvalue()).decode()
            plt.close() 
            stbr=""""""

            return render_template('index.html',t1=t1,t2=t2,plot1_url=plot1_url,plot2_url=plot2_url,stbr=stbr)
        if 'datagen' in request.form:
            ppl=[]
            for i in range(0,4):
                ppl.append(int(request.form.get("c"+str(i+1))))
            slot_interval=int(request.form.get("si"))
            simulation_time=int(request.form.get("simu"))
            path="data"
            t,m=gen(ppl, simulation_time, path, slot_interval)
            
            return render_template('index.html',m=m)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)