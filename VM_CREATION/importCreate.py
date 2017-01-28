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



csv_file='/opt/VM_CREATION/vmcreation-last7days.csv'
file_wget="wget -P /opt/VM_CREATION/  ftp://10.107.100.196/vmware/vmcreation-last7days.csv"

if  os.path.isfile(csv_file) :

	os.system('rm -f /opt/VM_CREATION/vmcreation-last7days.csv')
	print 'file delete'
	
	
os.system(file_wget)

#######################
###inster VM_CTEATION data into mysql


def insert( csv_file ):
	mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb" )
	cursor = mdb.cursor()
#	cursor.execute("TRUNCATE TABLE ucs_inventory")
	csv_data = csv.reader(file(csv_file))
	next(csv_data)
#	csv_data_withnoheader = next(csv_data,None)
	

	for row in csv_data:
		i = cursor.execute('select * from vm_creation where CreatedTime=%s',row[0])
		if i==0:
			if row[2].startswith('Removed'):
				cursor.execute('insert INTO vm_creation(CreatedTime,UserName,FullFormattedMessage,tag)' 'VALUES(%s,%s,%s,"removed")', row)
			else:
				cursor.execute('insert INTO vm_creation(CreatedTime,UserName,FullFormattedMessage,tag)' 'VALUES(%s,%s,%s,"created")', row)
		else:
			cursor.execute('delete from vm_creation where CreatedTime=%s',row[0])
			if row[2].startswith('Removed'):
				cursor.execute('insert INTO vm_creation(CreatedTime,UserName,FullFormattedMessage,tag)' 'VALUES(%s,%s,%s,"removed")', row)
			else:
				cursor.execute('insert INTO vm_creation(CreatedTime,UserName,FullFormattedMessage,tag)' 'VALUES(%s,%s,%s,"created")', row)
	cursor.close()
	print "VM_CTEATION insert Done"

insert( csv_file )
