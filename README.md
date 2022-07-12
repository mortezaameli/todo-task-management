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
* [Invite to project](api-docs-md/invite_to_project.md) : &nbsp; **`POST`**  &nbsp;  `/project/invite/`
* [Answer to invitations](api-docs-md/answer_to_invite.md) : &nbsp; **`POST`**  &nbsp;  `/project/invite/answer/`
