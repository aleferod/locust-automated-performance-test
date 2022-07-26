# Locust Automated Performance Test
Automated performance test using Locust (https://locust.io/), Python and Docker


# Setup

Configure the host in **docker-compose.yml**

```
    command: -f /mnt/locust/locustfile.py --master -H {host_to_test}
```
Create the http requests to load and stress test using python in **locustfile.py** file


# Run 

$ docker-compose up -d


# Access the dashboard 

http://localhost:8089 

# Load Test setup

![Load Test Setup](/assets/images/locust-setup-load-test.png)


```
   Number of Users = Concurrent users (Number of Threads)
   Spawn rate = Number of users to start every second util it fulfils the total number of users to simulate
```

# Load Test Summary

![Load Test Summary](/assets/images/locust-load-test-summary.png)


See more in https://docs.locust.io/en/stable/
