#!/bin/bash

for i in "/home/pedro913/Desktop/pageRank/program/tests"/* 
do
	f="$i"
	file="$(basename -- $f)"
	mkdir "results/$file"
	python3 program_txt.py < "$i"
done
