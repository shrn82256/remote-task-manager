from flask import Flask, render_template, request
from datetime import datetime
import processes
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/filesystem")
def filesystem():
    return render_template("fs.html")


@app.route("/resources")
def resources():
    return render_template("res.html")


@app.route('/processes', methods=['POST'])
def getProcessesData():
    return json.dumps(processes.getAllPInfo())


@app.route('/killproc', methods=['POST'])
def killproc():
    pid = int(request.form['pid'])
    processes.killProcess(pid)
    return ""


@app.route('/fsdata', methods=['POST'])
def fsdata():
    return json.dumps(processes.getAllFileSystemsInfo())


@app.route('/cpugraphdata', methods=['POST'])
def cpugraphdata():
    return json.dumps(processes.getCPUperc())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run(debug=True)
