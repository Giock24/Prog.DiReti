#!/bin/bash
cd ../

if [[ `ls client/myFiles/ | wc -l` -gt 0 ]]; then
	rm client/myFiles/*
fi

if [[ `ls client/download/ | wc -l` -gt 0 ]]; then
	rm client/download/*
fi

if [[ `ls server/serverStorage/ | wc -l` -gt 0 ]]; then
	rm server/serverStorage/*
fi 

