#bin/bash

mkdir vendor
sudo apt-get update
sudo apt-get install build-essential python-dev git python3-rpi.gpio
sudo apt-get install gpsd gpsd-clients

git clone https://github.com/adafruit/Adafruit_Python_PN532.git vendor/PN532
git clone https://github.com/lamondlab/IteadSIM800.git vendor/IteadSIM800
https://github.com/gilbitron/Cardash.git vendor/cardDash

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -

sudo pip3 install pyserial
sudo pip3 install geopy

cd vendor/PN532
sudo python setup.py install
