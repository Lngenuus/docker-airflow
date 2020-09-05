import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())
#user.username = os.environ['AIRFLOW_ADMIN_USSR']
#user.email = os.environ['AIRFLOW_ADMIN_EMAIL']
#user.password = os.environ['AIRFLOW_ADMIN_PASS']
user.username = 'admin'
user.email = 'admin@admin.com'
user.password = 'admin'
user.superuser = True
session = settings.Session()

session.add(user)
session.commit()
session.close()
