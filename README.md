This project shows available cars and allows logged in users to book.

#### Requirements
Python 2.7

#### Setup
* Install [pip](https://pip.pypa.io/)
* Setup & activate a virtual environment. Look at [virtualenv](https://virtualenv.pypa.io/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) for this.


#### Starting the project
Assuming you are in your virtual environment:
`$ git clone https://github.com/Jorzakay/evezy-project.git`
`$ cd evezy-project`
`$ pip install -r requirements.txt`
`$ python manage.py runserver`

In your browser, visit localhost:8000 to view the website.

#### Making a booking
* You must be logged in to make a booking
Demo credentials:
`username:demo`
`password:demo1234`
* Start/End dates must be in the format dd/mm/yyyy e.g.(31/01/2019)
* Start/End times must be in the format HH:MM e.g.(22:00)

#### For admins
Administrators can easily create, view, update and delete Cars and Bookings by visiting `http://localhost:8000/admin` using the credentials `username:admin password: admin1234`
