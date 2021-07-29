# Creating Python Package using Jupyter Notebook
 Creating your first data science python package straight from Jupyter Notebook.

![img](Images/pythonpackage.jpg)

> **Creating your first data science python package straight from Jupyter Notebook.**

[![View in Deepnote](https://deepnote.com/static/buttons/view-in-deepnote-white.svg)](https://deepnote.com/viewer/github/kingabzpro/Creating-Python-Package-using-Jupyter-Notebook/blob/main/python_packages.ipynb)

We are going to use the cloud Jupyter Notebook to ease the setting up of the environment and completely focus on creating a package. We have also used Object Orient Programming (OOP) fundamentals like Inheritance, objects, class, magic functions, and that I won't be discussing how each part work. I am sharing my experience of creating Python packages while taking AWS Machine Learning Foundations It took me 10 minutes to create a Python package once I knew who to build it, so practice will make you better at coding packages.

Have you wondered how Python packages like Scikit-learn, pandas, and NumPy are built? They are all based on OOP to create complex and easy-to-use packages. Why do data scientists need to build python packages? In modern times OOP is a necessity and it helps users to build program and share it with the public or within organizations.

# Creating ***__init__.py*** Function

We need to create `__init__.py` file in the distributions folder to initial the Classes within the python file. This will help us call specific classes directly.

We have inintaite Binomial and Gaussian class.

%%writefile distributions/__init__.py

from .binomial import Binomial

from .gaussian import Gaussian

```
Writing distributions/__init__.py 
```

# Creating *setup.py* Function

setup.py function giving all necessary information about the package. It uses setuptools library to create package name, version, description, author name, etc. We have to create this file outside the distribution folder.

%%writefile setup.py

from setuptools import setup

setup(name='distributions',

   version='0.2',

   description='Gaussian and Binomial distributions',

   packages=['distributions'],

   author = "Abid Ali Awan",

   author_email = "abidaliawan@rocketmail.com",

   zip_safe=False)

```
Writing setup.py 
```

# Directory

You can see how your directory should look like.

![Picture title](Images/image-20210724-124844.png)

# Installing distributions Package

Let's install the package by going into the Linux terminal and going into the work directory by using a cd. Then, use `pip install .` or `pip install -U .`

```
(venv) root@deepnote:~/work # pip install -U .
Processing /work
Building wheels for collected packages: distributions
  Building wheel for distributions (setup.py) ... done
  Created wheel for distributions: filename=distributions-0.2-py3-none-any.whl size=4800 sha256=39bc76cbf407b2870caea42b684b05efc15641c0583f195f36a315b3bc4476da
  Stored in directory: /tmp/pip-ephem-wheel-cache-ef8q6wh9/wheels/95/55/fb/4ee852231f420991169c6c5d3eb5b02c36aea6b6f444965b4b
Successfully built distributions
Installing collected packages: distributions
  Attempting uninstall: distributions
    Found existing installation: distributions 0.2
    Uninstalling distributions-0.2:
      Successfully uninstalled distributions-0.2
Successfully installed distributions-0.2
```

# Testing our Package

Let's test our package directly from the terminal and it seems like everything is working fine. Well done you have created your first python package.

```
>>> from distributions import Gaussian
>>> from distributions import Binomial
>>> 
>>> print(Gaussian(20,6))
mean 20, standard deviation 6
>>> print(Binomial(0.4,50))
mean 20.0, standard deviation 3.4641016151377544, p 0.4, n 50
>>> 
```
