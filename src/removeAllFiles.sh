#!/bin/bash
cd ../

if [[ `ls client/myFiles/ | wc -l` -gt 0 ]]; then
	rm client/myFiles/*File*
fi

if [[ `ls client/download/ | wc -l` -gt 0 ]]; then
	rm client/download/*File*
fi

if [[ `ls server/serverStorage/ | wc -l` -gt 0 ]]; then
	rm server/serverStorage/*File*
fi 

