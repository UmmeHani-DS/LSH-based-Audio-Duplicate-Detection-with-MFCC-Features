from flask import Flask, render_template, request
import librosa
import soundfile as sf
import numpy as np
import pickle
import statistics
import pandas as pd
import os
import glob
import scipy
from scipy import io
import warnings
warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings('ignore')
import statistics
from statistics import mean
from collections import defaultdict


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index():

    audio_file = request.files['audio_file']

    y, sr = librosa.load(audio_file, dtype='float32')
    mfccs = librosa.feature.mfcc(y=y, sr=sr)

    newFile = open(r"audiopkl.pkl", 'rb')
    data = pickle.load(newFile)
    newFile.close()

    OpFile3 = open(r"AudioFiles_mfcc.pkl", 'rb')
    newMfcc = pickle.load(OpFile3)
    OpFile3.close()

    newdata = mfccs

    # Hash Function

    def hashing(mf, x, y):
        hashfunc = []
        for i in range(0, len(mf)):
            b = np.mean(mf[i])
            a = (x * b + y) % 23
            hashfunc.append(a)
        return hashfunc

    a1 = hashing(newdata, 3, 1)
    a2 = hashing(newdata, 2, 2)
    a3 = hashing(newdata, 2, 3)
    a4 = hashing(newdata, 2, 4)
    a5 = hashing(newdata, 3, 5)
    a6 = hashing(newdata, 2, 6)
    a7 = hashing(newdata, 2, 7)
    a8 = hashing(newdata, 3, 8)
    a9 = hashing(newdata, 2, 9)
    a10 = hashing(newdata, 3, 10)

    # Conversion to 0 and 1

    def onecng(hsh):
        temp = []
        for i in range(0, len(hsh)):
            if (hsh[i] * 10) < 100:
                temp.append(1)
            else:
                temp.append(0)
        return temp

    o1 = onecng(a1)
    o2 = onecng(a2)
    o3 = onecng(a3)
    o4 = onecng(a4)
    o5 = onecng(a5)
    o6 = onecng(a6)
    o7 = onecng(a7)
    o8 = onecng(a8)
    o9 = onecng(a9)
    o10 = onecng(a10)

    # Making Bucket

    nFile = open(r"permspkl.pkl", 'rb')
    permss = pickle.load(nFile)
    newFile.close()

    def onebuc(hush, pers):
        buc = []
        minbuc = []
        for i in range(0, len(hush)):
            if hush[i] == 1:
                buc.append(pers[i])
        a = min(buc)
        return a

    sb1 = onebuc(o1, permss[0])
    sb2 = onebuc(o2, permss[1])
    sb3 = onebuc(o3, permss[2])
    sb4 = onebuc(o4, permss[3])
    sb5 = onebuc(o5, permss[4])
    sb6 = onebuc(o6, permss[5])
    sb7 = onebuc(o7, permss[6])
    sb8 = onebuc(o8, permss[7])
    sb9 = onebuc(o9, permss[8])
    sb10 = onebuc(o10, permss[9])

    # Partial Sums

    s1 = sb1 + sb2 + sb3 + sb4 + sb5
    s2 = sb6 + sb7 + sb8 + sb9 + sb10

    blist = [sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10]

    # Checking Similarity on basis of partial sums

    df1 = pd.read_csv("AudData1.csv")
    df2 = pd.read_csv("AudData2.csv")

    simlist1 = []
    simlist2 = []

    for i in df1[str(s1)]:
        simlist1.append(i)

    for i in df1[str(s2)]:
        simlist2.append(i)

    cleanedList1 = [x for x in simlist1 if str(x) != 'nan']
    cleanedList2 = [x for x in simlist2 if str(x) != 'nan']

    comp = []
    for i in cleanedList1:
        comp.append(i)

    for i in cleanedList2:
        comp.append(i)

    # Now checking similarity on basis of Bucket Data

    df3 = pd.read_csv("BucData.csv")

    OpFile3 = open(r"AudioFiles_mfcc.pkl", 'rb')
    newMfcc = pickle.load(OpFile3)
    OpFile3.close()

    names = []
    for i in newMfcc.index:
        names.append(i)

    tr = {}
    count = 0
    k = 0
    for i in df3.columns:
        for j in range(0, len(df3[i])):
            if (df3[i].loc[j] == blist[j]).any():
                count += 1
        tr[names[k]] = count
        count = 0
        k += 1

    Keymax = max(zip(tr.values(), tr.keys()))[1]
    Keymax2 = max(zip(tr.values(), tr.keys()))[0]
    Keymin = min(zip(tr.values(), tr.keys()))[1]
    Keymin2 = min(zip(tr.values(), tr.keys()))[0]

    output1 = Keymax, "has jaccard similarity", Keymax2 / 10, "to the given audio."
    output2 = Keymin, "has jaccard similarity", Keymin2 / 10, "to the given audio."

    return render_template('answer.html',output1 = output1, output2 = output2)



if __name__ == '__main__':


    app.run(debug=True)