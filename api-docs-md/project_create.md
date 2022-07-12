# Create Project

create new project

**URL** : `/project/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : YES

## Success Response

**Code** : `201 CREATED`

**request example:**
```json
{
    "name" : "project_name"
}
```

**response example:**
```json
{
    "id" : 12
}
```

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
