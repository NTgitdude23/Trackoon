

echo '[+] Installing Dependencies...'
echo '    Python'
apt-get -y install python3
echo '    PHP'
apt-get -y install php
echo '    wget'
apt-get -y install wget 
echo '    unzip'
apt-get -y install unzip 
echo '    openssh'
apt-get -y install ssh 
echo '    Requests'
pip3 install requests 

echo '[+] Installed.'