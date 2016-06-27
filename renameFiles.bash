#!/bin/bash

htmldir=html=
stringtofind2="_sources"
stringreplace2="sources"

cd $htmldir

mv _static static
mv _sources sources

for f in *.html
do
	echo "Processing $f"
    rpl $stringtofind2 $stringreplace2 $f
done
