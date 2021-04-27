# ShortLink

This is an app for the URL Shortening.

## Requirements

* `docker >= 20.10.5`
* `docker-compose >= 1.29.0`

## Build

* Run `docker-compose build`

## Run

1. Copy `env.template` to `.env` file and update values as you want
2. Add your value used for `URL_APP` parameter before to `/etc/hosts` local dns file (ex. `sudo echo "127.0.0.1 short.link" >> /etc/hosts`)
3. Run `docker-compose up -d`
4. Check the application status `docker-compose ps`

## Usage

Depends what value you used in `.env` and `/etc/hosts` files you should be able to access the app using that (including the port) in the browser (ex. in our case is `short.link:5000`).

A list with the functionality of the app can be found in [list.todo](list.todo).

## Endpoints

* `/` - Add a long URL and all URL records
* `/delete/<short_url>` - Delete a short URL
