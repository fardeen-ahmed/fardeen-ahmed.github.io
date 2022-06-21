import os
import os.path
import subprocess
import time
import shutil
import collections
from os import path
from pathlib import Path
from os import listdir
from os.path import isfile, join
from os.path import exists

current_working_directory = os.getcwd()
payload_dumper_path = current_working_directory+"\Tools\Payload_Dumper"
img_path=".\Output\Payload_Dumper_Output\system.img"
img_path1=".\Output\Payload_Dumper_Output\system_ext.img"
img_path2=".\Output\Payload_Dumper_Output\vendor.img"
imgextractor_path=current_working_directory+"\Tools\Imgextractor.exe"
tmp_path=current_working_directory+"\Output\Image_Extractor_Output"
all_extracted_apks=current_working_directory+"\Output\All_Extracted_APKs"
extracted_apks_by_appname=current_working_directory+"\\Output\\Extracted_APKs_by_AppName"
destination = all_extracted_apks
all_app_dir_path=tmp_path+"\\system\\app" #priv-app, overlay, package
all_app_dir_path1=tmp_path+"\\system\\priv-app"
all_app_dir_path2=tmp_path+"\\system\\package"
all_app_dir_path3=tmp_path+"\\system\\overlay"
source = all_app_dir_path
extract_payload="python "+payload_dumper_path+"\payload_dumper.py --out .\Output\Payload_Dumper_Output "+payload_dumper_path+"\payload.bin"
extract_img=imgextractor_path+ " " +img_path+ " " +tmp_path
extract_img1=imgextractor_path+ " " +img_path1+ " "+tmp_path
extract_img2=imgextractor_path+ " " +img_path2+ " " +tmp_path

def execute_cmd(cmd,text):
	text=text.upper()
	p1 = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p1.communicate()
	if "DUMMY" not in text :
		text=executable_output+text
		f=open(text,'a+')
		f.write(out)
		f.close()
	return out
	
def getUserChoice():
	print("\n\nPlease select an option to continue:")
	print("1. Extract all APKs from ROM file")
	print("2. Extract APKs by APK name from ROM file")
	selected_option = input("Enter your choice: ")
	selected_option = str(selected_option)
	if selected_option == '1':
		destination = current_working_directory+"\\Output\\All_Extracted_APKs"
		All_Extracted_APKs()
		print("\nAPKs extracted & moved to \Output\All_Extracted_APKs folder . . .")
	elif selected_option == '2':
		execute_cmd("mkdir .\Output\Extracted_APKs_by_AppName","dummy")
		destination = current_working_directory+"\\Output\\Extracted_APKs_by_AppName"
		Extract_APK_by_APKName()

	else: exit ("\nEntered the wrong option! Exiting . . ")
	return destination
	
def All_Extracted_APKs():
	all_apps = os.listdir(all_app_dir_path)
	total_no_of_apps=len(all_apps)
	apps_extracted=0
	for i in all_apps:	
		apk_path=os.path.join(source, i)
		for basename in os.listdir(apk_path):
			if basename.endswith('.apk'):
				apk = os.path.join(apk_path, basename)
				shutil.copy(apk, destination)
				apps_extracted +=1
	print("\nTotal number of apps on image: ",total_no_of_apps)
 
def All_Extracted_APKs1():
	all_apps = os.listdir(all_app_dir_path1)
	total_no_of_apps=len(all_apps)
	apps_extracted=0
	for i in all_apps:	
		apk_path=os.path.join(source, i)
		for basename in os.listdir(apk_path):
			if basename.endswith('.apk'):
				apk = os.path.join(apk_path, basename)
				shutil.copy(apk, destination)
				apps_extracted +=1
	print("\nTotal number of apps on image: ",total_no_of_apps)

def All_Extracted_APKs2():
	all_apps = os.listdir(all_app_dir_path2)
	total_no_of_apps=len(all_apps)
	apps_extracted=0
	for i in all_apps:	
		apk_path=os.path.join(source, i)
		for basename in os.listdir(apk_path):
			if basename.endswith('.apk'):
				apk = os.path.join(apk_path, basename)
				shutil.copy(apk, destination)
				apps_extracted +=1
	print("\nTotal number of apps on image: ",total_no_of_apps)
 
def All_Extracted_APKs3():
	all_apps = os.listdir(all_app_dir_path3)
	total_no_of_apps=len(all_apps)
	apps_extracted=0
	for i in all_apps:	
		apk_path=os.path.join(source, i)
		for basename in os.listdir(apk_path):
			if basename.endswith('.apk'):
				apk = os.path.join(apk_path, basename)
				shutil.copy(apk, destination)
				apps_extracted +=1
	print("\nTotal number of apps on image: ",total_no_of_apps)

def Extract_APK_by_APKName():
	All_Extracted_APKs()
	all_extracted_apps = os.listdir(all_extracted_apks)
	destination = current_working_directory+"\\Output\\Extracted_APKs_by_AppName"
	apps_extracted=0
	n = int(input("\nEnter the number of APKs you want to extract:"))
	print("Enter the names of the APKs you want to extract:")
	a = [input() for j in range(n)]
	for x in a:
		if x in all_extracted_apps:
			source = all_extracted_apks
			source = os.path.join(source, x)
			shutil.copy(source, destination)
			apps_extracted +=1
		else:
			print("\n",x,"not present.")
		
	
	print("\nAPKs extracted & moved to \Output\Extracted_APKs_by_AppName folder . . .")
	execute_cmd("rmdir .\Output\All_Extracted_APKs folder /S /Q","dummy")
	
print("                                                                                                 ")	
print("|-----------------------------------------------------------------------------------------------|")
print("|                                                                                               |")
print("|    ____  _________       ___    ____  __ __    ______     __                  __              |")
print("|   / __ \/_  __/   |     /   |  / __ \/ //_/   / ____/  __/ /__________ ______/ /_____  _____  |")
print("|  / / / / / / / /| |    / /| | / /_/ / ,<     / __/ | |/_/ __/ ___/ __ `/ ___/ __/ __ \/ ___/  |")
print("| / /_/ / / / / ___ |   / ___ |/ ____/ /| |   / /____>  </ /_/ /  / /_/ / /__/ /_/ /_/ / /      |") 
print("| \____/ /_/ /_/  |_|  /_/  |_/_/   /_/ |_|  /_____/_/|_|\__/_/   \__,_/\___/\__/\____/_/       |")
print("|                                                                                               |") 
print("|                         Developed By :- @KainatKamal                                          |")  
print("|                                                                                               |")
print("|-----------------------------------------------------------------------------------------------|")

execute_cmd("rmdir Output /S /Q","dummy")
execute_cmd("mkdir Output","dummy")
execute_cmd("mkdir .\Output\Payload_Dumper_Output","dummy")
execute_cmd("mkdir .\Output\Image_Extractor_Output","dummy")
execute_cmd("mkdir .\Output\All_Extracted_APKs","dummy")

payload_path=input("\n\nEnter the Full Path of the payload.bin file: ")
if path.exists(str(payload_path)):
	shutil.copy(payload_path, payload_dumper_path)
else:
	exit("Invalid path entered! Exiting . . .")

print("\nExtracting the payload.bin. Please wait . . .")
execute_cmd(extract_payload,"dummy")
print("payload.bin extracted . . .")
print("Extracting system.img . . .")
execute_cmd(extract_img,"dummy")
print("system.img extracted . . .")
print("Extratcing system_ext.img . . .")
execute_cmd(extract_img1,"dummy")
print("system_ext.img extracted . . .")
print("Extracting vendor.img . . .")
execute_cmd(extract_img2,"dummy")
print("vendor.img extracted . . .")

selected_option = getUserChoice()

execute_cmd("rmdir .\Output\Payload_Dumper_Output /S /Q","dummy")
execute_cmd("rmdir .\Output\Image_Extractor_Output /S /Q","dummy")
execute_cmd("del .\Output\Image_Extractor_Output_statfile.txt /S /Q","dummy")
