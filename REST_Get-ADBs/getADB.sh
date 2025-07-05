#!/bin/bash

########################## Fill these in with your values ##########################
#OCID of the tenancy calls are being made in to
tenancy_ocid="[change]"

# OCID of the user making the rest call
user_ocid="[change]"

# path to the private PEM format key for this user
privateKeyPath="[change]"

# fingerprint of the private key for this user
fingerprint="[change]"

# The REST api you want to call, with any required paramters.
rest_api="/20160918/autonomousDatabases?compartmentId=[change - put your compartment id]"

# The host you want to make the call against
host="database.us-ashburn-1.oraclecloud.com [change]"
####################################################################################


date=`date -u "+%a, %d %h %Y %H:%M:%S GMT"`
date_header="date: $date"
host_header="host: $host"
request_target="(request-target): get $rest_api"
# note the order of items. The order in the signing_string matches the order in the headers
signing_string="$request_target\n$date_header\n$host_header"
headers="(request-target) date host"


echo "====================================================================================================="
printf '%b' "signing string is $signing_string \n"
signature=`printf '%b' "$signing_string" | openssl dgst -sha256 -sign $privateKeyPath | openssl enc -e -base64 | tr -d '\n'`
printf '%b' "Signed Request is  \n$signature\n"

echo "====================================================================================================="
set -x
curl -v -X GET -sS https://$host$rest_api -H "date: $date" -H "Authorization: Signature version=\"1\",keyId=\"$tenancy_ocid/$user_ocid/$fingerprint\",algorithm=\"rsa-sha256\",headers=\"$headers\",signature=\"$signature\"" 
