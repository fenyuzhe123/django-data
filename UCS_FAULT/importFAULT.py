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



csv_file='/opt/UCS_FAULT/ucs-faults.csv'
file_wget="wget -P /opt/UCS_FAULT/  ftp://10.107.100.196/ucs/ucs-faults.csv"

if  os.path.isfile(csv_file) :

	os.system('rm -f /opt/UCS_FAULT/ucs-faults.csv')
	print 'file delete'
	
	
os.system(file_wget)

#######################
###inster ucs-fault data into mysql


def inster( csv_file ):
	mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb" )
	cursor = mdb.cursor()
	cursor.execute("TRUNCATE TABLE ucs_fault")
	csv_data = csv.reader(file(csv_file))
	next(csv_data)
#	csv_data_withnoheader = next(csv_data,None)
	

	for row in csv_data:
		
		cursor.execute('replace INTO ucs_fault(Ucs,lasttransition,severity,type,dn,descr)' 'VALUES(%s,%s,%s,%s,%s,%s)', row)
	
	cursor.close()
	print "UCS_FAULT Done"

inster( csv_file )
