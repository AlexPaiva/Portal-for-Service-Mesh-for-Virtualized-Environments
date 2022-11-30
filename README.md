# Portal-for-Service-Mesh-for-Virtualized-Environments

Descrição Aqui

Check Notion.so para updates!!

Passo 1 - Criar K8s master e workers com scripts baseados em Vermin (single binary: https://github.com/mhewedy/vermin), pegar no master.sh e worker.sh e editar

Passo 2 - Instalar ISTIO, usei https://makeoptim.com/en/service-mesh/kubeadm-kubernetes-istio-setup#installing-kubeadm-kubelet-and-kubectl-for-every-node que instala kubeadm também embora instale também METALLB, é um 'barebones' load balancer para as K8s o que é um + (MAS está em beta portanto se algo der erro tentar sem METALLB!)

Passo 3 - A criação de outro cluster (repetir passos 1 e 2)

Passo 4 - Instalar ADMIRAL https://github.com/istio-ecosystem/admiral/ Aqui no exemplo da documentação do admiral: https://github.com/istio-ecosystem/admiral/blob/master/docs/Examples.md vêm (obviously) um exemplo para ajudar a implementar

--

Acabar front-end flask site para estar ready para o api server e front-end (north bound/side do Admiral)
Fazer um website basic em git pages para o professor ter o website de projeto que pede
