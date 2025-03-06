# Github App Integration

## Overview
This project integrates with the Github API to provide a seamless experience.

## Tech Stack
Python: Programming language
Pytest: Testing framework
FastAPI: Web framework for building APIs
Pydantic: Library for building robust data models

## Getting Started

### Setting up environment variables

```bash
cp env-template .env
```

then replace the values for real ones

### local data

`*.py.example` files are templates for real `*.py tests`

### Running the API
To start the API, run the following command:
```bash
fastapi dev
```
This will start the development server, and you can access the API at http://localhost:8000.

### Docs
http://localhost:8000/docs

### Running Tests
To run the tests, use the following command:
```bash
pytest
```
This will execute all the tests in the project.
