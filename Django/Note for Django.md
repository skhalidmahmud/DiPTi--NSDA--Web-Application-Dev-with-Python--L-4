# Django setup

For Django Documentation [Click here](https://docs.djangoproject.com/).

---

## Django Active on first time

>```Before starting: you need to install```[python 3.x.x,](https://www.python.org/downloads/)```any of code editor (here use Visual Studio Code)```[Visual Studio Code,](https://code.visualstudio.com/download)```For opening DB, download your preferred DB (here use SQLite)```[SQLite,](https://sqlitebrowser.org/dl/)```and all need to be the latest version.```

### Step 1: Create a folder (Django)

> ```Create a folder anywhere on your drive. Remember, it is too important, and we use that folder as our main root folder for our project.```

### Step 2: Make Environment for our project

##### 1. Open CMD

> You can open CMD from ```Ctrl+r``` and type ```cmd```, I open it from ```CMD on my VS Code```.

##### 2. Run make Environment command:

>You must be in our main root folder (here, <b>```Django```</b>)
Samle: ```C:\Users\Khalid\OneDrive\Desktop\Django> ```

```bash
python -m venv myEnv #this run on root folder for create Environment as myEnv
```

##### 3. Activate Environment from Scripts folder:

###### Open Scripts folder

```bash
cd ..\myEnv\Scripts #this for go Scripts folder from root folder
```

###### ⚠️ Remember: For activate, you must on Scripts Folder

```bash
activate #run this on Scripts folder in CMD
```

### Step 3: Install Django and Startproject

##### 1. Install Django (anywhere, but when active Environment):

> For confurm Install Django Environment are active or not
```txt
(my_venv) C:\Users\Khalid\OneDrive\Desktop\Django\my_venv\Scripts> #Here on most left '(my_venv)' indicate.
```

```bash
pip install django
```

##### 2. Go back root folder and startproject:

> Go back on root folder, for this

```bash
cd ../.. #(my_venv) C:\Users\Khalid\OneDrive\Desktop\Django>
```

```py
django-admin startproject myProject #for startproject, here myProject is a name for your project
```

### Step 4: Run Runserver:
##### Go back Project folder and runserver:


```bash
cd myProject #for go on manage.py
```

```bash
python manage.py runserver
```

##### Congrasulation!

```If all okey then congrasulation! You successfully run your first Django Project. for check it:```

###### 1. Go any brawser
###### 2. Copy it and and peast brawser
```txt
27.0.0.1:8000 #For home page
27.0.0.1:8000/admin #For admin page
```

###### ⚠️ WARNING: 

---

## Use Django reactvate

### 1. From previous but inactive project:

#### Step 1: 

#### Step 2:

### 2. From Git:

---

## Extra info for Django

### 1. 

### 2. 