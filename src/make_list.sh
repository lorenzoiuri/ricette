#!/bin/bash

# puts content in recipes.tex

echo "\chapterstyle{"$1"}" > recipes.tex
echo "" >> recipes.tex

for filename in content/$1/*.tex; do
    echo "\input{"$filename"}" >> recipes.tex
done