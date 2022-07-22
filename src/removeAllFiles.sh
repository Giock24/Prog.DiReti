#!/bin/bash
cd ../

if [[ `ls client/myFiles/*File* | wc -l` -gt 0 ]]; then
	rm client/myFiles/*File*
fi 2> /dev/null

if [[ `ls client/download/*File* | wc -l` -gt 0 ]]; then
	rm client/download/*File*
fi 2> /dev/null

if [[ `ls server/serverStorage/*File* | wc -l` -gt 0 ]]; then
	rm server/serverStorage/*File*
fi 2> /dev/null

