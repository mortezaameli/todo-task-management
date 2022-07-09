from jwt_client import JWTClient

client = JWTClient()
endpoint = 'http://localhost:8000/project/'
name = input('Project name: ')
post_data = {'name': name}
result = client.post_data(endpoint, post_data)
print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])
