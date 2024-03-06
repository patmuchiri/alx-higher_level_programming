#!/bin/bash
# sends a request to a URL and only displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
