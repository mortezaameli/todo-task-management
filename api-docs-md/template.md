# Register a user

register a user with email, username, password, password2

**URL** : `/api/register/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : NO

## Success Response

**Code** : `200 OK`

**Content examples**

```json
{
    "email"    : "sample@gmail.com",
    "username" : "Mortza",
    "password" : "MA12=sdOP",
    "password2": "MA12=sdOP"
}
```


## Notes

* If the User does not have a `UserInfo` instance when requested then one will
  be created for them.



