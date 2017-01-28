import ftplib 
import sys
import getpass 
import os.path
import time
import os 
import subprocess
import datetime
import csv
import MySQLdb



csv_file='/opt/VM_EVENT/event.csv'
file_wget="wget -P /opt/VM_EVENT/  ftp://10.107.100.196/vmware/event.csv"

if  os.path.isfile(csv_file) :

	os.system('rm -f /opt/VM_EVENT/event.csv')
	print 'file delete'
	
	
os.system(file_wget)

#######################
###inster VM_event data into mysql


def inster( csv_file ):
	mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb" )
	cursor = mdb.cursor()
#	cursor.execute("TRUNCATE TABLE ucs_inventory")
	csv_data = csv.reader(file(csv_file))
	next(csv_data)
#	csv_data_withnoheader = next(csv_data,None)
	

	for row in csv_data:
		
		cursor.execute('replace INTO vm_event(CreatedTime,UserName,FullFormattedMessage)' 'VALUES(%s,%s,%s)', row)
	
	cursor.execute('insert into vm_event_temp(CreatedTime,UserName,FullFormattedMessage) select distinctrow* from vm_event')
	cursor.execute("TRUNCATE TABLE vm_event")
	cursor.execute('insert into vm_event(CreatedTime,UserName,FullFormattedMessage) select * from vm_event_temp')
	cursor.execute("TRUNCATE TABLE vm_event_temp")
	cursor.close()
	print "VM_EVENT Done"

inster( csv_file )
