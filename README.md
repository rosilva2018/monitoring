# monitoring

Este projeto entrega uma solução simples de observabilidade usando:

* Grafana
* Grafana Loki
* Prometheus
* app-python

# Uso

### Build da aplicação sample (python-app)

docker tag python-app:latest <your-registry>/python-app:latest
docker push <your-registry>/python-app:latest

### Deploy

kubectl create -f (deployment.yaml)

### Acesso local

kubectl port-forward svc/prometheus 9090:9090
kubectl port-forward svc/grafana 3000:3000

### Infra

Minikube

# Dependências

* Python 3
* Minikube

# Contribuição

Se você quiser contribuir com este projeto, siga as diretrizes abaixo:

* Faça um fork do repositório.
* Crie uma branch para a sua feature (git checkout -b minha-feature).
* Commit suas alterações (git commit -m 'Adiciona uma nova feature').
* Faça o push para a branch (git push origin minha-feature).
* Abra um Pull Request.

# Contato

Para dúvidas ou sugestões, entre em contato:

https://www.linkedin.com/in/rog%C3%A9rio-carvalho-870436208/
