#!/usr/bin/env bash

cat ~/.bashrc | grep -v 'stop' > ~/.bashrc_organizer;

cat ~/.bashrc_organizer |grep -v 'stop' > ~/.bashrc;

rm /usr/bin/organizer.py;

exec bash
