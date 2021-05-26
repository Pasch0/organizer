#!/bin/bash

echo "alias stop='touch ~/Downloads/stop'" >> ~/.bashrc;

echo "alias organizer='rm ~/Downloads/stop & nohup python3 /usr/bin/organizer.py & disown ; rm nohup.out & rm ~/Downloads/nohup.out & clear'" >> ~/.bashrc;

exec bash
