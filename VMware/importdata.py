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



csv_file='/opt/VMware/VMinventory.csv'
zip_file='/opt/VMware/VMinventory.zip'
file_wget="wget -P /opt/VMware/  ftp://10.119.237.248/VMinventory.zip"


if	os.path.isfile(zip_file):

		os.system('rm -f /opt/VMware/VMinventory.csv')
		os.system('rm -f /opt/VMware/VMinventory.zip')
		print 'file delete'



os.system(file_wget)
os.system('unzip /opt/VMware/VMinventory.zip')
os.system('mv /opt/VMware/*.csv /opt/VMware/VMinventory.csv')




def inster( csv_file ):
		mdb = MySQLdb.connect("localhost","root","1234,qwer","cmdb" )
		cursor = mdb.cursor()
		cursor.execute("TRUNCATE TABLE vm_inventory")
		csv_data = csv.reader(file(csv_file))
                next(csv_data)

		
		for row in csv_data :
			cursor.execute('replace INTO vm_inventory(HostName,Name,InsUUID,OS_Family,MoRef,NumSocket,NumCoresPerSocket,Total_Core,MemoryMB,VMStatus,Network,MAC,VLAN_ID,Network_Adapter,IpAddress,VMDisk_Count,ESXHost,ClusterName,Element_Manager,DataCenter,GuestId,Market,Total_Disk_Count,FolderLocation,VMXpath,VMTools_verison,VMTools_status,OS_Version,VMDisk_AllocatedInKB,RDMDisk_AllocatedInKB,Total_StorageAllocatedinGB,Total_Disk_UsageInKB,RDMDisk_Count,HDDetails,Template,RDMFlag,Org,prod_ID,Product,ProductFound,Rail_NodePath_ID,Rail_NodePath_Name,DeviceType,QB_ID,DC_ID,Sizing)' 'VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")', row)
		cursor.close()
		print "VMware Done"



inster( csv_file )
