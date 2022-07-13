# Update Project Name

update project name

**URL** : `/project/:pk/`

**Method** : `PUT`

**Auth required** : YES

**Permissions required** : YES

## Success Response

* When the project name is different from the previous name:

> **Code** : `200 OK`

**request example:**
```json
{
    "name" : "new_project_name"
}
```

**response example:**
```json
{
    "id" : 12
}
```

* When the project name is the same as the previous name:

> **Code** : `204 NO_CONTENT`

## Error Response

* **Code** : `403 FORBIDDEN`
* **Code** : `404 NOT_FOUND`

