echo '[+] Installing Dependencies...'
pkg update
pkg upgrade
echo '[!]Python'
pkg install python
echo '[!]PHP'
pkg install php
echo '[!]wget'
pkg install wget 
echo '[!]unzip'
pkg install unzip 
echo '[!]openssh'
pkg install ssh 
echo '[+]Requests'
pip install requests 
echo '[+] Installed.'
