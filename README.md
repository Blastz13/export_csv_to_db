# Test Task

## Stack project

- **Python**
- **Django**
- **Django Rest Framework**
- **JWT**
- **Flake8**
- **Swagger**
- **Docker**

## Installation and launch

**Installation**

You can clone this application:

```bash 
git clone https://github.com/Blastz13/export_csv_to_db.git
```

Next, you need to install the necessary libraries:

```bash
cd export_csv_to_db
pip3 install -r requirements.txt
```

**Launch**

Change directory from web app, create and apply migrations:

```bash
* Add the police-department-calls-for-service.csv file to the project *
python3 upload_data_to_db.py
python3 manage_dev.py collectstatic
python3 manage_dev.py makemigrations
python3 manage_dev.py migrate
```

Now you can start the server:

```bash
python3 manage_dev.py runserver
```

### License

Copyright © 2022 [Blastz13](https://github.com/Blastz13/).