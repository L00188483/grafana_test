#!/bin/bash

echo -e "\nRemoving: \n"

docker rm -f prometheus
docker rm -f grafana
docker rm -f webapp

docker image rm grafana_test-webapp

docker volume rm -f grafana_test_grafana-storage
docker volume rm -f grafana_test_prometheus-storage
