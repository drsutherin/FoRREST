#!/bin/bash

htmldir=html
stringtofind1="_static"
stringtofind2="_sources"
stringreplace1="static"
stringreplace2="sources"

cd $htmldir

mv _static static
mv _sources sources

for f in *.html
do
	echo "Processing $f"
    rpl $stringtofind1 $stringreplace1 $f
    rpl $stringtofind2 $stringreplace2 $f
done
