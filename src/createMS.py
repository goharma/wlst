# Python Imports
import socket
from ClusterHelper import ClusterHelper 

def getCluster():
	clusters=cmo.getClusters()
	if len(clusters)


# Get the managed server name
msname=socket.gethostname()+'_MS'

# Get the machine name
machinename=socket.getfqdn()

# connect to the admin server
try:
	connect('weblogic','weblogic1','t3://localhost:7001')
except Exception, e:
	print "Could not connect to "		

# Get the cluster
clusters=cmo.getClusters()

# Enter edit session
edit()
startEdit()

# Add machine
cd('/Machines')
machine=create(machinename, 'Machine')

# Add server
cd('/Servers')
server=create(msname, 'Server')
cd(msname)

# Assign machine to server
cd('/Servers/' + msname)
cmo.setMachine(machine)

# Add server to cluster
cmo.setCluster(clusters[0])

# Save and Activate changes
save()
activate()