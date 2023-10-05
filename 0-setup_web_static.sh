#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

apt update

apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

printf "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHello World!\n\t</body>\n</html>\n" | 
tee /data/web_static/releases/test/index.html 

ln -fs /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

loc_header="location \/hbnb\_static\/ {"
loc_content="alias \/data\/web\_static\/current\/;"
loc1="\n\t$loc_header\n\t\t$loc_content\n\t}\n"
sed -i "37s/$/$loc1/" /etc/nginx/sites-available/default

service nginx restart
