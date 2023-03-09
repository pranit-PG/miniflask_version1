flask installation

pip install Flask

project structure

flask_101 (project root)
    - README.md
    - requirements.txt
    - main.py 
Running flask application

flask --app <file-name> run

# DEBUG MODE
flask --app <file-name> run --debug

# CHANGING PORT
flask --app main1 run --debug --port 8000

# CHANGING HOST

 flask --app main1 run --host 0.0.0.0 --debug --port 8000
 # 0.0.0.0 is attached to your public IP