# Verify JWT Token

verify JWT access token

**URL** : `/api/verify/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : NO

## Success Response

**Code** : `200 OK`

**request example:**
```json
{
    "token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NTM5NzE0LCJpYXQiOjE2NTc1Mzk0MTQsImp0aSI6IjM4ZGJiMzk4NDA1YTQzMTViNTBjMjVkMTkwOTczNWI5IiwidXNlcl9pZCI6MX0.SGoj6oZnN44Ycnf5RAlH6KJcyFmvkIKJqdOaQv6_wik"
}
```

**response example:**
```json
{}
```

## Error Response

**Condition** : token expire or invalid

**Code** : `401 UNAUTHORIZED`

**Content** : 
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```
