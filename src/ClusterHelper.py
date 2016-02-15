import wl

class ClusterHelper:
	msname = ""
	machinename = ""
	domainMBean = ""
	
	def __init__(self, user, password, url):
		print "Initializing"
		wl.connect(user,password,url)
		self.domainMBean=wl.cmo		
		
	def usage(self):
		print "Usage"

#-----------------------------------
# Prints all the clusters          -
#-----------------------------------
	def printAllClusters(self):
		clusters=self.domainMBean.getClusters()
		
		if(len(clusters) > 0):
			print "Have a cluster"
			for i in range(len(clusters)):
				item = clusters[i]
				print item.getName()		

#-----------------------------------
# Gets the ClusterMBean by Name    -
#-----------------------------------
	def getClusterByName(self, name):
		cluster = None
		
		clusters=self.domainMBean.getClusters()
		
		if(len(clusters) > 0):
			print "Have a cluster"
			for i in range(len(clusters)):
				item = clusters[i]
				if(item.getName()	== name):
					cluster = item
		return cluster

#----------------------------------- 
# Adds a server to a cluster       -
#-----------------------------------
	def addServer(self, byName=True, cluster=None, server=None):
		if(byName):
			print "Adding server by name"
			addServerByName(clusterName=cluster, serverName=server)
		else:
			print "Adding server by mbean"
		
		raise SyntaxError("Must use string or object")
		# server.setCluster(cluster)
		if(cluster is None):
			print "Cluster is NONE"
		else:
			print "Cluster is " + cluster
			
		if(server is None):
			print "server is NONE"
		else:
			print "server is " + server		

	def addServerByName(self, clusterName=None, serverName=None):
		if(clusterName is None or serverName is None):
			raise SyntaxError("Either ServerName or ClusterName are missing")