# ToDo Task Management

Task management application that manage todo task

Users can create different projects and invite other users to collaborate on the project.
Each project consists of some tasks that fall into categories ToDo, Doing, Done.

This project written in the python Django Rest Framework (DRF)

> **Here is the `backend` of the project**

> **A friend has implemented a `frontend` in `React` using the APIs made here : [React FrontEnd](https://github.com/mojtaba1374/To-Do_TaskManager)**

## Installation and Run server

Create python virtualenv and activate it, then:

Install requirement packages:
```sh
pip install requirements/requirements.txt
```

Running the server on port 8000
```sh
python backend/manage.py runserver
```

## APIs Documentation

### Login and Register

* [Register a user](api-docs-md/register_user.md) : &nbsp; **`POST`**  &nbsp;  `/api/register/`
* [Login and fetch JWT tokens](api-docs-md/login_user.md) : &nbsp; **`POST`**  &nbsp;  `/api/token/`
* [Refresh access token](api-docs-md/refresh_token.md) : &nbsp; **`POST`**  &nbsp;  `/api/token/refresh/`
* [Verify access token](api-docs-md/verify_token.md) : &nbsp; **`POST`**  &nbsp;  `/api/token/verify/`
* [User profile info](api-docs-md/user_profile.md) : &nbsp; **`GET`**  &nbsp;  `/api/profile/`

### Projects

* [Projects list](api-docs-md/project_list.md) : &nbsp; **`GET`**  &nbsp;  `/projects/`
* [Create project](api-docs-md/project_create.md) : &nbsp; **`POST`**  &nbsp;  `/project/`
* [Delete project](api-docs-md/project_delete.md) : &nbsp; **`DELETE`**  &nbsp;  `/project/:pk/`
* [Update project name](api-docs-md/project_update.md) : &nbsp; **`PUT`**  &nbsp;  `/project/:pk/`

### Members
* [Invite to project](api-docs-md/invite_to_project.md) : &nbsp; **`POST`**  &nbsp;  `/project/invite/`
* [Answer to invitations](api-docs-md/answer_to_invite.md) : &nbsp; **`POST`**  &nbsp;  `/project/invite/answer/`
* [Project members list](api-docs-md/project_members_list.md) : &nbsp; **`GET`**  &nbsp;  `/project/:pk/members/`
* [Project members delete](api-docs-md/project_members_delete.md) : &nbsp; **`DELETE`**  &nbsp;  `/project/:pk/member/`

### Tasks
* [Task list](api-docs-md/task_list.md) : &nbsp; **`GET`**  &nbsp;  `/project/:pk/tasks/`
* [Create Task](api-docs-md/task_create.md) : &nbsp; **`POST`**  &nbsp;  `/project/:pk/task/`
* [Update Task](api-docs-md/task_update.md) : &nbsp; **`PUT`**  &nbsp;  `/project/task/<int:pk>/`
* [Delete Task](api-docs-md/task_delete.md) : &nbsp; **`DELETE`**  &nbsp;  `/project/task/<int:pk>/`
