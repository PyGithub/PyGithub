#!/bin/sh

cp -r *.md doc COPYING* github

python setup.py sdist

rm -rf github/*.md github/doc github/COPYING*

echo "Type 'yes' if everything is right and you want to publish the package"
read yes
if [ "x$yes" == "xyes" ]
then
    python setup.py upload
fi
