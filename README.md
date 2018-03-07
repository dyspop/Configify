# Configify

Are you sick and tired of writing packages or apps that are super great but don't work unless your end-user scours your README for instructions on how to structure config files and how and where to instantiate them? 

Configify is the app and package configuration generator package developed for developers who develop apps and/or packages for use by other developers.

Configify allows you to ship code and have the end-user developer install and configure it just by running your app or package. You can call it from setup.py or bind it to whatever you like in your code so the results of the new configuration are made immediately available to whatever context the app or package will be used in.

---

## Warning

This software is in alpha development. This should work, please report bugs. 

Key caveats:
* Outputs your configuration data to the screen in some cases.
* Only supports json
* Only available for python.
* You want this module to prompt from TTY. 

These are intended to be developed further, but in this state it should be useful nonetheless.

## Installation

    pip install git+git://github.com/dyspop/Configify

## Usage

To just prompt your end user, you put this code in your app/package:

    import Configify

    template = {
        'username': 'default',
        'password': 'anotherdefault'
    }

    Configify.make(template)

To generate a configuration and load the new configuration data into the app context otherwise just use:

    config = Configify.make(template, get=True)

and the end user will be prompted with:

    Enter value for "username"
    (return for default "default")': ▋userinput
    Enter value for "username"
    (return for default "default")': 
    Set "username" to "userinput" in config.json
    Enter value for "password"
    (return for default "anotherdefault")': ▋anotheruserinput
    Enter value for "password"
    (return for default "anotherdefault")': 
    Set "password" to "anotheruserinput" in config.json

and generate a `config.json` file:

    {"username": "userinput", "password": "anotheruserinput"}

By default Configify assumes a few things:

* You want the file to be named `config.json`
* You want the file generated at the path the python code that executes it runs from
* You don't want to return the configuration data itself to the application context
* The user interface is TTY. 

But you can change most of that:


```
template = {
    'PORT': '3000',
    'DEBUG': 'True'
}
Configify.make(data=template, filename='appconfig.json')
Enter value for "PORT"
(return for default "3000")': ▋8080
Set "PORT" to "8080" in appconfig.json
Enter value for "DEBUG"
(return for default "True")': ▋False
Set "DEBUG" to "False" in appconfig.json
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
