# Locust Automated Performance Test
Automated performance test using Locust (https://locust.io/), Python and Docker


# Setup

Configure the host in **docker-compose.yml**

```
    command: -f /mnt/locust/locustfile.py --master -H **{host_to_test}**
```
Create the http requests to load and stress test using python in **locustfile.py** file


# Run 

$ docker-compose up -d


# Access the dashboard 

http://localhost:8089 

# Load and Stress Test setup

![Load and Stress Test Setup](/assets/images/locust-setup-load-test.png)



