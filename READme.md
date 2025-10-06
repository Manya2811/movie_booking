# Movie Ticket Booking System - Backend

This repository contains the backend system for a Movie Ticket Booking application, developed as part of a backend developer assignment. The system is built with Python, Django, and Django REST Framework, providing a complete RESTful API for user authentication, movie browsing, showtime viewing, and ticket booking.

## ✨ Features

- **JWT Authentication**: Secure user registration and login using JSON Web Tokens (JWT).
- **Movie & Show Management**: Endpoints to list movies and view available showtimes for each movie.
- **Seat Booking & Cancellation**: Functionality for authenticated users to book seats for a specific show and cancel their existing bookings.
- **User-Specific Views**: An endpoint for users to view a list of all their own bookings.
- **API Documentation**: Integrated Swagger UI for interactive API documentation and testing.
- **Robust Business Logic**: Includes server-side validation to prevent double-booking and over-booking seats.

## 🛠️ Technology Stack

- **Backend**: Python, Django, Django REST Framework
- **Authentication**: djangorestframework-simplejwt (JWT)
- **API Documentation**: drf-yasg (Swagger)
- **Database**: SQLite (Default for Django development)

## 🚀 Setup and Installation

Follow these steps to get the project running on your local machine.

1.  **Clone the Repository**

    ```bash
    git clone <your-repository-url>
    cd movie_booking_system
    ```

2.  **Create and Activate a Virtual Environment**

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (for Admin Access)**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    The API will now be available at `http://127.0.0.1:8000/`.

## ⚙️ API Usage

The API follows a standard RESTful flow. Booking-related actions require authentication.

1.  **Register a New User**
    Send a `POST` request to `/api/signup/` with a `username` and `password`.

2.  **Log In to Get JWT Token**
    Send a `POST` request to `/api/login/` with your credentials to receive an `access` and `refresh` token.

3.  **Authorize Future Requests**
    For all protected endpoints, include the `access` token in the `Authorization` header:

    ```
    Authorization: Bearer <your_access_token>
    ```

4.  **API Flow Example**
    - View all movies: `GET /api/movies/`
    - View shows for a movie: `GET /api/movies/<id>/shows/`
    - Book a seat: `POST /api/shows/<id>/book/` (Requires Authorization)
    - View your bookings: `GET /api/my-bookings/` (Requires Authorization)
    - Cancel a booking: `POST /api/bookings/<id>/cancel/` (Requires Authorization)

## 📚 API Documentation (Swagger)

Interactive API documentation is available through Swagger UI. Once the server is running, you can access it at:

- **URL**: `http://127.0.0.1:8000/swagger/`

You can use the "Authorize" button in the Swagger UI to add your JWT Bearer token and test all the protected endpoints directly from your browser.
