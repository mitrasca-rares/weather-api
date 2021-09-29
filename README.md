# Weather API

Weather API is a Django application that provides weather history for a given location.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the application.
```bash
pip install -r requirements.txt
```

## Usage
```bash
python manage.py runserver
```

## API Endpoints

```python
Users
'/api/auth/token/$' (User login endpoint)
'/api/auth/token-refresh/$' (User token refresh endpoint)

Locations
'/api/locations/$' (User location list endpoint)
'/api/locations/{location-id}/$' (User location detail endpoint)

Parameters
'/api/locations/{location-id}/parameters/$' (Location parameter list endpoint)
'/api/locations/{location-id}/parameters/{parameter-id}/$' (Location parameter detail endpoint)
