import glob
import os
import shutil
import subprocess
import webbrowser
import sys
import time

file = open('project.csv','r')
print("\tExisting Projects : ")
numberOfProjects = 1
existingProjects = []
for line in file:
    fields = line.strip().split(',')
    existingProjects.append(fields[0])
    print ("\t\t" + str(numberOfProjects) + " . " + fields[0])
    numberOfProjects+=1
file.close()

print("\tEnter the Project name or Number : ", end='')
project = input()

def projectDetails(projectId):
    with open('project.csv','r') as open_file:
        lines = open_file.readlines()
        projectName = lines[project].strip().split(',')
        return projectName

def projectByName(word):
    with open('project.csv','r') as file:
        lines = file.read().split("\n")
        for i,line in enumerate(lines):
            if word in line: 
                return i

try:
    project = int(project) - 1
    if(numberOfProjects - 2 < project):
        print("\nInvalid entry. No such project")
        exit()
    else:
        print("\n\t\tLooks Good. Keep going...")
except:
    if(project == None):
        print("Invalid Name for Project")
        exit()
    else:
        if(project in existingProjects):
            print("\n\t\tLooks Good. Keep going...")
        else:
            print("Invalid Name for Project")
            exit()
    project = projectByName(project)

xamppDir = "c:/xampp/"
apacheDir = xamppDir + "apache/conf/"
confList = []
for f in glob.glob(apacheDir + "*.conf"):
    confList.append(f.strip().split('\\')[1])

if("httpd-" + projectDetails(project)[0] + ".conf" in confList):
    for item in existingProjects:
        if("httpd-" + item + ".conf" in confList):
            if(item == projectDetails(project)[0]):
                continue;
            else:
                os.remove(apacheDir + "httpd.conf")
                #print(apacheDir + "httpd-" + item + ".conf")
                shutil.copyfile(apacheDir + "httpd-" + projectDetails(project)[0] + ".conf", apacheDir + "httpd.conf")
                #print(apacheDir + "httpd-" + projectDetails(project)[0] + ".conf")
                print("\n\t\tConf file intiated succesfully...")
                break;
                
        else:
            print("\n\t\tNo CONF file assosate with the " + item + " project")
else:
    print("\n\t\tNo CONF file assosate with the current selected project")

subprocess.Popen(['C:/xampp/xampp-control.exe'])
print("\n\t\tXampp control panel opened...")
os.system("code " + xamppDir + "htdocs/" + projectDetails(project)[0])
print("\n\t\tProject code base opened...")
os.system("start cmd /K cd " + xamppDir + "htdocs/" + projectDetails(project)[0])
print("\n\t\tTerminal opened...")

url = 'http://localhost'
if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)
    
print("\n\t\tBrowser Ready...")
time.sleep(1)
print("\n\t\tHooray! Good to Go", end="")
for i in range(0,4):
    time.sleep(1)
    print(".", end="")


time.sleep(2)

exit()























print()
