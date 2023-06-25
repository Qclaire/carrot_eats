## Carrot Eats Project [A mini clone of DoorDash]

This guide provides concise instructions to clone, setup, and run the project. The project uses Pipenv as the dependency manager and includes Swagger documentation located at `/docs`.

### Prerequisites

- Git installed on your system
- Python installed on your system
- Pipenv installed (`pip install pipenv`)

### Instructions

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

7. Access the Swagger documentation:
   Open your web browser and go to `http://localhost:8000/docs` to view the Swagger documentation.

8. Locate `POST users/` near the bottom of documention under users section
9. Click on it to expand the menu

10. Click on `Try it out`
11. Fill in the first_name, last_name, email and passwork json keys with your desired values
12. Click on `Execute` to execute the request.

13. If sucessful, you should get a 200 status code with the details you presented in response body

14. Now locate the `token` section just above `users`

15. Expand `token/login` and use your credentials from `11` above to login

16. If successfull, you will recieve a pair of jwt tokens `access` and `refresh`

17. copy the value of the access token and to be used as authorisation token for all subsequent requests

18. Scroll all the way to the top of the document and look for the `authorize` button
19. Type

These instructions assume you are using the default port 8000 for the development server. If you're using a different port, adjust the URL accordingly.
