# Advanced API Project

This project demonstrates the implementation of a Django REST API for managing books and authors. It includes models, serializers, views, URLs, and test cases.

## Models

### Author Model

The `Author` model represents an author with a single field `name`.

### Book Model

The `Book` model represents a book with three fields `title`,`publication_year` and `author` which is a Foreign key to the `Author` model.

## Serializers

Each model has a custom serilizer that can parse the model from python classes to a `json` format.

### AuthorSerializer

The `AuthorSerializer` class parses the `Author` model to the `json` format.

### BookSerializer

The `BookSerializer` class parses the `Book` model to the `json` format. There's also a custom validation method that checks if the publication year is a valid year and not some random/future year.

## Views

The views are the classes that perform certian functionality for each api endpoints. This application consists of five views:

### ListView

The `ListView` inherits from the rest_framework's `mixins.ListModelMixin` and `generics.GenericAPIView` classes. `ListView` takes a `GET` request and returns the list of the `Book` models that's in the database. It can also filter the outputted data by `title`, `publication_year` and `author`, has a search field for `title` and `author` then finally order the `book` by the `title`, `publication_year` and by `author`. Authentication is not required to access `ListView`.

### DetailView

The `DetailView` inherits from rest_framwork's `mixins.RetreiveModelMixin` and `generics.GenericAPIView`. `DetailView` takes a `GET` request and returns a `Book` instance based on it's id i.e `Book().id`. Authentication is not required to access `DetailView`

### CreateView

The `CreateView` inherits from rest_framwork's `mixins.CreateModelMixin` and `generics.GenericAPIView` classes. `CreateView` takes a `POST` request and creates a new instance of the `Book` model and save it to the database. It returns the newly created instance model. Authentication is required to create a new instance model.

### UpdateView

The `UpdateView` inherits from rest_framework's `mixins.UpdateModelMixin` and `generics.GenericAPIView` classes. `UpdateView` takes a `PUT` request and modifies or update an existing instance of the `Book` model it specifies it by it's id. Authentication is required to update an instance model

### DeleteView

The `DeleteView` inherits from rest_framwork's `mixins.DestroyModelMixin` and `generics.GenericAPIView` classes. `DeleteView` takes a `DELETE` request and deletes/destroys an existing model instance by it's id. Authentication is required delete an instance model.

## URLs

These are the api endpoints for each of the view classes.
- `books/` accesses the `ListView`
- `books/<int:pk>/` access the `DetailView` and `<int:pk>` represents the id therefore `books/i/` accesses the book instance with `id = 1`
- `books/create/` accesses the `CreateView`
- `books/update/<int:pk>` accesses the `UpdateView`
- `books/delete/<str:title>` accesses the `DeleteView`. Note the `<str:title>` this access the book based on the book title i.e `/books/delete/things fall` delete book with title things fall.

## Tests

### Interpreting Test Results
- If all tests pass, you will see a message indicating that all tests ran successfully.
- If any test fails, you will see a detailed error message indicating which test failed and why.
### Test Strategy
- Model Tests: Ensure that the models are correctly defined and that the data is being stored and retrieved as expected.
- View Tests: Ensure that the API endpoints are working correctly and that the appropriate status codes are returned.
### Guidelines
- Ensure that the database is properly set up before running the tests.
- Use the setUp method to create any necessary test data.
- Use assertions to verify that the expected results match the actual results.