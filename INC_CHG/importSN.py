
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

#######################
csv_file1='/opt/INC_CHG/incident.csv'
csv_file2='/opt/INC_CHG/change_request.csv'
csv_file1_tmp='/opt/INC_CHG/incident_tmp.csv'
csv_file2_tmp='/opt/INC_CHG/change_request_tmp.csv'

#######################

###check the file exits
def file_exits( file ):
		if os.path.exists( file ):
			message = "Ok, the "+file+" file exists."
			return 1
		else:
			message = "Sorry, I cannot find the "+file+" file."
			return 0
		print message
#######################

###check the file empty
def file_empty1( file ):
#		if os.test -s ( file ):
		if os.path.getsize( file ) !=0:
			rename = "mv -f "+file+" /opt/INC_CHG/incident.csv"
			os.system(rename) 
			print "Ok, the "+file+" file is not empty, rename successfully"
			return 1
		else:
			print "the file "+file+" is empty"
			return 0


def file_empty2( file ):
		if os.path.getsize( file ) !=0:
			rename = "mv -f "+file+" /opt/INC_CHG/change_request.csv"
			os.system(rename)
			print "Ok, the "+file+" file is not empty, rename successfully"
			return 1
		else:
			print "the file "+file+" is empty"
			return 0
######################

###delete file
def delete_file( file ):
		dl_file="rm -rf "+file
		os.system(dl_file)
		print "removed file"

#######################
###Download the incidents and change csv file from services-now
def download1( file ):
	file_wget="wget -O '"+file+"' --auth-no-challenge --continue --no-check-certificate 'https://activenetwork.service-now.com/sys_report_template.do?CSV&jvar_report_id=dd9d8d4f1386a2400dc4b0322244b099' --http-user=czhang4 --http-password=Fenyuzhe234!"
	os.system( file_wget )

def download2( file ):
	file_wget="wget -O '"+file+"' --auth-no-challenge --continue --no-check-certificate 'https://activenetwork.service-now.com/sys_report_template.do?CSV&jvar_report_id=3acf24071346a2400dc4b0322244b08e' --http-user=czhang4 --http-password=Fenyuzhe234!"
	os.system( file_wget )

#######################
###inster inc data into mysql
def inster1( csv_file ):
	mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb")
	cursor = mdb.cursor()
        cursor.execute("TRUNCATE TABLE incident_info")
	csv_data = csv.reader(file(csv_file))
	next(csv_data)
	for row in csv_data:
		cursor.execute('replace INTO incident_info(number,state,short_description,opened_at,caller_id,u_business_service,u_item_type,u_service_name,u_issue_type,assigned_to)' 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
	cursor.close()
	print "inc done"

###inster chg data into mysql
def inster2( csv_file ):
        mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb")
        cursor = mdb.cursor()
        cursor.execute("TRUNCATE TABLE change_info")
        csv_data = csv.reader(file(csv_file))
        next(csv_data)

        for row in csv_data:
                cursor.execute('replace INTO change_info(number,state,start_date,short_description,type,approval,cab_date,assigned_to)' 'VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', row)
        cursor.close()
        print "chg done"

#######################


#delete_file( csv_file1 )
#delete_file( csv_file2 )
download1( csv_file1_tmp )
download2( csv_file2_tmp )

if file_empty1( csv_file1_tmp )==1 :
	if file_exits( csv_file1 )==1 :
		inster1( csv_file1 )
	else:
		print "No new inc data"
else:
	print "No new inc data"

if file_empty2( csv_file2_tmp )==1 :
	if file_exits( csv_file2 )==1 :
		inster2( csv_file2 )
	else:
		print "No new chg data"
else:
	print "No new chg data"

#if file_exits( csv_file1 )==1 :
#   inster1( csv_file1 )
#else: 
#   print "No new inc data"
#
#if file_exits( csv_file2 )==1 :
#   inster2( csv_file2 )
#else:
#   print "No new chg data"
#
