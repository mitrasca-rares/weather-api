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
'/auth/token/$' (User login endpoint)
'/auth/token-refresh/$' (User token refresh endpoint)

Locations
'/locations/$' (User location list endpoint)
'/locations/{location-id}/$' (User location detail endpoint)

Parameters
'/locations/{location-id}/parameters/$' (Location parameter list endpoint)
'/locations/{location-id}/parameters/{parameter-id}/$' (Location parameter detail endpoint)
