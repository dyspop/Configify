# Configify

The app and package config generator package developed for developers who develop apps and/or packages.

Are you sick and tired of writing packages or apps that are super great but don't work unless your end-user scours your README for instructions on how to structure config files and how and where to instantiate them? 

Configify allows you to ship code and have the end-user developer install and configure it. You can call it from setup.py or bind it to whatever you like in your code.

## Installation

pip install git+git://github.com/dyspop/Configify

## Usage

You put this code in your app/package

    import Configify

    template = {
        'username': 'default',
        'password': 'anotherdefault'
    }

    Configify.make(template)

To generate a configuration and load it into the app context otherwise just use:

    config = Configify.make(template, get=True)

and the user will be prompted with

    >>>Enter value for "username": 
    🔑
    Set username to ************** in config.json
    >>>Enter value for "password":
    🔑
    Set password to ****************** in config.json

and generate a `config.json` file:

    {"username": "frominputabove", "password": "alsofrominputabove"}

By default Configify assumes a few things:

* You want the file to be named `config.json`
* Your inputs are secret
* You want the file generated at the path the python code that executes it runs from
* You don't want to return the configuration data to the application context
* You want the obscuring character to be an asterisk

But you can change any of that:


```
>>>Configify.make(data=template, filename='secret.json')
Enter value for "username"
(return for default "*******")': 
🔑
Set "username" to "***********" in secret.json
Enter value for "password"
(return for default "***********")': 
🔑
Set "password" to "*****" in secret.json
```
```
>>>Configify.make(data=template, secret=False)
Enter value for "username"
(return for default "someusername")': 
▋userinput
Set "username" to "userinput" in config.json
Enter value for "password"
(return for default "somepassword")': 
▋otheruserinput
Set "password" to "otheruserinput" in config.json
```
```
>>>Configify.make(data=template, path='~/Configs/')
Enter value for "username"
(return for default "*******")': 
🔑
Set "username" to "***********" in config.json
Enter value for "password"
(return for default "***********")': 
🔑
Set "password" to "*****" in ~/Configs/config.json
```
```
>>>Configify.make(data=template, get=True')
Enter value for "username"
(return for default "*******")': 
🔑
Set "username" to "***********" in config.json
Enter value for "password"
(return for default "***********")': 
🔑
Set "password" to "*****" in config.json
{'template': {'username': 'userinput', password: 'otheruserinput'}}
```
```
>>>Configify.make(data=template, char='ﷺ')
>>>Enter value for "username": 
🔑
Set username to "ﷺﷺﷺﷺﷺﷺﷺﷺﷺ" in config.json
>>>Enter value for "password":
🔑
Set password to "ﷺﷺﷺﷺﷺﷺﷺﷺﷺﷺ" in config.json
```

## Contributing

Fork the source repository https://github.com/dyspop/Configify make a new branch and submit a pull request.
