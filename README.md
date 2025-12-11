# API Testing Portfolio

A comprehensive API testing project demonstrating automated testing skills using Python, Playwright, and pytest.

## Overview

This project showcases API testing capabilities using the JSONPlaceholder API, a free fake REST API for testing and prototyping. The test suite covers all major CRUD operations and common API testing scenarios.

## Features

- **Complete CRUD Testing**: Create, Read, Update, Delete operations
- **HTTP Method Coverage**: GET, POST, PUT, PATCH, DELETE
- **Status Code Validation**: 200 OK, 201 Created, 404 Not Found
- **Response Structure Validation**: Schema and data type validation
- **Query Parameter Testing**: Filtering and searching
- **Error Handling**: Testing negative scenarios and edge cases

## Technologies Used

- **Python 3.13.3**: Programming language
- **Playwright**: API testing framework
- **pytest**: Test framework and test runner
- **JSONPlaceholder**: Test API endpoint

## Project Structure

```
api-testing-portfolio/
├── tests/
│   ├── __init__.py
│   └── test_api.py          # Main test suite
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd api-testing-portfolio
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

Run all tests:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run a specific test:
```bash
pytest tests/test_api.py::test_get_single_user
```

Run tests with output captured:
```bash
pytest -s
```

## Test Coverage

The test suite includes:

### Basic CRUD Operations
- `test_get_single_user` - Retrieve a single user by ID
- `test_get_all_users` - Retrieve all users
- `test_create_user` - Create a new user (POST)
- `test_update_user` - Update a user completely (PUT)
- `test_partial_update_user` - Update a user partially (PATCH)
- `test_delete_user` - Delete a user

### Advanced Testing
- `test_get_users_with_query_params` - Query parameters and filtering
- `test_get_nonexistent_user` - 404 error handling
- `test_user_response_structure` - Response schema validation
- `test_response_status_codes` - Multiple status code scenarios

## API Endpoint

Base URL: `https://jsonplaceholder.typicode.com`

## Future Enhancements

- Add authentication/authorization testing
- Implement data-driven testing with parametrization
- Add performance/load testing
- Implement CI/CD pipeline
- Add test reporting with HTML reports
- Add more negative test scenarios
- Implement request/response logging

## License

This project is created for portfolio and educational purposes.
