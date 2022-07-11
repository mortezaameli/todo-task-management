# Login a user

Refresh JWT access token

**URL** : `/api/refresh/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : NO

## Success Response

**Code** : `200 OK`

**request example:**
```json
{
    "refresh" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NjkzOTQwNCwiaWF0IjoxNjU2ODUzMDA0LCJqdGkiOiJlNTgzZGQwNDRiNjc0ZWMyODVkMWVkMTg5NWRiYjJiYSIsInVzZXJfaWQiOjF9.ZUk7I0WXxbSAOtucZJyUmZRtlj4YhUfBouk5S98Uf80"
}
```

**response example:**
```json
{}
```

## Error Response

**Condition** : refresh token expire or invalid

**Code** : `401 UNAUTHORIZED`

**Content** : 
```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```
