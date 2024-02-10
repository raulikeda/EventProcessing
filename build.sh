#! /usr/bin/bash
rm ./dist/*
python3 setup.py pytest
python3 setup.py bdist_wheel
python3 -m twine upload dist/*
