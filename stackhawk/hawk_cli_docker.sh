#!/bin/bash


# get an API key from: https://app.stackhawk.com/settings/apikeys
API_KEY="XXXXXX"

if [ "$API_KEY" == "XXXXXX" ]; then
   echo "API_KEY not set"
   exit 1
fi

# copy yaml from your current directory into ~/.hawk
cp stackhawk-juiceshop.yml /home/vboxuser/.hawk/stackhawk.yml

docker run -e API_KEY=$API_KEY --rm -v /home/vboxuser/.hawk:/hawk:rw -it stackhawk/hawkscan:latest



