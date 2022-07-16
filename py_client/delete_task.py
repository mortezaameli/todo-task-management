from jwt_client import JWTClient

client = JWTClient()
id = input('Task ID: ')
endpoint = f'http://localhost:8000/project/task/{id}/'
result = client.delete_without_data(endpoint)

print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])