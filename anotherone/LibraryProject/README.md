# LibraryProject

## Introduction
LibraryProject is a Django-based web application designed to manage a library system. It allows users to browse, borrow, and return books, as well as manage their library accounts.

## Features
- User authentication and authorization
- Book catalog management
- Borrowing and returning books
- User account management
- Search functionality for books

## Installation
1. Clone the repository:
	```bash
	git clone https://github.com/yourusername/LibraryProject.git
	```
2. Navigate to the project directory:
	```bash
	cd LibraryProject
	```
3. Create a virtual environment:
	```bash
	python3 -m venv env
	```
4. Activate the virtual environment:
	```bash
	source env/bin/activate
	```
5. Install the required dependencies:
	```bash
	pip install -r requirements.txt
	```
6. Apply migrations:
	```bash
	python manage.py migrate
	```
7. Create a superuser:
	```bash
	python manage.py createsuperuser
	```
8. Run the development server:
	```bash
	python manage.py runserver
	```

## Usage
1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Log in with your superuser credentials.
3. Start managing your library!

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Django Documentation
- Bootstrap for front-end styling
