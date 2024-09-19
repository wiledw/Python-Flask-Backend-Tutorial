# Flask MongoDB CRUD API

This repository contains a Flask application that performs CRUD (Create, Read, Update, Delete) operations using MongoDB.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup and Installation](#setup-and-installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [API Endpoints (CRUD Operations)](#api-endpoints)

## Prerequisites

- Python 3.6 or higher
- MongoDB (Local or MongoDB Atlas)
- `pip` (Python package installer)

## Setup and Installation

  **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

  **Install Dependencises**
  ```bash
    pip install "pymongo[srv]==3.11" Flask python-dotenv
   ```

  **Create .env file**
  ```bash
   MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority
   ```
  Replace <username> and <password> with your MongoDB Atlas credentials.
  Replace mydatabase with the name of your database.
  Make sure to ignore the env file in .gitignore

## Configuration

  **Setup MongoDB**
  MongoDB Atlas: Sign up for MongoDB Atlas and create a cluster. Obtain your connection URI from the Atlas dashboard.

## Running the Application

   ```bash
   python app.py or py app.py
   ```
  The application will start and listen on http://127.0.0.1:5000 by default.

## API Endpoints (CRUD Operations)

   **Create User(POST /users)**
   Body:
   ```json
   {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
   ```

   **Get all User(GET /users)**
   
   **Get specific User(GET /users/<user_id>)**
    
   **Update User(PUT /users)**
   Body:
   ```json
   {
    "name": "Jane Doe",
    "age": 25
  }
   ```

  **DELETE specific User(DELETE /users/<user_id>)**


  



