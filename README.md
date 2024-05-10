# UAV RENTAL APP

## Project Description

This project aims to create a comprehensive system for managing UAVs (Unmanned Aerial Vehicles) and rentals, while also providing user management functionalities. The backend is built using Django REST Framework, and the frontend is developed with React.

## Modules:

1. **UAV (Unmanned Aerial Vehicle):**
   - CRUD operations are available.
   - Two types of users exist: BrandUser and CustomUser.

2. **Rental:**
   - CRUD operations are available.
   - Both BrandUser and CustomUser have full access to rental operations.

3. **Users:**
   - BrandUser: Has authorization for all UAV CRUD operations.
   - CustomUser: Has authorization only to list UAVs.

## Authorization:
   - **BrandUser:** Authorized for all CRUD operations related to UAVs.
   - **CustomUser:** Authorized only to list UAVs.
   - Both BrandUser and CustomUser have full access to rental CRUD operations.

## Frontend Integration:
   - Currently, only BrandUsers can log in.
   - Upon BrandUser login, navigation is enabled.
   - For CustomUser, navigation to specific pages has not been implemented yet.

## How to Run:

### Prerequisites:

- Node.js and npm installed
- Python and pip installed

### Backend (Django REST Framework):

1. Navigate to the `uavrentalapi` directory: `cd uavrentalapi`.
2. Install Python dependencies: `pip install -r requirements.txt`.
3. Apply database migrations: `python manage.py migrate`.
4. Run the Django server: `python manage.py runserver`.

### Frontend (React):

1. Navigate to the `uavrentalportal` directory: `cd uavrentalportal`.
2. Install Node.js dependencies: `npm install`.
3. Start the development server: `npm start`.

### Docker Compose:

#### Running with Docker Compose:

1. Make sure you have Docker installed on your machine.
2. Navigate to the project directory.
3. Run the following command to build and start the services:

    ```
    docker-compose up --build
    ```

4. Once the services are up and running, you can access the application at the following URLs:
   
   - uavrentalapi (Django): http://app.uavrental.com:8000
   - uavrentalportal (React): http://ui.uavrental.com:3000

#### Accessing the Application:

Please make sure to add the following entries to your hosts file (`C:\Windows\System32\drivers\etc\hosts`) after starting the services:

   ```
      127.0.0.1       db.uavrental.com
      127.0.0.1       app.uavrental.com
      127.0.0.1       ui.uavrental.com
   ```