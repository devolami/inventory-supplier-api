# Business Scenario: Online Store Inventory and Supplier Management API

## Important Information

### Steps to Run the Project Locally

1. **Clone the repository**, then `cd` into the project directory.
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Create a virtual environment**:
   - On Windows:
     ```bash
     py -m venv venv
     ```
   - On Mac:
     ```bash
     virtualenv venv
     ```
   - Note: Ensure `virtualenv` is installed before running this command.

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install necessary packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Make migrations**:
    ```bash
    python manage.py makemigrations
    ```

6. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Run all tests**:
    ```bash
    python manage.py test
    ```
    - The results of the tests will be printed in the terminal.

8. **Create a superuser**:
    ```bash
    python manage.py create_superuser
    ```
    - Follow the prompts to create a super user.

9. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

10. **Navigate to the admin panel**:
    - URL: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
    - Login to add data.

11. **Read detailed documentation and test endpoints**:
    - Swagger: [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Author: Muhammed Abdulganiyy