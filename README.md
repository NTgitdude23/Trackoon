# Trackoon



<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
	

Trackoon is hosting fake websites on **PHP Servers** and uses **Serveo** for tunneling. The website asks for Location Permission, if the user allows it we get:

* Longitude
* Latitude
* Accuracy
* Altitude - Not always available
* Direction - Only available if user is moving
* Speed - Only available if user is moving

Along with Location Information we also get **Device Information**:

* Operating System
* Platform
* Number of CPU Cores
* Amount of RAM - Approximate Results
* Screen Resolution
* GPU information
* Browser Name and Version
* Public IP Address

**This tool is a Proof of Concept and is for Educational Purposes Only, Trackoon shows what data a malicious website can gather about you and your devices and why you should not click on random links and allow critical permissions such as Location etc.**


**Other tools and services offer IP Geolocation which is not very accurate and does not give the exact location of the user. This tool does it! :D**

## Tested On :

* Kali Linux 2018.2
* Ubuntu 18.04
* Arch Linux based Distro
* Termux
* Kali Linux (WSL)
* Parrot OS
* Zorin OS
* Mac OS High Sierra

## Installation


 **WARNING!! Before installation CHECK to see if you have the Dependencies ALREADY INSTALLED! If you install the same Dependency again you may break it! (Mostly on MAC)**
 
 CHECK YOUR STUFF (MAC) :
 ``
 Homebrew
 brew
 wget
 php
 python3
 unzip
 openssh
 python3-requests ( pip3 install requests )
 ``
 If you already have these DO NOT RUN macinstall.sh.
 Your mac may overwrite them!
 


### Ubuntu/Kali Linux

```
git clone https://github.com/KnightSec-Official/Trackoon.git
cd Trackoon/
chmod 777 install.sh
./install.sh
```


### Mac OS

```
git clone https://github.com/KnightSec-Official/Trackoon.git
cd Trackoon/
chmod 777 macinstall.sh
./macinstall.sh
```


### Termux

```
git clone https://github.com/KnightSec-Official/Trackoon.git
cd Trackoon/
chmod 777 termuxinstall.sh
./termuxinstall.sh
```
## Running
``
python3 Trackoon.py
``

#######

**This repo has been inspired by the tool called Seeker made by thewhiteh4t! Some of the code has been copyied from Seeker.py!**

#######

***TO DO***
* Add more phishing pages
* Set webserver tunneling via Ngrok and Custom Serveo
* Make it a Spear Phishing Doxxing tool
* Make it a Phishing 0-Day xD

```
####################################################	
#  Trackoon made and lit up by  <>,.,Knigtsec,.,<> #
#						   #
#						   #
# Instagram: @knightsec_		           #
# Github: KnightSec-Official                       #
# Youtube:                                         #
# www.youtube.com/channel/UCG3kQUplyR1ktq702VpWFQg #
#                                                  #
#                                                  #
#  More repositories soon :D			   #
#						   #
#						   #
#						   #
####################################################			  
			  	        ⟋﹈﹈⟍
			   	       ⎠    ⟋⎪⟍
			      		  ⟋⎪⎛⎪⎞⎪⟍
			    		⟋⎪⸦⎪⎝⎪⎠⎪⸧⎪⟍
			   	       ⟍____⟋⟍____⟋
			  	      ⟋    〜^〜     ⟍
 			 	      ⟍    ▔▔▔▔▔    ⟋
			    		⟍    ⧱    ⟋
			      		  ⟍__⧱__⟋
				     		*Knightsec* 1.1.5
							{{<O>}}
```
              
