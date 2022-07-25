from locust import HttpUser, between, task, events
import os 

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def getMovies(self):
        self.client.get("/restapis/" + str(os.getenv('API_GATEWAY_ID')) + "/dev/_user_request_/movies")

    @task
    def getBestMoviesRated(self):
        self.client.get("/restapis/" + str(os.getenv('API_GATEWAY_ID')) + "/dev/_user_request_/best-movies-rated")
    
    @task
    def rateMovie(self):
        self.client.post("/restapis/" + str(os.getenv('API_GATEWAY_ID')) + "/dev/_user_request_/rate-movie", json={
        "id": "438149",
        "overview": "A fanboy of a supervillain supergroup known as the Vicious 6, Gru hatches a plan to become evil enough to join them, with the backup of his followers, the Minions.",
        "poster_path": "/tzFAboMUGJKoPQEtlxfxbbYsSWa.jpg",
        "release_date": "2022-06-29",
        "title": "Minions: The Rise of Gru",
        "grade_evaluated" : 1
})



