# Create Task

create new task

**URL** : `/project/:pk/task/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : YES

## Success Response

**Code** : `201 CREATED`

**request example:**
```json
{
    "title" : "task_title"
}
```

**response example:**
```json
{
    "id" : 3
}
```

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
