from jwt_client import JWTClient

client = JWTClient()
endpoint = 'http://localhost:8000/task/'
id = input('Project ID: ')
title = input('Task title: ')
post_data = {'project_id': id, 'title': title}
result = client.post_data(endpoint, post_data)
print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])
