# use PowerShell instead of sh:
set shell := ["powershell.exe", "-c"]

# Default command to run test and linter
@default:
    docker-compose run --rm app sh -c "python manage.py test && ruff check"

# Run ruff linter
lint:
    docker-compose run --rm app sh -c "ruff check"

# Run ruff linter and fix issues
lint-fix:
    docker-compose run --rm app sh -c "ruff check --fix"

# Run ruff linter and format issues
format:
    docker-compose run --rm app sh -c "ruff format"

# Check if the code is formatted correctly
format-check:
    docker-compose run --rm app sh -c "ruff format  --check"

# Run tests
test:
    docker-compose run --rm app sh -c "python manage.py test"

# Make migrations for a specific app
makemigrations app="":
    docker-compose run --rm app sh -c "python manage.py makemigrations {{app}}"

# Apply migrations for a specific app
migrate app="":
    docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate {{app}}"

# Run shell in the app container
shell:
    docker-compose run --rm app sh -c "python manage.py shell -i ipython"

# Run manage.py commands
manage +command:
    docker-compose run --rm app sh -c "python manage.py {{command}}"

# Start the application in detached modeusing docker-compose
up:
    docker-compose up -d

# Stop the application using docker-compose
down:
    docker-compose down

# Rebuild the Docker image and restart the application
rebuild:
    docker-compose down
    docker-compose build
    docker-compose up -d 

# Show the logs for the app container
logs *args:
    docker-compose logs {{args}}