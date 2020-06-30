# Example with Cryptography library

## Configuring the environment


If you don't have pipenv in MAC:
````shell script
brew install pipenv
````

To create the environment and install the dependencies.

```sh
pipenv install --python 3.7
pipenv shell
pipenv install
```

To deactivate the environment:

```sh
exit 
```

## Run the program

To run the program:

```sh
pipenv shell
pipenv run start --port $YOUR_PORT
```

* **port**: is set by default to 5000.

## Test the API

Once the application is up and running you can request for `http://127.0.0.1:5010/users`.
Here is an example from postman:

![Request for users](docs/request_users.png)
