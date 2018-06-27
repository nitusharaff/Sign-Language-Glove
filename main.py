from __future__ import print_function
from flask import Flask
from flask import request
from flask import render_template
import numpy as np
from scipy import stats
from modeling import model
import MySQLdb
from flask import session, redirect
from flask import url_for
import serial
import time
import pyttsx


# print (model)
app = Flask(__name__)
app.secret_key = "root"
ans = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/trial', methods=['POST', 'GET'])
def trial():
    ans = request.form['ans']
    session['ans'] = ans
    return render_template("trial.html", ans=ans)


@app.route('/vids', methods=['GET', 'POST'])
def new():
   if request.method=='GET':
    store = session.get('ans')
    words = store.split(" ")
    con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="speech")
    cur = con.cursor()
    a = []
    for i in words:
        # print ("i=",i)
        j = str(i)
        cur.execute('SELECT sign FROM asignl WHERE word= %s', [j])
        data = cur.fetchall()
        # print(data)
        if len(data) < 1:
            continue
        a.append(url_for('static', filename=data[0][0]))
        session['tdata'] = a

    params = session.get('tdata')
    textword = store.upper()
    return render_template("vids.html", params=params, words=textword)
   elif request.method == 'POST':
       print ("here")
       return redirect(url_for('index'))


param = []

@app.route('/glove', methods=['GET', 'POST'])
def glove():
    if request.method == 'GET':
        t_end = time.time() + 60 * 1
        param = []
        ser = serial.Serial('COM3', 9600)
        predicted_svm="something"
        while True:

            count = 0
            data = []
            while (count < 5):
                # time.sleep(1)
                if (ser.isOpen() == False):
                    ser.open()
                    ser.flushInput()
                    print(count)
                elif (count == 4):
                    data.append(ser.readline())
                    print("if count")
                    ser.close()
                else:
                    data.append(ser.readline())
                    #print(ser.readline())

                    print(count)
                count = count + 1

            data1 = data
            data1.pop(0)
            lines = []
            for line in data1:
                lines.append(line.decode('utf-8', 'slashescape'))
            lines1 = lines
            [s.strip('\r\n') for s in lines1]
            y = []
            for x in lines1:
                y.append(map(int, x.split(",")))
            print("1")

            if(int(y[0][10])== 0):
                predicted_svm="nothing"
                print("nothing")
                break

            else:
                for i in range(len(y)):
                    y[i].pop(-1)
                print("1")
                #col_totals = [sum(x) for x in zip(*y)]
                # print(col_totals)
                #means = [int(x / 10) for x in col_totals]
                arr = np.array(y)
                m = stats.mode(arr)
                modes=m[0]
                print(modes)
                predicted_svm = model.predict(modes.reshape(1,-1))
                #predicted_svm = predicted_svm[1:-1]
                engine = pyttsx.init()
                #engine.say("beep")
                engine.say(predicted_svm)
                engine.runAndWait()
                param.append(predicted_svm[0])
                print(param)
                time.sleep(3)
                print("sleep over")
                # return  redirect(url_for('glove'))
        print("something")
        return render_template("glove.html", param=param)
    elif request.method == 'POST':
        return redirect(url_for('index'))
        # return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
