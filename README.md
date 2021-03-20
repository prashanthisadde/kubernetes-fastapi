## Steps:
```bash
git clone https://github.com/PSsudo/prashanthi_k8s.git
cd prashanthi_k8s
helm install datak ./products_helm
minikube service fastapi-svc
```

- <code>minikube service fastapi-svc </code> will expose the service running inside the minikude to localhost
- port details will be displayed on the terminal console
- The REST endpoint will be accessible in the browser
- Go to ENDPOINT/docs to get the swagger format of the rest API
- Use the "Try it out" button to test the application


