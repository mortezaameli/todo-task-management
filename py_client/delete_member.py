from jwt_client import JWTClient

client = JWTClient()
id = input('Project ID: ')
endpoint = f'http://localhost:8000/project/{id}/member/'
email = input('User email to delete(or empty enter for send yourself): ')
if email == '':
    result = client.delete_without_data(endpoint)
else:
    data = {'email': email}
    result = client.delete_with_data(endpoint, data)

print('=' * 60)
print(f"Status Code: {result['status_code']}")
print('-' * 60)
print(result['text'])