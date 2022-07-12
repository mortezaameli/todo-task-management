# Invite to project

invite other users to the project for collaborate

**URL** : `/project/invite/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : YES

## Success Response

**Code** : `200 OK`

**request example:**
```json
{
    "project_id": 4,
    "user_email": "abc@gmail.com"
}
```

**response example:**
```json
{
    "username": "username_of_invited_user"
}
```

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
* **Code** : `404 NOT_FOUND`
* **Code** : `409 CONFLICT`
