from jwt_client import JWTClient

client = JWTClient()
id = input('Project ID: ')
endpoint = f'http://localhost:8000/project/{id}/'
new_name = input('Project new name: ')
put_data = {'name': new_name}
result = client.put_data(endpoint, put_data)
print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])
