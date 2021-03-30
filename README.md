# B Blog

B Blog is a site similar to the early versions of instagram where users can make posts and follow different users

# Tech Stack

Django <br>
PostgreSQL <br>
Bootstrap <br>

## Installation

Make sure python 3 + is installed on your devices

```bash
python -m venv venv
venv\Scripts\activate
cd blog
pip install -r requirements.txt 
py manage.py migrate
```
To connect to postgres Database please find the settings.py file in blog/blog/ and enter password, port,  username and database <br>
![image](https://user-images.githubusercontent.com/47046091/111366856-72772b80-866a-11eb-9cbc-2e392910adfb.png)

## Usage

```bash
py manage.py runserver

```
## Features
<ul>
  <li>Pagination</li>
  <li>Image Uploading</li>
  <li>Protected Auth Routes</li>
  <li>Following / Unfollowing user</li>
</ul>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
