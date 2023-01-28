# Django Mpesa STK push
## Links:
- [Youtube Tutorial](https://www.youtube.com/watch?v=CKFu3229p9Q&t=24s&ab_channel=FortuneDevAcademy)
- [Github Source Code](https://github.com/Fortune-dot/Django-STK-Push)
- [Github Daraga](https://github.com/Fortune-dot/django-daraja)
- [Safaricom Daraje](https://developer.safaricom.co.ke/)

## 1.SETTING UP 
- 1 .1 create a virtual environment named .venv based on your current interpreter:
   
    ```
    # Linux
    sudo apt-get install python3-venv    # If needed
    python3 -m venv .venv
    source .venv/bin/activate

    # macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    py -3 -m venv .venv
    .venv\scripts\activate
    ```

- 1.2 Activate virtual environment:

```
    .venv\Scripts\Activate 
```

- 1.2 Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.
- 1.3 In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:
- 1.4 The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:

- 1.5 Update pip in the virtual environment by running the following command in the VS Code Terminal:

```
    python -m pip install --upgrade pip
```

- 1.6 Install Django in the virtual environment by running the following command in the VS Code Terminal:

```
    python -m pip install django
```

## INSTALLATIONS 
- install the following:

```
pip install django_daraja
pip install django-rest-framework
```

- Exporting requirements:

```
	pip freeze > requirements.txt
```

- Installing requirements:

```
	pip install -r requirements.txt
```

## 2.CREATING AND RUNNING DJANGO PROJECT
- 2.1 Create the Django project
In the VS Code Terminal where your virtual environment is activated, run the following command:

```
    django-admin startproject project
```

- 2.2 Create an empty development database by running the following command:

```
    python manage.py migrate
```

- navigate to mongo_django_project by typing:

```
    cd project
```
- 2.3 To verify the Django project, make sure your virtual environment is activated, then start Django's development server using the command:

```
     python manage.py runserver
```

- 2.4 Ctrl+click the http://127.0.0.1:8000/ URL in the terminal output window to open your default browser to that address.


## 3. CREATING DJANGO APP
- 3.1 In the VS Code Terminal with your virtual environment activated, run the administrative utility's startapp command in your project folder (where manage.py resides):

```
    python manage.py startapp app
```
 

 # API
 ## 1. Using Browser
-  To make an STK Push using the browser, run the following url in browser:

```
http://127.0.0.1:8000/
```
- If successful, response will be:

```
{
  "MerchantRequestID": "119407-226353936-1",
  "CheckoutRequestID": "ws_CO_28012023102652950797292290",
  "ResponseCode": "0",
  "ResponseDescription": "Success. Request accepted for processing",
  "CustomerMessage": "Success. Request accepted for processing"
}
```

<br>

## 2. Using Postman
1. Create User
- Endpoint ->  http://127.0.0.1:8000/users
- request:

```
{
    "name": "Martin",
    "amount": 1,
    "phone": "0797292290"
}
```

- expected response:

```
{
    "id": 1,
    "name": "Martin",
    "phone": "0797292290",
    "amount": 1,
    "created_at": "2023-01-28T08:21:15.716136Z"
}
```

