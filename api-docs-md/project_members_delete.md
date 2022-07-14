# Project Member Delete

* admin of project delete other member
* user leaves the project herself

**URL** : `/project/:pk/member/`

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : YES

## Success Response

**Code** : `204 NO_CONTENT`

> when admin of project delete other member

**request example:**
```json
{
    "email" : "email_of_user_to_delete"
}
```

when user leaves the project herself

**request example:**

do not send data as a request

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
* **Code** : `404 NOT_FOUND`
