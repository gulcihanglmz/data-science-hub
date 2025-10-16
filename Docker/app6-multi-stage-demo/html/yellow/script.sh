#!/bin/sh
rm index.html;sed -e s/USER/"$USER"/ temp.html > index1.html; sed -e s/HOSTNAME/"$HOSTNAME"/ index1.html > index.html ; nginx -g 'daemon off;'