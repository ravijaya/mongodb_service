#!/bin/bash 

function check_for_empty {
    if [[ -z $2 ]]; then
	echo "$0: $1: input cannot be empty"
        exit 2
    fi	
}

function check_for_fqdn {
    echo $2 | grep -Pq '(?=^.{1,254}$)(^(?>(?!\d+\.)[a-zA-Z0-9_\-]{1,63}\.?)+(?:[a-zA-Z]{2,})$)'

    if (( $? == 1)); then
        echo "$0:$1 is not a FQDN:$2"
	exit 1
    fi
}

echo -n  'enter the server name :'
read servername 
check_for_empty ServerName $servername
# check_for_fqdn ServerName $servername 

echo -n  'enter the gateway port:'
read gatewayport
check_for_empty "Gateway Port" $servername

echo -n 'enter the MongoDB Server :'
read dbserver
check_for_empty "MongoDB Server" $dbserver
# check_for_fqdn "MongoDB Server" $dbserver

echo -n 'enter the MongoDB Port :'
read port
check_for_empty "MongoDB Port" $port

echo -n 'enter the MongoDB Username :'
read username
check_for_empty "MongoDB Username" $username

echo -n 'enter the MongoDB Password :'
read -s password
check_for_empty "MongoDB Password" $password
echo; echo

cat <<EOF > env.list
SERVERNAME=$servername
GATEWAYPORT=$gatewayport
ROOTDIR=/home/cpxroot
DATABASE=mongodb://${dbserver}:${port}/
USERNAME=$username
PASSWORD=$password
MONGODB_SERVER=$dbserver
MONGODB_PORT=$port
MONGODB_USERNAME=$username
MONGODB_PASSWORD=$password
EOF

export SERVERNAME=$servername
export GATEWAYPORT=$gatewayport
export ROOTDIR=/home/cpxroot
export DATABASE=mongodb://${dbserver}:${port}/
export USERNAME=$username
export PASSWORD=$password
export MONGODB_SERVER=$dbserver
export MONGODB_PORT=$port
export MONGODB_USERNAME=$username
export MONGODB_PASSWORD=$password

platform_api_path=platform_api

docker-compose -f mongodb/docker-compose.yml up --build -d
echo
docker-compose -f mongodb/docker-compose.yml ps
echo 

