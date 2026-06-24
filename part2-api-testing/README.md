# API Testing

## Overview

This test suite validates basic REST API behavior using the JSONPlaceholder API.

It covers the following scenarios:

- Fetching an existing user
- Creating a new post
- Verifying the API response for a non-existent user

## Tech Stack

- Python
- pytest
- requests

## Test Coverage

### GET `/users/1`

Validates that an existing user can be fetched successfully.

Assertions include:

- Response status code is `200`
- Response contains required fields: `id`, `name`, and `email`
- User ID matches the requested user

### POST `/posts`

Validates that a new post can be created successfully.

Assertions include:

- Response status code is `201`
- Response contains a generated `id`
- Response body matches the submitted payload

### GET `/users/999`

Validates API behavior when requesting a non-existent user.

Assertions include:

- Response status code is `404`
- Response body is empty

## Setup

Install dependencies from the project root:

```powershell
py -m pip install -r part2-api-testing\requirements.txt