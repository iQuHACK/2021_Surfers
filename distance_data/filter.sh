#!/bin/env bash

unzip -p sf12010countydistancemiles.csv.zip | egrep '^"23.*,"23\d{3}*' >maine_dist.txt
unzip -p sf12010countydistancemiles.csv.zip | egrep '^"50.*,"50\d{3}*' >vermont_dist.txt
