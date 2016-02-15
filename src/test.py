import socket
from ClusterHelper import ClusterHelper 

clusterHelper = ClusterHelper('weblogic','weblogic1','t3://localhost:7001')

clusterHelper.printAllClusters()

# EXISTING CLUSTER
cluster = clusterHelper.getClusterByName('Cluster-0')
print "getClusterByName: " + cluster.getName()
clusterHelper.addServer(server='Server', cluster='Cluster')

# NON EXISTING CLUSTER
cluster = clusterHelper.getClusterByName('Cluster-1')

if cluster is None:
	print "getClusterByName: NOT FOUND"
else:	
	print "getClusterByName: " + cluster.getName()

