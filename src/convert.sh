
#!/bin/bash

# applies template_to_tex.py to every file in recipes/<mode>/<course>/
# $1 is <course> : primi/secondi/dolci/antipasti
# $2 is <mode> : old/new

# if the mode argument is missing, assume is "old"
if [ $# -eq 1 ]
  then 
    mode="old"
  else 
    mode=$2
fi


for filename in recipes/$mode/$1/*.txt; do
    basename=`basename $filename .txt`
    python3 src/template_to_tex.py $filename > content/$1/$basename.tex
done
