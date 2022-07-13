# ToDo Task Management

Task management application that manage todo task

This project written in the python Django Rest Framework (DRF)

## APIs Documentation

### Login and Register

* [Register a user](api-docs-md/register_user.md) : &nbsp; **`POST`**  &nbsp;  `/api/register/`
* [Login and fetch JWT tokens](api-docs-md/login_user.md) : &nbsp; **`POST`**  &nbsp;  `/api/token/`
* [Refresh access token](api-docs-md/refresh_token.md) : &nbsp; **`POST`**  &nbsp;  `/api/token/refresh/`
* [Verify access token](api-docs-md/verify_token.md) : &nbsp; **`POST`**  &nbsp;  `/api/token/verify/`

### Projects

* [Projects list](api-docs-md/project_list.md) : &nbsp; **`GET`**  &nbsp;  `/projects/`
* [Create project](api-docs-md/project_create.md) : &nbsp; **`POST`**  &nbsp;  `/project/`
* [Delete project](api-docs-md/project_delete.md) : &nbsp; **`DELETE`**  &nbsp;  `/project/:pk/`
* [Update project name](api-docs-md/project_update.md) : &nbsp; **`PUT`**  &nbsp;  `/project/:pk/`

### Members
* [Invite to project](api-docs-md/invite_to_project.md) : &nbsp; **`POST`**  &nbsp;  `/project/invite/`
* [Answer to invitations](api-docs-md/answer_to_invite.md) : &nbsp; **`POST`**  &nbsp;  `/project/invite/answer/`
* [Project members list](api-docs-md/project_members_list.md) : &nbsp; **`GET`**  &nbsp;  `/project/:pk/members`

