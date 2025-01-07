# Patient Registration API

A **FastAPI-based Patient Registration System** for securely collecting and storing patient information, validating input data, handling file uploads, and sending email confirmations.

---

## Features
1. **Patient Registration**: 
   - Collects patient name, email, phone number, and a document file.
   - Validates email and phone formats.
   - Enforces document size limit (2MB).
2. **Database Storage**: MySQL-based secure patient data storage.
3. **Asynchronous Email Notifications**: Sends confirmation emails upon successful registration.
4. **Dockerized Setup**: Simplified deployment using Docker Compose.

---

## Requirements
- **Docker**: 20.10+
- **Docker Compose**: 1.29+

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
```
### 2. Configure Environment Variables
In the root directory of the project, create a .env file and add the required mail server credentials. 
You can refer to the env-sample file for the necessary variables. 
For testing purposes, you can use a service like MailTrap.

### 3. Start the application

```bash
docker-compose up --build
```

## API Access

The API can be accessed at `http://localhost:8000`. 

You can view the available endpoints and documentation by visiting `http://localhost:8000/docs`. This API is built using FastAPI and provides interactive documentation for easier exploration of the available endpoints.

## API Endpoints

### 1. **Register Patient**
- **URL**: `/register`
- **Method**: POST
- **Payload**:
  ```json
  {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "+1234567890",
    "document": "<base64-encoded-photo>"
  }
  
### Responses

- **Success**: `201 Created`
  ```json
  {
    "message": "Patient registered successfully."
  }
- **Validation Error**: `422 Unprocessable Entity`
  ```json
  {
    "detail": "**Validation Error detail**"
  }

- **Internal Server Error**: `500 Internal Server Error`
  ```json
  {
    "detail": "An error occurred during registration. Please try again later."
  }
