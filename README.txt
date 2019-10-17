----This project was created by Django----

***********

To config this project, do follow these steps:

1. Activate virtual environment to create an isolated environment for Django:

- It's like Docker so if you are using Docker, forget this.
- To activate, open terminal in root folder and run ". env/bin/activate" then you will see "(env)" at the begining of each command line.

2. Install all required packages:

- Open terminal in the root folder and run "pip3 install -r requirements.txt"

3. Run project:

- get in 'userlookup' folder and run "python3 manage.py runserver"

4. Observe result:

- Go to url "127.0.0.1:8000/userlookup/admin" to add more user, using this information: 
 + username: user
 + password: user

- Go to url "127.0.0.1:8000/userlookup/" to show data

*********

**NOTE**:
- You won't see the page reset when hitting refresh :v
- If you intend to run this project on cloud, make searching for "deploy django project on <somewhere> "
