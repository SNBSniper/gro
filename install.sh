#bin/bash

mkdir vendor
sudo apt-get update
sudo apt-get install build-essential python-dev git python3-rpi.gpio
sudo apt-get install gpsd gpsd-clients

git clone https://github.com/adafruit/Adafruit_Python_PN532.git vendor/PN532
git clone https://github.com/lamondlab/IteadSIM800.git vendor/IteadSIM800
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

sudo apt-get install nodejs -y

npm install serialport
npm install gps
npm install express
npm install requestify
npm install request

sudo pip3 install pyserial
cd vendor/PN532
sudo python setup.py install
