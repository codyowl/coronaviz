# coronaviz
A dashboard to vizualise corona virus' stats

## How to run on local ?

    create a virtual env:
    virtualenv -p python3 <your_env>
    
    activate your env:
    source /<your_env_path>/bin/activate
    
    Install all the required packages:
    pip3 install -r requirements.txt
    
    Create a database on mysql with the name:
    create database coronaviz
    
    Now go inside the project root folder and type the following management commands:
    python manage.py makemigrations
    python manage.py migrate
    
    Run the project:
    python manage.py runserver
