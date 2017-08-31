#!/usr/bin/env python
import os

def delete_file(filepath):
    os.remove(os.path.join(os.path.realpath(os.path.curdir), filepath))

if __name__ == '__main__':
    if '{{cookiecutter.create_vs_project}}'.lower() != 'y':
        delete_file('{{cookiecutter.app_name}}.pyproj')
