# Update Task

* update position of task (phase and row_position)
* update title of task
* update description of task
* update start_date of task
* update due_date of task
* update percentage of task

**URL** : `/project/task/<int:pk>/`

**Method** : `PUT`

**Auth required** : YES

**Permissions required** : YES

## Success Response

**Code** : `200 OK`

**request examples:**

* update position of task (phase and row_position):

```json
{
    "phase" : "TODO",      // ["TODO", "DOING", "DONE"]
    "row_position" : 2,
}
```

* update title of task:
```json
{
    "title" : "new_title",
}
```

* update description of task
```json
{
    "description" : "new_description",
}
```

* update start_date of task
```json
{
    "start_date" : "new_start_date",
}
```

* update due_date of task
```json
{
    "due_date" : "new_due_date",
}
```

* update percentage of task
```json
{
    "percentage" : 35,  //[0-100]
}
```

## Error Response

* **Code** : `400 BAD_REQUEST`
* **Code** : `403 FORBIDDEN`
* **Code** : `404 NOT_FOUND`
