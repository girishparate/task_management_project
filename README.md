step 1 : First, you need to pull / clone the repository to the local machine 
step 2 : install all the requirements from requirements.txt using following command
          NOTE : create virtual environment before entering any command
          
          pip install -r requirements.txt
          
step 3 : To start with the database, you need to run following commands, 
          
          python manage.py makemigrations
          
step 4 : Now, to migrate all the migrations files to the database, you need to put below command,
          python manage.py migrate

          
step 5 : To start with the project, we need to start django server where the project configuration folder is present.
          Go to the directory and run following command 
          python manage.py runserver

          
step 6 : In your browser, you will be able to check the project with localhost:8000 port number and you will be able to login and register on the project


step 7 : After successfull registration, and login, we can create task and edit them in the task details page and also there is an option to delete the task
