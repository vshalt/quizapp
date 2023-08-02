# Country Quiz

## Installation
- Download the repository and open it
- Create a virtual environment.  Use `python3 -m venv venv` to create a virtual environment.
- Activate the virtual environment by using `source venv/bin/activate` in UNIX systems and `.\venv\Scripts\activate` in Windows devices.
- Install the dependencies by using `python pip install -r requirements.txt`
- Run migrations on database so that the latest schema is reflected. `python manage.py migrate`
- Run the file `add_data.py` that will get the countries and load them into the database `python manage.py add_data.py`
- Run the server by running `python manage.py runserver`
