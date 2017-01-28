import ftplib
import sys
import getpass
import os.path
import time
import os
import subprocess
import csv
import MySQLdb
import string


#csv_file='/opt/UCS/UCSInventory.csv'
csv_file='/opt/INC_CHG/change_request.csv'
mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb")
cursor = mdb.cursor()
#cursor.execute("TRUNCATE TABLE changeinfo")
csv_data = csv.reader(file(csv_file))
cursor.execute("TRUNCATE TABLE change_info")
next(csv_data)
#q = 'insert INTO changeinfo(number,state,start_date,short_description,type,approval,cab_date,assigned_to) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
for row in csv_data:
        cursor.execute('replace INTO change_info(number,state,start_date,short_description,type,approval,cab_date,assigned_to)' 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',row)
#        cursor.execute(q,(row,))

#



#for row in csv_data:
#        row[6]=row[6][-12:]
#        row[8]=row[8][0:10]
#                
#        cursor.execute('insert INTO ucs_inventory(Ucs,chassis_ID,SlotId,chassis_SN,usrLbl,Serial,UUID,Model,mfgtime,Adaptor,IOM,CPU,NumOfCpus,NumOfCores,AvailableMemory,Firmware,AssignedToDn)' 'VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")', row)



#x=cursor.execute("select * from changeinfo")
#print x
cursor.close()
print "Well Done"
