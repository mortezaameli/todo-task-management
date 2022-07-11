# Login a user

login and get JWT tokens(access, refresh)

**URL** : `/api/token/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : NO

## Success Response

**Code** : `200 OK`

**request example:**
```json
{
    "email"    : "sample@gmail.com",
    "password" : "MA12=sdOP",
}
```

**response example:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzYyNTgxNCwiaWF0IjoxNjU3NTM5NDE0LCJqdGkiOiIyYjc1ZDIzM2E2N2M0YWUxYmYxZDgxODA2ZTk2NTNkMyIsInVzZXJfaWQiOjF9.RUdveEQ_u6VDTCBdLCF0UR0jAp9-zQZgYVpJt1Ote9k",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NTM5NzE0LCJpYXQiOjE2NTc1Mzk0MTQsImp0aSI6IjM4ZGJiMzk4NDA1YTQzMTViNTBjMjVkMTkwOTczNWI5IiwidXNlcl9pZCI6MX0.SGoj6oZnN44Ycnf5RAlH6KJcyFmvkIKJqdOaQv6_wik"
}
```
