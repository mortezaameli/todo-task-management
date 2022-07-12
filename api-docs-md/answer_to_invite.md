# Answer to project invitations

accept or reject invitations

**URL** : `/project/invite/answer/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : YES

## Success Response

**Code** : `200 OK`

when you want accept invitations:

**request example:**
```json
{
    "project_id": 3,
    "confirmed": true
}
```

**response example:**
```json
{
    "msg": "You have been added to the project"
}
```

and when you want reject invitations:

**request example:**
```json
{
    "project_id": 3,
    "confirmed": false
}
```

**response example:**
```json
{
    "msg": "Your membership was rejected"
}
```

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
* **Code** : `404 NOT_FOUND`
* **Code** : `409 CONFLICT`
