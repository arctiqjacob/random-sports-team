# Random Sports Team
Demo Python application showing random sports teams. The sport is controlled by the `SPORT` environment variable. Defaults to `NHL` if no environment variable is set.

![application](images/application.png "Application")
![application2](images/application2.png "Application2")

## How to Build
```shell
$ docker build --tag random-sports-team .

$ docker tag random-sports-team jacobmammoliti/random-sports-team

$ docker push jacobmammoliti/random-sports-team
```

## Deploy into Kubernetes
```shell
$ kubectl create deployment random-sports-team --image=jacobmammoliti/random-sports-team

$ kubectl expose deployment random-sports-team --port 8080

$ kubectl port-forward svc/random-sports-team 8080:
```