#!/bin/bash
url="google.com"
if ping -c 1 "$url" > /dev/null; then
  echo "$url is up"
else
  echo "$url is down"
fi