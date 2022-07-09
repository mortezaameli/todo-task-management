from jwt_client import JWTClient

client = JWTClient()
endpoint = 'http://localhost:8000/project/invite/'
id = input('Project ID: ')
email = input('User email for Invitation: ')
post_data = {'project_id': id, 'user_email': email}
result = client.post_data(endpoint, post_data)
print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])