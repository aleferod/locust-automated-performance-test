from locust import HttpUser, between, task, events
import os 

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def googleTest(self):
        self.client.get("/")






