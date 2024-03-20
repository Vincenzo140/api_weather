from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def generate_weather(self):
        self.client.get("/generate", name="/generate")
