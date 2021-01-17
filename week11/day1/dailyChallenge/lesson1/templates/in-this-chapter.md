# What You Will Learn: 1


Imagine you have an application that needs the version 3 of the module  
beautiful soup, and another that needs the version 2,     
how can you use both of these applications ?  

As a working developer you often need to install different versions of the same library for different projects
Conflicts arising from having the wrong version of a dependency installed can cause long-term nightmares

# What Is Virtualenv ? 2

virtualenv is a tool that allows you to make isolated python environments.
It allows you to install packages inside it.

It creates an environment that has its own installation directories, that doesn’t share libraries with other virtualenv environments

# Installing Virtualenv 2

Installing virtualenv can be done with pip

$ pip install virtualenv

# How To Use Virtualenv 2

First, we need to create a virtual env, this can be done with:

$ virtualenv my_environment
What happened after you run this command ? * A new directory with your requested name (ie. here it’s my_environment) was created

# Activating Virtualenv 2

And then we just need to activate it by running:

On Unix:

$ source my_environnement/bin/activate
On Windows:

$ my_environnement/Scripts/activate
Notice that the your shell prompt has changed. It indicates which virtualenv is currently active.

# Deactivating Virtualenv 2

$ deactivate
Now you are ready to install packages and use them
