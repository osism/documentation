#!/usr/bin/env bash

rm -rf build/html/.buildinfo build/html/.doctrees build/html/_sources
lftp -u "$FTP_USERNAME,$FTP_PASSWORD" -e "set ftp:ssl-allow no; mirror -R --delete build/html osism; exit;" ftp://betacloud.io
