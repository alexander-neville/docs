#!/bin/bash

### Set initial time of file
LTIME=`stat -c %Z $1`
echo "hello"

while true    
do
   ATIME=`stat -c %Z $1`

   if [[ "$ATIME" != "$LTIME" ]]
   then    
       echo "RECOMPILING ..."
       pdflatex index.tex
       LTIME=$ATIME
   fi
   sleep 5
done
