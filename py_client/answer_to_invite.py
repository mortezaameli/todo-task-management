from jwt_client import JWTClient

client = JWTClient()
endpoint = 'http://localhost:8000/project/invite/answer/'
id = input('Project ID: ')
confirmed = input('Confirm project invitation(y/n): ')
if confirmed.lower() == 'y':
    confirmed = True
elif confirmed.lower() == 'n':
    confirmed = False
post_data = {'project_id': id, 'confirmed': confirmed}
result = client.post_data(endpoint, post_data)
print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])