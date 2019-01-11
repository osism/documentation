#!/usr/bin/env bash

rm -rf build/html/.buildinfo build/html/.doctrees
lftp -u "$FTP_USERNAME,$FTP_PASSWORD" -e "set ssl:verify-certificate false; mirror -v -R --delete build/html osism; exit;" ftp://betacloud.io
