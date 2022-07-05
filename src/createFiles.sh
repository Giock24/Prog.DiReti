#!/bin/bash

cd ../

for ((i = 0 ; i < 5; i= $i+1)) do

	cd server/serverStorage/
	touch serverFile$i.txt
	echo "Hello World $i" > ./serverFile$i.txt
	
	cd ../../
	
	cd client/myFiles/
	touch clientFile$i.txt
	echo "Hello World $i" > ./clientFile$i.txt
	
	cd ../../

done

