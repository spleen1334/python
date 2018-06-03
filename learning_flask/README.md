# FLASK TUTORIAL

## Info
* Install venv and run the following for Flask instalation:
    ```shell
    virtualenv venv
    source venve/bin/activate
    pip install Flask
    ```
    
* Install gunicorn server
    ```shell
    pip install gunicorn
    ```

* Freeze pip packages
    ```shell
    pip freeze > requirements.txt
    ```

* Create Procfile for heroku and set it up:
    ```shell
    touch Procfile
    # inside Procfile add >> web: gunicorn route:app
    ```
