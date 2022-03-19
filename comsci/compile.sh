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
       pdflatex -shell-escape $1
       pdflatex -shell-escape $1
       echo ""
       echo "DONE!"
       echo ""
       LTIME=$ATIME
   fi
   sleep 5
done
