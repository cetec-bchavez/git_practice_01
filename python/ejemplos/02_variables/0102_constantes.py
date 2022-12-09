#!/usr/bin/env python

#Python doesn’t support constants or non-reassignable names.

PORT_DB_SERVER= 3307   #int(),:int 
USER_DB_SERVER = "root" #str(),:str
PASSWORD_DB_SERVER = "123456"   #str(),:str
DB_NAME = "nomina"  #str(),:str
IP_DB_SERVER ="localhost"   #str(),:str


print ("scp -v -P {0} {1}@{2}:/{3}/{4}/{4}.sql /srv/backup".format(
    str(PORT_DB_SERVER), USER_DB_SERVER, IP_DB_SERVER, USER_DB_SERVER,DB_NAME))


IP_DB_SERVER="127.0"