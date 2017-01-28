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



csv_file='/opt/UCS/UCSInventory.csv'
file_wget="wget -P /opt/UCS/  ftp://10.107.100.196/UCSInventory.csv"

if  os.path.isfile(csv_file) :

	os.system('rm -f /opt/UCS/UCSInventory.csv')
	print 'file delete'
	
	
os.system(file_wget)



def inster( csv_file ):
	mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb" )
	cursor = mdb.cursor()
#	cursor.execute("TRUNCATE TABLE ucs_inventory")
	csv_data = csv.reader(file(csv_file))
	next(csv_data)
#	csv_data_withnoheader = next(csv_data,None)
	

	for row in csv_data:
		row[6]=row[6][-12:]
		row[8]=row[8][0:10]
		
		cursor.execute('insert INTO ucs_inventory(Ucs,chassis_ID,SlotId,chassis_SN,usrLbl,Serial,UUID,Model,mfgtime,Adaptor,IOM,CPU,NumOfCpus,NumOfCores,AvailableMemory,Firmware,AssignedToDn)' 'VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")', row)
	cursor.close()
	print "UCS Done"

inster( csv_file )
