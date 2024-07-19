The OANDA v20 REST API provides programmatic access to OANDA's next generation
v20 trading engine.

Installation
############

Install using pip::

	pip install v20

If you don't wish to use pip::

	git clone https://github.com/oanda/v20-python.git

Documentation
#############

For documentation, usage and examples, see: http://developer.oanda.com/rest-live-v20/introduction
and https://github.com/oanda/v20-python-samples


[CoPilot]:
Yes, running setup.py is one way to install a Python package, including the v20-python package, especially if you're working with a version of the package that's not available on PyPI or if you're installing from a source code checkout. Running setup.py will install the package and its dependencies, making the modules available for use in your Python environment.

To install a package using setup.py, navigate to the directory containing setup.py in your terminal and run:

               $      python setup.py install

This command builds and installs the package. Alternatively, for a development installation (if you plan to modify the package), you can use:

               $      python setup.py develop


If you have already successfully installed the v20 package using ```  pip install v20  ```, you do not need to run python setup.py install or python setup.py develop for the purpose of installing the package. The pip install command fetches the package from PyPI (or another specified source) and installs it, handling dependencies automatically. This is generally the preferred method for installing Python packages.

The python setup.py install command is an alternative way to install the package, typically used when you have a local copy of the package source code and it may not be available on PyPI, or you want to install a modified version.

The python setup.py develop command is useful if you are developing the package, i.e., making changes to the source code. It installs the package in a way that allows you to edit the source code and have the changes immediately reflected in your environment, without needing to reinstall the package after each change.

In summary, if pip install v20 was successful and you're not planning to modify the v20 package source code, you do not need to run either python setup.py install or python setup.py develop.

