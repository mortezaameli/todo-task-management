from jwt_client import JWTClient

client = JWTClient()
endpoint = "http://localhost:8000/projects/"
data = client.fetch_data(endpoint)
print(data)