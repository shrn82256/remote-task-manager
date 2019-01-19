import psutil, os

def getPids():
	return psutil.pids()

def getAllPInfo():
	AllPInfo = []
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['name', 'username', 'cpu_percent', 'pid', 'num_threads', 'status', 'nice'])
		except psutil.NoSuchProcess:
			pass
		else:
			AllPInfo.append(pinfo)
	return AllPInfo

def killProcess(pid):
	p = psutil.Process(pid)
	p.terminate()

def getAllFileSystemsInfo():
	partitions = []
	for partn in psutil.disk_partitions():
		partnData = list(partn[0:3])

		du = psutil.disk_usage(partn[0])

		partnData.extend(du)
		partitions.append(partnData)
	return partitions

def getCPUperc():
	return psutil.cpu_percent(percpu=True)