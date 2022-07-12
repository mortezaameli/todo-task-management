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
    "msg" : "The request for cooperation in the project was sent to the user"
}
```

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
* **Code** : `404 NOT_FOUND`
* **Code** : `409 CONFLICT`
