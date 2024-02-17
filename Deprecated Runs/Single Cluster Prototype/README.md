# Project Setup Instructions

This guide provides step-by-step instructions for setting up the project environment (single cluster only) using Kind ([Kubernetes in Docker](https://kind.sigs.k8s.io "KIND Homepage")), ([Docker](https://www.docker.com "Docker Homepage")), and ([Istio](https://istio.io "Istio Homepage")).

## Prerequisites

- Docker
- Kind
- kubectl
- Access to a terminal/command prompt

## 0. Create Kind Cluster

To create a Kind cluster, navigate to the directory containing the `kind-config.yaml` file and run:

```bash
kind create cluster --config kind-config.yaml
```

## ISTIO Installation

1. Access the master node:

```bash
sudo docker exec -it kind-control-plane /bin/bash
```

2. Install Istio inside the node:

```bash
curl -L https://istio.io/downloadIstio | sh -
export PATH="$PATH:/istio-1.17.1/bin"
istioctl install --set profile=default
```

## 1. Create Docker Image for Portal

This step is required only once before pushing the image to the repository.

In the directory of `app.py`, run:

```bash
docker build -t flask-portal-image .
```

**Note:** Pay attention to the period at the end of the command.

After running this command, you will have a Docker image named `flask-portal-image` for the Flask Portal.

## 2. Create Docker Image for Factory

This step is required only once before pushing the image to the repository.

In the directory of `factory_app.py`, run:

```bash
docker build -t factory-image1 .
```

**Note:** Pay attention to the period at the end of the command.

After running this command, you will have a Docker image named `factory-image1` for the Factory App.

To create `factory-image2`, repeat the steps, changing `1` to `2`.

## 3. Load Docker Images to the Kind Cluster

**Option 1:** If not using a repository, load images directly into Kind.

- For the Portal, navigate to the Portal directory and run:

```bash
kind load docker-image flask-portal-image
```

- For the Factory, navigate to the Factory directory and run:

```bash
kind load docker-image factory-image1
```

**Option 2:** Push created images to a repository (required only once).

```bash
docker login
docker tag <image-name> <username>/<repository_name>:<image_tag>
docker push <username>/<repository_name>:<image_tag>
```

Repeat the steps for factory images.

**Important:** Whenever there are changes in the factory or portal app, repeat from step 2 to update the image. To verify changes, use:

```bash
kubectl exec -it <pod-name> -- /bin/bash
```

## 4. Deploy Using YAML Files

- For the Portal, navigate to the Portal directory and run:

```bash
kubectl apply -f portal-deployment.yaml
```

- For the Factory, navigate to the Factory directory and run:

```bash
kubectl apply -f factory-deployment.yaml
```

## 5. Start the Portal

Since the portal is of type 'NodePort', it can be accessed on a specific port. Find the 'NodePort' value by running:

```bash
kubectl get services portal-service
```

Note the 'NodePort' value in the format "80:<NodePort>". Allow traffic on this port by running:

```bash
ufw allow <NodePort>
```

To find the IP of the node containing the Portal:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <node-name>
```

or

```bash
sudo kubectl get nodes -o wide
```

## 6. Verify Everything is Connected and Working

Before accessing the portal to avoid corrupt data, ensure everything is set up correctly:

1. **Check Cluster State:** Ensure the Kind cluster is running and all worker nodes are 'Ready' using:

```bash
kubectl get nodes
```

2. **Check Service Status:** Use `kubectl get deployments` to see if the Flask portal and factories are properly deployed without errors.

3. **Check Service State:** Use `kubectl get services` to verify that services are running with valid ClusterIPs and ports are correctly exposed.

4. **Check Logs:** For the Flask Portal and factory applications, use `kubectl logs <pod-name>` to check for errors or issues.

## 7. Accessing the Flask Portal

To access the portal, open a browser and navigate to `http://<Node_IP>:<NodePort>`. Log in with one of the following credentials:

- `factoryManager:password` (Displays a table of both factories updating every 10 seconds)
- `factory1:password` (Same as above but for factory 1 only)
- `factory2:password` (Same as above but for factory 2 only)

Done! :)