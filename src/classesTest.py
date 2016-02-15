import socket

class Test:
	msname = ""
	machinename = ""
	domainMBean = ""
	
	def __init__(self, user, password, url):
		print "Initializing"
		connect(user,password,url)
		self.domainMBean=cmo
		
	def printClusters(self):
		clusters=self.domainMBean.getClusters()
		
		if(len(clusters) > 0):
			print "Have a cluster"
			for i in range(len(clusters)):
				item = clusters[i]
				print item.getName()	
	
	def getClusterByName(self, name):
		cluser = ""
		
		clusters=self.domainMBean.getClusters()
		
		if(len(clusters) > 0):
			print "Have a cluster"
			for i in range(len(clusters)):
				item = clusters[i]
				if(item.getName()	== name):
					cluser = item
		return item
	
t=Test('weblogic','weblogic1','t3://localhost:7001')
t.printClusters()
print(t.getClusterByName("Cluster-0"))