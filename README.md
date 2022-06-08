# Your Python Project

A python project is structured around a `setup`, which is described in a file, one of the files is `setup.py` that
must reside in your project root directory. `setup.py` will contain important metadata (data about data - your code) 
used to build your project.

Clone the example from GitHub to work locally:

```
git clone git@github.com:python-class-examples/python-deployment-blog.git
```

1. Enter the folder `python-deployment-blog` 
2. Create a virtual environment there with `python -m venv .venv`
3. Activate the virtual environment `. .venv/bin/activate`
4. Open the project folder with Pycharm. If you want you can do steps 2 and 3 in pycharm.
5. Please inspect the `setup.py` file
6. Modify it...
7. Modify some important aspects of the project, like the `package` and `subpackages` names

If you have a console script (`setup.py` console_scripts config) use `pip install -e .` to test it in 
your terminal.

After you finish the changes, try to build and upload your project to the PyPi test server. F
or that you can follow these commands, make sure to create a twine account:

- `pip install twine`
- `python setup.py sdist`
- `twine upload -r testpypi dist/*`

Share your package installation link generated in PyPi, so that we can test it.

## Now From Scratch

Now, try to create a new project and publish it by scratch from an empty directory. You can use pycharm and you can
take a look on the previous example if needed. 