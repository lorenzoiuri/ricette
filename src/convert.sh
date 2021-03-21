
#!/bin/bash

# applies template_to_tex.py to every file in recipes/type

for filename in recipes/$1/*.md; do
    basename=`basename $filename .md`
    python3 src/template_to_tex.py $filename > content/$1/$basename.tex
done