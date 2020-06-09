#!/usr/bin/env bash

rm -r dist

python setup.py sdist

cp dist/geo_calculator*.tar.gz dist/geo_calculator.tar.gz

sudo pip3 install dist/geo_calculator.tar.gz

cd test || exit

python3 -m unittest geo_calculator_test.py

cd ..
