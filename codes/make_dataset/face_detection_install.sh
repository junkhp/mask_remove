#!/bin/sh
apt-get update
apt-get install libboost-all-dev -y
apt-get install -y cmake
apt-get install -y build-essential
apt-get install -y libx11-dev
apt-get install -y libopenblas-dev liblapack-dev
apt-get install -y libgl1-mesa-dev

pip install dlib
pip install imutils

pip install opencv-python