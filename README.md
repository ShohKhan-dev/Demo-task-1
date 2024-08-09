
## Setup

create .env file and copy everything from .env-sample to .env file


```
>>> pip install -r requirements.txt

```


## Run

```
>>> python manage.py runserver
```


## API Endpoints

```JSON
{
    "categories": "http://127.0.0.1:8000/api/categories/",
    "category": "http://127.0.0.1:8000/api/categories/{id}/",
    "category organizations": "http://127.0.0.1:8000/api/categories/{id}/organizations/",
    "category services": "http://127.0.0.1:8000/api/categories/{id}/services/",
    
    "services": "http://127.0.0.1:8000/api/services/",
    "service": "http://127.0.0.1:8000/api/services/{id}/",
    "service organizations": "http://127.0.0.1:8000/api/services/{id}/organizations/",
    "service profiles": "http://127.0.0.1:8000/api/services/{id}/profiles/",
    
    "profile-services": "http://127.0.0.1:8000/api/profile-services/",
    "profile-service": "http://127.0.0.1:8000/api/profile-services/{id}/",
    
    "profiles": "http://127.0.0.1:8000/api/profiles/",
    "profile": "http://127.0.0.1:8000/api/profiles/{id}/",
    "profile services": "http://127.0.0.1:8000/api/profiles/{id}/services/",
    
    "organization-services": "http://127.0.0.1:8000/api/organization-services/",
    "organization-service": "http://127.0.0.1:8000/api/organization-services/{id}/",
    
    "portfolio-images": "http://127.0.0.1:8000/api/portfolio-images/",
    "portfolio-image": "http://127.0.0.1:8000/api/portfolio-images/{id}/",
    
    "organizations": "http://127.0.0.1:8000/api/organizations/",
    "organization": "http://127.0.0.1:8000/api/organizations/{id}/",
    "organization profiles": "http://127.0.0.1:8000/api/organizations/{id}/profiles/",
    "organization portfolio images": "http://127.0.0.1:8000/api/organizations/{id}/portfolio_images/",
    "organization services": "http://127.0.0.1:8000/api/organizations/{id}/services/",
}

```