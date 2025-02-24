## This project was made watching https://www.youtube.com/watch?v=XltFOyGanYE&ab_channel=DevOpsDirective

FastApi: https://fastapi.tiangolo.com/tutorial/first-steps/

kubectl and minikube

### Kubernetes commands:
```bash 
minikube start
````

### Apply changes
```bash 
kubectl apply -f k8s
````

### Check the pods are being created
```bash 
kubectl get pods
kubectl get pods -W # to watch the pods
```

### get service url
```bash 
minukube service list
````

### make sure of the service name to use it with below command
```bash 
minikube service <service-name> --url
````

## Local development

### Run the app in dev mode:
```bash
fastapi dev app/main.py
```

