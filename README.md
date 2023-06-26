# Carrot Eats Project [A mini clone of DoorDash]

This guide provides concise instructions to clone, setup, and run the project. The project uses Pipenv as the dependency manager and includes Swagger documentation located at `api/docs/`.

## Prerequisites

The projet is built in Django and Django Rest Framework.

- Git installed on your system
- Python installed on your system
- Pipenv installed (`pip install pipenv`)

## Project Structure

The project is structures following Django's project/app concept. Django provides that there be one base project and infinite number of apps, each representing a unique set of functionalities (microservices).

In this project I have created one main project and one app as follows:

- `main` - This is the main project directory containing project settings and urls.
- `api` - This is a Django app containing the api code. All logic of the code is stored here.

### API Structure

In the api directory which contains the overall logic for the application backend, you will find a number of directories containing different pieces of code as follows:

1. `migrations` - This directory contains the database migration records. You don't need to inspect this directory
2. `models` - This contains the database table definitions and relationships
3. `serializers` - This contains the code for serialising data to sent the caller and deserialising data to store the database
4. `view` - These are the classes representing the presentation layer of this application
5. `tests` - contains a few unit test for demonstration purposes

If you are familiar with Django you would realise that the directory structure has been modified from simple files to packages for convenience and better organisation

## Unit tests

Though not specified as part of the assignment, I have included a few unit tests to cover some of the models as a demonstration.
To inspect them go to `api > tests > models`
The tests for each model has a dedicated file to store it's unit tests.

## How to run the tests

To rund the unit tests, follow `Instructions to run and test the APIs` below from step 1 to 5.
Once at at step 5 and your virtaul environment is active, run the following command in the terminal

```bash
python manage.py test api.tests.models
```

## Instructions to run and test the APIs

1. Clone the project repository:

   ```bash
   git clone https://github.com/Qclaire/carrot_eats
   ```

2. Change into the project directory:

   ```bash
   cd carrot_eats
   ```

3. Create a virtual environment and install project dependencies:

   ```bash
   pipenv install
   ```

4. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

5. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

   By default this will run your appl on port 8000. If you wish to use a different port eg: 9000, you need to specify the port like so:

   ```bash
   python manage.py runserver 9000
   ```

7. Access the Swagger documentation:

   - Open your web browser and go to `http://localhost:8000/api/docs/` to view the Swagger documentation.

8. Create A new user Account and login

   - Locate `POST /users/` under users section near the bottom of documention
   - Click on it to expand the menu
   - Click on `Try it out` near the top
   - Fill in the provided json keys with desired values
   - Click on `Execute` to send the request.
   - If sucessful, you should get a 200 status code

9. Now login to obtain authorisation tokens

   - locate the `token` section just above `users` section
   - Locate `POST token/login/`
   - Use the credentials you created in 8 to login
   - You will recieve `access` and `refresh` jwt token pair
   - You will need the access token for subsequent requests
   - Copy the value of the access token for the next step

10. Now you need to authorise future requests

- Locate the `authorize` button at the top of the document
- Click on it to see the authorisation pop up
- In the box type `Bearer` and leave single space
- Paste you access token copied ealier after the space
- Click `Authorize` to save the token
- Click `Close` be careful not to click logout instead

11. You are now ready to explore the APIs

- Expand any enpoint you wish to test and input the necessary data where applicable

## How to test with postman or similar tools

Due to the presence of the swagger documentation you may not have a need to test in postman or similar tools. However, if you choose to do so, you can easily test by following the similar instructions as the swagger documentation

- The base url is `http://localhost:8000/api`
- You must append the specific path for you desired endpoints to this base url to test in postman
- start by using `POST /users/` to create your account but making post request to `http://localhost:8000/api/users/` in postman
- provide the first_name, last_name, email, password as a multipart form or Json.
- once use a similar approach to login and obtain your access token
- Then add the token to your request headers in each request

## Role-based Authorisation

In the file `api/permissions.py` I have provided sample authorisations using hardcoded roles. These have been used as permission classes in a few of the veiws to demonstrate how we might restrict access to the application based on user roles.

There is also a Role database model that demonstrate how we might store the roles in a database instead of hardcoding them. For simplicity these models have not been used in this application to avoind having to create roles before being able to test the APIs

### Existing Roles

I have included the following roles

```
RESTAURANT_MANAGER_ROLE = "RESTAURANT_MANAGER"
DELIVERY_AGENT_ROLE = "DELIVERY_AGENT"
ADMIN_ROLE = "ADMIN"
CUSTOMER_ROLE = "CUSTOMER"
```

While creating a user, you will need to specify one of these. for the user of they will be automatically assigned the role of `CUSTOMER`

## Additional Notes

- The price on a menu item is stored in integers instead of floats for simplicity and efficiency. This means a price of GHS 1 will be stored as 100 pesewas instead.
-
