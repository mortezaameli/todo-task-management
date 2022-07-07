from jwt_client import JWTClient

client = JWTClient()
endpoint = 'http://localhost:8000/project/'
name = input('Project name: ')
post_data = {'name': name}
data = client.post_data(endpoint, post_data)
print(data)