# Configify

The app/package config generator package developed for developers who develop apps/packages and developers who develop apps/packages for developers! 

## Installation

not yet...

## Usage

    import Configify

    template = {
        'username': '',
        'password': ''
    }

    Configify.make(template)

This will prompt the user for input and generate a `config.json`.

By default Configify assumes a few things:

* Your inputs are secret
* You want the file generated at the path the python code that executes it runs from
* You don't want to return the configuration data to the application context.

But you can change that:

    Configify.make(template, secret=False)
    Configify.make(template, path='~/Configs/')
    Configify.make(template, get=True)
    {'template': {'username': 'bobsyouruncle', password: 'steppintime'}}
