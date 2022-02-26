# Client REST API test

Small repository running a really simple REST API for test purposes.

Yet this server only owns a **Client** Resource with GET, PUT PATCH and DELETE endpoints.

You can interact with the API from the *test.py* file.

The Client resource owns an **id** (Integer) field working as a primary key in the SQL database and 3 other argument fields:

- **name**: String(100)
- **gender**: String(100)
- **age**: Integer

## "Build" the repository

If you want to clone and run this repository, make sure you have a Python Version higher than 3.6.

````bash
# "Build"
git clone https://github.com/CedricLeon/RESTAPITest.git
pip3 install -r requirements.txt
````

````bash
# In one shell: Run the API
python3 main.py
````

````bash
# In another shell: call the test file interacting with the API
python3 test.py
````

You can also create a **virtualenv** to install the dependences and run the API.