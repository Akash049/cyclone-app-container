# Cyclone Project
Cyclone backend server

## Contributors
* Akash Chandra

| Key | Value |
|----------|------------|
| username | root | 
| email | info@cyclone.com | 
| password | qwertyqwerty | 

## Packages
| Name | Versions |
|----------|------------|
| Django | 2.2.1 | 
| Celery | 4.4.6 | 
| Redis | 3.4.1 |
| Beautifulsoup4 | 4.9.1 | 
| psycopg2-binary | 2.8 | 
| Coverage | 3.6 |

## Commands
docker-compose up -d --build

## API Enndpoints
| Name | TYPE | Endpoint | 
|----------|----|------------|
| Fetch All Data | GET | /forecast/all/ |
| Delete All Data| GET | /forecast/delete_all/ |
