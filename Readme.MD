# Stage 2 Task

This is a RESTful API for managing and interacting with [describe what your API does].

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Starting the API](#starting-the-api)
  - [API Endpoints](#api-endpoints)

## Getting Started

These instructions will guide you through setting up and running Your API Name on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) (version X.X or higher)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (recommended for managing Python environments)
- [Django](https://www.djangoproject.com/download/) (version X.X or higher)
- [Django Rest Framework](https://www.django-rest-framework.org/#installation)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-api-name.git
    ```

1. Navigate to the project directory:

    ```bash
    cd your-api-name
    ```

1. Create and activate a virtual environment (optional but recommended):

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```
1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
1. Apply migrations to create the database:

    ```bash
    python manage.py migrate
    ```

## Usage
Starting the API
To run the API locally, use the following command:

    python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/

#### API Endpoints
Create a Person (POST)
Create a new person by sending a POST request to the following endpoint:
```
POST /api/people/
```
Example request body:

```json
{
  "name": "John Doe"
}
```
> *Note* name must be unique
Retrieve a Person (GET)
Retrieve information about a person by sending a GET request to the following endpoint:

```sh
GET /api/people/<person_id>/
```
Update a Person (PUT)
Update a person's information by sending a PUT request to the following endpoint:

```
PUT /api/people/<person_id>/
```
Example request body:

```json
{
  "id": <person_id>,
  "name": "Updated Name"
}
```
Delete a Person (DELETE)
Delete a person by sending a DELETE request to the following endpoint:

```
DELETE /api/people/<person_id>/
```

# UML Diagram

Below is a simplified UML class diagram representing the structure and relationships of the `PersonView` API class and the `Person` model.
(url)[https://drawsql.app/teams/captain/diagrams/stage2]