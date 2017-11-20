#bin/bash

mkdir vendor
sudo apt-get update
sudo apt-get install build-essential python-dev git python3-rpi.gpio

git clone https://github.com/adafruit/Adafruit_Python_PN532.git vendor/PN532
git clone https://github.com/lamondlab/IteadSIM800.git vendor/IteadSIM800

sudo pip3 install pyserial
cd vendor/PN532
sudo python setup.py install