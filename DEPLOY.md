## Run Locally
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
```
Make a copy of `config.template.yaml` and name it `config.yaml`

Run `docker-compose up --build` and access admin dashboard via http://localhost/admin/
## Deploy to AWS