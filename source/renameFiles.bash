#!/bin/bash

htmldir=$1
stringtofind1="_static"
stringtofind2="_sources"
stringreplace1="html/static"
stringreplace2="html/sources"

cd $htmldir

mv _static static
mv _sources sources

for f in *.html
do
	echo "Processing $f"
    rpl $stringtofind1 $stringreplace1 $f
    rpl $stringtofind1 $stringreplace1 $f
done
