#!/bin/bash
# takes in a URL and display all HTTP methods the server will accept.
curl -Is "$1" | grep Allow | cut -c 8-
