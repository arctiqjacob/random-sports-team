# Random Sports Team
Demo Python application showing random sports teams. The sport is controlled by the `SPORT` environment variable. Defaults to `NHL` if no environment variable is set.

![application](images/application.png "Application")
![application2](images/application2.png "Application2")

## Build with Docker
```shell
$ docker build docker build --tag jacobmammoliti/random-sports-team:<version> .
...
Successfully tagged jacobmammoliti/random-sports-team:2.0

$ docker push jacobmammoliti/random-sports-team
...
2.0: digest:...
```