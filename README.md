# Configify

The app and package config generator package developed for developers who develop apps and/or packages.

Are you sick and tired of writing packages or apps that are super great but don't work unless your end-user scours your README for instructions on how to structure config files and how and where to instantiate them? 

Configify allows you to ship code and have the end-user developer install and configure it. You can call it from setup.py or bind it to whatever you like in your code.

## Installation

not yet...

## Usage

You put this code in your app/package

    import Configify
    template = {
        'username': '',
        'password': ''
    }   
    Configify.make(template)

and the user will be prompted with

    >>>'username': 🔑
    Set username to **** in config.json
    >>>'password': 🔑
    Set password to **** in config.json

and generate a `config.json` file:

    {"username": "someuser", "password": "somepassword"}

By default Configify assumes a few things:

* You want the file to be named `config.json`
* Your inputs are secret
* You want the file generated at the path the python code that executes it runs from
* You don't want to return the configuration data to the application context.

But you can change any of that:

```Configify.make(data=template, filename='secret.json')
```
```Configify.make(data=template, secret=False)
>>>'username': ▋
Set user to someusername in config.json
>>>'password': ▋
Set password to somepassword in config.json
```
```Configify.make(data=template, path='~/Configs/')
>>>'username': 🔑
Set username to ************ in ~/Configs/config.json
>>>'password': 🔑
Set password to ************ in ~/Configs/config.json
```
```Configify.make(data=template, get=True)
>>>'username': 🔑
Set username to **** in config.json
>>>'password': 🔑
Set password to **** in config.json
{'template': {'username': 'someusername', password: 'somepassword'}}
```
