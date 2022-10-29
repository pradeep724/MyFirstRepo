#!/bin/bash
sed 1d harish.csv | while read -r line; do
    formatted_line=$(echo $line | sed 's/,/ /g')
    os_type=$(echo $formatted_line | awk '{print $7}')
    if [ "$os_type" == 'Linux' ]; then
        server_name=$(echo $formatted_line | awk '{print $1}')
        echo $server_name >> linux_server.list
    fi
done

for serv in $(cat linux_server.list); do
    echo $serv
done
