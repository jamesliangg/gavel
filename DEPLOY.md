## Run Locally
### Using SendGrid API
Create a `.env` file in the same folder as the `docker-compose.yml` file with the following variables:
```
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
ADMIN_PASSWORD=<ADMIN_PASSWORD>
EMAIL_FROM=<EMAIL_FROM>
EMAIL_USER=_unused_
EMAIL_PASSWORD=_unused_
SECRET_KEY=<SECRET_KEY>
DATABASE_URL=<DATABASE_URL>
REDIS_URL=redis://redis:6379/0
USE_SENDGRID=True
SENDGRID_API_KEY=<SENDGRID_API_KEY>
DISABLE_EMAIL=False
SEND_STATS=False
```
Make a copy of `config.template.yaml` and name it `config.yaml`

Run `docker-compose up --build` and access admin dashboard via http://localhost/admin/
### Using SMTP
### Using SendGrid API
Create a `.env` file in the same folder as the `docker-compose.yml` file with the following variables:
```
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
ADMIN_PASSWORD=<ADMIN_PASSWORD>
EMAIL_FROM=<EMAIL_FROM>
USE_SENDGRID=False
DISABLE_EMAIL=False
SECRET_KEY=<SECRET_KEY>
DATABASE_URL=<DATABASE_URL>
REDIS_URL=<REDIS_URL>
SEND_STATS=False

EMAIL_USER=<EMAIL_USER>
EMAIL_PASSWORD=<EMAIL_PASSWORD>
EMAIL_HOST=<EMAIL_HOST>
EMAIL_PORT=<EMAIL_PORT>
EMAIL_AUTH_MODE=<EMAIL_AUTH_MODE>

```
Make a copy of `config.template.yaml` and name it `config.yaml`

Run `docker-compose up --build` and access admin dashboard via http://localhost/admin/
## Deploy to AWS