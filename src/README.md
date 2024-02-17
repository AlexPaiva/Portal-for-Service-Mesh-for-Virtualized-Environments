# Portal and Factories Cluster Setup Guide

This guide details the steps to set up the Portal 'Main' cluster (the only one with ISTIO) and a Factories cluster. Follow these instructions carefully to ensure successful deployment.

## Portal 'Main' Cluster Setup

### Step 0: Create Portal 'Main' Cluster (with ISTIO)
- **0.1** Change directory to `Cluster_1` folder in your terminal.
- **0.2** Deploy the KIND cluster using the command below:
  ```bash
  kind create cluster --config kind-config-portal.yaml --name portal-cluster
  ```
- **0.3** Deploy ISTIO (Ensure ISTIO is installed and properly configured in your PATH):
  ```bash
  kubectl config use-context kind-portal-cluster
  istioctl install --set profile=demo -y
  ```
- **0.4** Enable ISTIO sidecar injection:
  ```bash
  kubectl label namespace default istio-injection=enabled
  ```
- **0.5** Build the Docker image (First, change directory to the `.py` file's folder):
  ```bash
  docker build -t flask-portal-image .
  ```
- **0.6** Load the image into the cluster:
  ```bash
  kind load docker-image flask-portal-image --name portal-cluster
  ```
- **0.7** Deploy!
  Set the current context to portal-cluster and deploy the portal and Istio configuration:
  ```bash
  kubectl config use-context kind-portal-cluster
  kubectl apply -f portal-deployment.yaml
  kubectl apply -f istio-config.yaml
  ```
- **0.8** Retrieve the Portal's IP for the factories to connect:
  ```bash
  kubectl get services portal-service -o=jsonpath='{.spec.clusterIP}'
  ```
  Copy the Portal's IP obtained and paste it into `portal_api_ip.txt` in the factories cluster folder.
- **0.9** Proceed to the Factories cluster setup.

### Step 1: Create Factories Cluster
- **1.1** Create the factories cluster:
  ```bash
  kind create cluster --config kind-config-factory.yaml --name factory-cluster
  ```
- **1.2** Build the Docker image (First, change directory to the `.py` file's folder):
  ```bash
  docker build -t factory-image .
  ```
- **1.3** Load the Docker image into the cluster:
  ```bash
  kind load docker-image factory-image --name factory-cluster
  ```
- **1.4** Deploy!
  Set the current context to factory-cluster and deploy the factories:
  ```bash
  kubectl config use-context kind-factory-cluster
  kubectl apply -f factory-deployment.yaml
  ```

### Step 2: Verify Proper Operation
- **2.1** In the Portal Cluster:
  ```bash
  kubectl config use-context kind-portal-cluster
  kubectl get deployments
  kubectl get services
  kubectl get pods
  ```
- **2.2** In the Factories Cluster:
  ```bash
  kubectl config use-context kind-factory-cluster
  kubectl get deployments
  kubectl get services
  kubectl get pods
  ```

### Step 3: Accessing the Portal
- **3.1** In the terminal of the portal cluster, run the following to obtain the NodePort:
  ```bash
  kubectl get service istio-ingressgateway -n istio-system -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}'
  ```
- **3.2** Access the portal via `http://localhost:<NodePort>`, replacing `<NodePort>` with the port obtained in the previous step.