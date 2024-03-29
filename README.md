# Portal for Service Mesh in Virtualized Environments

## Overview
This portal was designed as a cutting-edge solution to streamline the integration, management, and operational oversight of Kubernetes clusters, leveraging the Istio service mesh in a multi-cluster setup. Rooted in the context of industry 4.0, our project simulates a global network of factories, each represented by a Kubernetes cluster. These factories, through our portal, report real-time data on production processes, integrating seamlessly with a central Flask web portal. This setup not only showcases the potential for microservice architecture in industrial applications but also demonstrates a sophisticated use of technology to enhance operational efficiency and global management. Our portal, aimed at simplifying Kubernetes' complexities, offers layered access tailored to various user expertise levels, making it a pivotal tool for educational and development purposes in cloud-native technologies.

**Note**: As of August 2023, this project is no longer under active maintenance.

## Features
- **Simplified Kubernetes Management**: Facilitates the management of Kubernetes clusters, making advanced operations accessible.
- **Multi-Cluster Management**: Enables oversight across multiple Kubernetes clusters from a singular interface.
- **Istio Service Mesh Integration**: Employs Istio for advanced network functionalities, enhancing traffic management, security, and observability.
- **Real-Time Data Simulation**: Simulates real-time data reporting from multiple clusters, representing a network of factories.

## System Requirements
- [Docker](https://www.docker.com "Docker Homepage")
- [Kubernetes](https://kubernetes.io/ "Kubernetes Homepage")
- [KIND (Kubernetes in Docker)](https://kind.sigs.k8s.io "KIND Homepage")
- [Istio](https://istio.io "Istio Homepage")

## Installation and Setup
1. **Prerequisites**: Ensure Docker, Kubernetes, KIND and Istio are installed.
2. **Deployment**:
   - Clone the repository.
   - Follow the setup instructions within the `src` directory [README.md](../main/src/README.md) file for current deployment guidelines. All other deployment files are deprecated.
3. **Accessing the Portal**:
   - The portal is accessible via `http://localhost:<PORT>`, with `PORT` being the deployment-specific port.

## Documentation
For an in-depth understanding, please refer to the supplementary [PDF report](../main/Report.pdf), which provides detailed documentation on our project's objectives, architecture, and implementation nuances.

## Deprecated Versions
- [Vagrant Single Cluster Prototype (Deprecated Feb 23, 2023)](../main/deprecated-runs/vagrant-single-cluster-prototype/README.md)
This guide provides step-by-step instructions for setting up the project environment (single cluster only) using ([Vagrant](https://www.vagrantup.com "Vagrant Homepage")) and ([Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/ "Kubeadm Documentation")).

- [Single Cluster Prototype (Deprecated March 29, 2023)](../main/deprecated-runs/single-cluster-prototype/README.md)
This guide provides step-by-step instructions for setting up the project environment (single cluster only) using Kind ([Kubernetes in Docker](https://kind.sigs.k8s.io "KIND Homepage")), ([Docker](https://www.docker.com "Docker Homepage")), and ([Istio](https://istio.io "Istio Homepage")).

## Acknowledgments
Thanks to the students and faculty of Universidade de Aveiro for their collaboration and insights into creating this innovative project.

## License
This project is licensed under the MIT License - see the [LICENSE](../main/LICENSE) file for details.
