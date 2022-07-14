from jwt_client import JWTClient

client = JWTClient()
id = input('Project ID: ')
endpoint = f'http://localhost:8000/project/{id}/task/'
title = input('Task title: ')
post_data = {'title': title}
result = client.post_data(endpoint, post_data)
print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])
