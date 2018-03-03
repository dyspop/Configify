# Configify

The app and package config generator package developed for developers who develop apps and/or packages.

Are you sick and tired of writing packages or apps that are super great but don't work unless your end-user scours your README for instructions on how to structure config files and how and where to instantiate them? 

Configify allows you to ship code and have the end-user developer install and configure it. You can call it from setup.py or bind it to whatever you like in your code.

## Installation

not yet...

## Usage

You put this code in your app/package

```diff
+ import Configify
+
+ template = {
+    'username': '',
+    'password': ''
+ }
+
+ Configify.make(template)
```

and the user will be prompted with

```diff
- 'username': 🔑
- Set username to **** in config.json
- 'password': 🔑
- Set password to **** in config.json

```

This will prompt the user for input and generate a `config.json`:

```
{"username": "whatevertheuserentered"}
```

By default Configify assumes a few things:

* Your inputs are secret
* You want the file generated at the path the python code that executes it runs from
* You don't want to return the configuration data to the application context.

But you can change that:

```diff
+ Configify.make(template, secret=False)
```
```diff
- 'username': ▋
- Set user to adifferetpassword in config.json
- 'password': ▋
- Set user to adifferetpassword in config.json


    Configify.make(template, path='~/Configs/')
    Configify.make(template, get=True)
    {'template': {'username': 'bobsyouruncle', password: 'steppintime'}}
