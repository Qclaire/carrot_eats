## Django DRF Project Setup with Pipenv and Swagger Documentation

This guide provides concise instructions to clone, setup, and run a Django DRF project that uses Pipenv as the dependency manager and includes Swagger documentation located at `/docs`.

### Prerequisites
- Git installed on your system
- Python installed on your system
- Pipenv installed (`pip install pipenv`)

### Instructions

1. Clone the project repository:
   ```bash
   git clone <repository_url>
   ```

2. Change into the project directory:
   ```bash
   cd <project_directory>
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

Remember to replace `<repository_url>` with the actual URL of the project repository and `<project_directory>` with the desired directory name for your project.

These instructions assume you are using the default port 8000 for the development server. If you're using a different port, adjust the URL accordingly.

Save these instructions in a Markdown (`.md`) file for easy reference.

Enjoy working with your Django DRF project and exploring the Swagger documentation!