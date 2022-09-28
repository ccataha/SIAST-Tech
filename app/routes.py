from distutils import core
from unittest import result
from flask import render_template, flash, redirect, url_for, request, session,  Response
from flask import request, json, jsonify, Response 

from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from flask_sse import sse

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, Model


import psutil
import netifaces
import json
import os
import subprocess
import sys
import numpy as np
import pandas as pd 
import pickle
import os, signal
from app.forms import If_form
from app import app, db, manager
from app.models import User
flows = []
resp = {}
pid = None
interface = ''
basedir = os.path.abspath(os.path.dirname(__file__))
core_resources = os.path.join(os.path.dirname(basedir), 'core_resources')
     



@app.route('/',methods=['GET'])  # 
def index():
    return render_template('index.html')
       
@app.route('/analyze',methods=['POST','GET'])  # 
@login_required           # decorators that modifies function follows
def analyze():
       interface = netifaces.interfaces()
       form = If_form();
       print(request.url)
       interface.insert(0,"Выберите интерфейс")
       form.interface.choices = interface
       form.interface.default = interface[0]
       
       ifconfig = subprocess.check_output(['ifconfig'])

       return render_template('interface.html', form = form, ifconfig = ifconfig)

def cicflowmeter(start,interface):
    global pid
    if start:     
        p = subprocess.Popen(["cicflowmeter","-i",
                            interface,"-c",
                            os.path.join(basedir, 'static/flows.csv') ,
                            "-u",
                            request.url_root+"predict/"]) # Call subprocess
        pid = p.pid
    elif not start:        
        os.kill(pid, signal.SIGSTOP)
        
        



@app.route('/start',methods=['POST','GET'])
#@login_required           # decorators that modifies function follows
def start():
        form = If_form();      
        cicflowmeter(True,form.interface.data)
        session['interface'] = form.interface.data
        return redirect(url_for('home'))




@app.route('/ip', methods=['GET'])
#@login_required
def ip():
    ip = request.args.get('ip')
    if request.method == 'GET':
        whois = subprocess.check_output([f'whois {ip}'],shell=True)
        # traceroute = subprocess.check_output([f'traceroute  {ip}'],shell=True)        
        message = {'whois': whois.decode("utf-8")}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/newInterface')
#@login_required
def newInterface():
    cicflowmeter(False,None)
    return redirect(url_for('analyze'))


@app.route('/stop')
#@login_required
def stop():
    cicflowmeter(False,None)
    print("Stooooooooooooooop")
    return redirect(url_for('home'))


#De-Serializing Model
model = pickle.load(open(os.path.join(basedir, 'nids_model.pkl'),"rb"))
model_bin = pickle.load(open(os.path.join(core_resources, 'lstm.pkl'),"rb"))
model_multi = pickle.load(open(os.path.join(core_resources, 'knn.pkl'),"rb"))

@app.route('/testing')
#@login_required
def testing():
    Total_multi = 0 
    DDoS_multi = 0 
    DoSGoldenEye_multi = 0           
    DoSHulk_multi = 0 
    DoSSlowhttptest_multi = 0 
    DoSSlowloris_multi = 0 
    FTPPatator_multi = 0 
    Heartbleed_multi = 0 
    Infiltration_multi = 0 
    PortScan_multi = 0 
    SSHPatator_multi = 0 
    BruteForce_multi = 0 
    SQLInjection_multi = 0 
    Xss_multi = 0 
    Bot_multi = 0

    file_bin = pd.read_csv(os.path.join(core_resources, 'test_x_smt.csv'));
    file_bin = file_bin[file_bin.label != "BENIGN"] 
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    target_multi = le.fit_transform(file_bin["label"])
    data_multi = file_bin.drop("label", axis=1)
    data_multi = np.array(data_multi)
    target_multi = np.array(target_multi)
    print(data_multi.shape, target_multi.shape)
    scaler = MinMaxScaler(feature_range=(-1,1))
    scaler.fit(np.nan_to_num(data_multi).astype(float))
    data_multi = scaler.transform(np.nan_to_num(data_multi).astype(float))
    data_multi = data_multi.reshape(data_multi.shape[0], data_multi.shape[1], 1)
    pred_multi_raw = model_multi.predict(data_multi)    
    pred_multi = np.argmax(pred_multi_raw, axis=1)
    
    for x in pred_multi:
        Total_multi += 1
        if x == 0:
            Bot_multi += 1
        elif x == 1:
            DDoS_multi += 1
        elif x == 2:
            DoSGoldenEye_multi += 1          
        elif x == 3:
            DoSHulk_multi += 1
        elif x == 4:
            DoSSlowhttptest_multi += 1
        elif x == 5:
            DoSSlowloris_multi += 1
        elif x == 6:
            FTPPatator_multi += 1
        elif x == 7:
            Heartbleed_multi += 1
        elif x == 8:
            Infiltration_multi += 1
        elif x == 9:
            PortScan_multi += 1
        elif x == 10:
            SSHPatator_multi += 1
        elif x == 11:
            BruteForce_multi += 1
        elif x == 12:
            SQLInjection_multi +=1
        elif x == 13:
            Xss_multi += 1
 
    Accuracy_multi = metrics.accuracy_score(target_multi, pred_multi)
    Recall_multi = metrics.recall_score(target_multi, pred_multi, average="weighted")
    Precision_multi = metrics.precision_score(target_multi, pred_multi, average="weighted")
    F1score_multi = metrics.f1_score(target_multi, pred_multi, average="weighted")
    Roc_auc_multi = metrics.roc_auc_score(to_categorical(target_multi), np.nan_to_num(pred_multi_raw), multi_class='ovr')
#-----------------------------------------------------------------------------------------------------------------------------
    Benign_bin = 0
    Attack_bin = 0
    Total_bin = 0
    data_bin = []
    target_bin = []
    file = pd.read_csv(os.path.join(core_resources, 'test_x_smt.csv'));
    for n, i in file.iterrows():
        a = []
        for j in i[:-1]:
            a.append(j)
        data_bin.append(a)
        target_bin.append(0 if i[-1] == 'BENIGN' else 1) #0 benign 1 attack
    del file
    data_bin = np.array(data_bin)
    target_bin = np.array(target_bin)
    print(data_bin.shape, target_bin.shape)
    #scaler = MinMaxScaler(feature_range=(-1,1))
    #scaler.fit(np.nan_to_num(data_bin).astype(float))
    #data_bin = scaler.transform(np.nan_to_num(data_bin).astype(float))
    #scaler = MinMaxScaler(feature_range=(-1,1))
    #scaler.fit(np.nan_to_num(data_bin).astype(float))
    scaler = MinMaxScaler(feature_range=(-1,1))
    scaler.fit(np.nan_to_num(data_bin).astype(float))
    data_bin = scaler.transform(np.nan_to_num(data_bin).astype(float))
    data_bin = data_bin.reshape(data_bin.shape[0], data_bin.shape[1], 1)
    #df.drop('Unnamed: 0',
    #axis='columns', inplace=True)
    pred_bin = model_bin.predict(data_bin)    
    # (unique, counts) = np.unique(pred, return_counts=True)
    pred_bin = np.argmax(pred_bin, axis=1)
    Accuracy_bin = (metrics.accuracy_score(target_multi , pred_multi))
    
    for x in pred_bin:
        Total_bin += 1
        if x == 0:
            Benign_bin += 1
        elif x == 1:
            Attack_bin += 1          

    result = {"Accuracy_multi" : Accuracy_multi,
                "Bot_multi": Bot_multi, "Total_multi": Total_multi, "DDoS_multi": DDoS_multi,
                "DoSGoldenEye_multi": DoSGoldenEye_multi, "DoSHulk_multi": DoSHulk_multi, "DoSSlowhttptest_multi": DoSSlowhttptest_multi,
                "DoSSlowloris_multi": DoSSlowloris_multi, "FTPPatator_multi": FTPPatator_multi, "Heartbleed_multi": Heartbleed_multi,
                "Infiltration_multi": Infiltration_multi, "PortScan_multi": PortScan_multi, "SSHPatator_multi": SSHPatator_multi,
                "BruteForce_multi": BruteForce_multi, "SQLInjection_multi": SQLInjection_multi, "Xss_multi": Xss_multi, 
                "Accuracy_bin" : Accuracy_bin, "Benign_bin": Benign_bin, "Attack_bin" : Attack_bin, "Total_bin" : Total_bin,
                "Recall_multi": Recall_multi, "Precision_multi": Precision_multi, "F1score_multi": F1score_multi, "Roc_auc_multi": Roc_auc_multi}

    print(result)
    return render_template('testing.html', result=result)
  

@app.route('/predict/', methods=['POST'])
#@login_required
def predict():
    req = request.get_json()
    df1 = pd.DataFrame(data=req["data"], columns=req["columns"] )
    df2 = df1.copy()
    cols = [' Bwd Packet Length Std', ' min_seg_size_forward', ' PSH Flag Count',
            ' Min Packet Length',' Init_Win_bytes_backward', ' ACK Flag Count', 
            'Total Length of Fwd Packets', ' Subflow Fwd Bytes',
            'Init_Win_bytes_forward', ' Bwd Packet Length Min', ' Fwd IAT Std',
            ' Flow IAT Max', ' URG Flag Count',' Destination Port', ' Flow IAT Mean',
            ' Flow Duration', ' Bwd Packets/s', 'Fwd IAT Total', 'Bwd IAT Total', 
            ' act_data_pkt_fwd', ' Down/Up Ratio', ' Idle Min', ' Fwd Packet Length Min', 
            ' Bwd IAT Max', ' Fwd Packet Length Mean']
    feature = df1[cols]

    # Making Pridiction
    pred = model.predict(feature) 
    label = pred[0]

    if label == 0:
        df1['label'] = 'Benign'
    elif label == 1:
        df1['label'] = 'Bot'
    elif label == 2:
        df1['label'] = 'DDoS'
    elif label == 3:
        df1['label'] = 'Infilteration'
    elif label == 4:
        df1['label'] = 'PortScan'
    elif label == 5:
        df1['label'] = 'Brute-Force'
    elif label == 6:
        df1['label'] = 'Sql-Injection'
    elif label == 7:
        df1['label'] = 'XSS'

    df1.rename(columns = {" Destination Port": "dst_port"}, 
        inplace = True)

    result = df1.to_json(orient="records")    
    sse.publish(result, type='greeting')
    resp = {"label" :  df1['label'].values[0]}
    print(resp)
    return jsonify(resp)

@app.route('/home')
@login_required
def home():    
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next') 

            return redirect(next_page)
        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please, fill all fields!')
        elif password != password2:
            flash('Passwords are not equal!')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
#@login_required
def logout():
    logout_user() 
    return redirect(url_for('login_page')) #or index


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response