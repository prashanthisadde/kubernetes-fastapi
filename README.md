## Run the application:
```bash
git clone https://github.com/pssudo/kubernetes-fastapi.git
cd kubernetes-fastapi
```

### Deploy using Helm
```bash
helm install products ./products_helm
```

### Deploy using kubectl
```bash
kubectl apply -f products_k8s_manifest.yaml
```
### Access the application
```bash
minikube service fastapi-svc
minikube addons enable metrics-server
```

## Explaination & Steps to follow

- <code>minikube service fastapi-svc </code> will expose the service running inside the minikude to localhost
- port details will be displayed on the terminal console
- The REST endpoint will be accessible in the browser
- Go to ENDPOINT/docs to get the swagger format of the rest API
- Use the "Try it out" button to test the application
- Use POST and GET methods as per the swagger documentation
- Once new records are created using POST method run the below command to test the load
    ```bash
    for i in {1..1000}; do curl -s http://127.0.0.1:63538/products/1234 > /dev/null; done
    ```
:::note
- Please change the port number from 63538 to the one which is running in your local
- Change the product id from 1234 to the value you have passed as p_id
:::

## Auto Scaling

- While the above load test is running, you can observe the scaling policy (Up & Down are configured on CPU Utilization) using
```bash
kubectl describe hpa fastapi-hpa
```
- Alternatively you can enable the dashboard addon and observe the events
```bash
minikube addons enable dashboard
minikube dashboard
```
