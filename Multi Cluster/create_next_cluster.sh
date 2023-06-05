#!/bin/bash

CLUSTERS_DIR="../Multi Cluster"
NEXT_CLUSTER=$(find "$CLUSTERS_DIR" -type d -name "Cluster *" | wc -l)
NEXT_CLUSTER=$((NEXT_CLUSTER + 1))
NEXT_CLUSTER_DIR="$CLUSTERS_DIR/Cluster $NEXT_CLUSTER"

cp -R "Cluster 2" "$NEXT_CLUSTER_DIR"
cd "$NEXT_CLUSTER_DIR"

sudo kind create cluster --config kind-config-factory.yaml --name factory-cluster"$NEXT_CLUSTER"
sudo kubectl config use-context kind-factory-cluster"$NEXT_CLUSTER"
sudo istioctl install --set profile=demo -y
sudo kubectl label namespace default istio-injection=enabled
cd Factory
sudo kubectl config use-context kind-factory-cluster"$NEXT_CLUSTER"

sudo kubectl config use-context kind-factory-cluster
sudo docker build -t factory1-deployment-cluster2 .
sudo docker tag factory1-deployment-cluster2 istsmerafarlho/projpeci:factory1-deployment-cluster2
sudo docker push istsmerafarlho/projpeci:factory1-deployment-cluster2
sudo kubectl apply -f factory1-deployment-cluster2.yaml

sudo docker build -t factory2-deployment-cluster2 .
sudo docker tag factory2-deployment-cluster2 istsmerafarlho/projpeci:factory2-deployment-cluster2
sudo docker push istsmerafarlho/projpeci:factory2-deployment-cluster2
sudo kubectl apply -f factory2-deployment-cluster2.yaml


