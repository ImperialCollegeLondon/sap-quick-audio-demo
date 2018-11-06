# script to generate and display an audio demo
# requies one input parameter - path to folder of files
# optional second parameter give the demo a name
# TODO: specify csv file as input to specify subset of files
# TODO: rewrite using pure python for cross-platform compatability using py-docker bindings https://docker-py.readthedocs.io/en/1.2.0/api/
#
# see https://www.katacoda.com/courses/docker/create-nginx-static-web-server for easy overview of Docker
# basic steps
# - Clone template files from git
# - Create webpage called index.html inside html subdirectory
# - Build new image based on html subdirectory
# - Run the image
# - Open the running site in browser

# clone repository to create staging area with dependencies
# TODO: use submodule to get latest version of trackswitch.js
echo Number of inputs $#
if [ $# -lt 1 ]
then
    echo Must specify input directory
    exit
fi

SOURCE=$1
if [ $# -gt 1 ]
then
    NAME=$2
else
    NAME='Audio Demo'
fi
echo Making $NAME from $SOURCE

# simple test is to copy html file directly
#cp indexTemplate.html html/index.html

#python make_html.py --source=${SOURCE} --name=${NAME}
python make_html.py "${SOURCE}" "${NAME}"

docker build -t webserver-image:v1 .
docker run -d -p 80:80 --rm --name audio-demo webserver-image:v1 

python -m webbrowser -t "http://localhost"