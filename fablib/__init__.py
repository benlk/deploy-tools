import os

from fabric.api import *
from fabric import colors

from local import *
from vagrant import *
from wordpress import fetch_sql_dump, install_wordpress, verify_prerequisites, deploy as _wp_deploy
from wordpress.migrations import *
from helpers import _search_replace as search_replace

# Deployment related
env.path = ''
env.dry_run = False

def stable():
    """
    Work on stable branch.
    """
    print(colors.green('On stable'))
    env.branch = 'stable'


def master():
    """
    Work on development branch.
    """
    print(colors.yellow('On master'))
    env.branch = 'master'


def branch(branch_name):
    """
    Work on any specified branch.
    """
    print(colors.red('On %s' % branch_name))
    env.branch = branch_name


def rollback():
    """
    Deploy the most recent rollback point.
    """
    print(colors.red('Rolling back last deploy'))
    env.branch = 'rollback'


def path(path):
    """
    Specify the project's path on remote server.
    """
    env.path = path


def dry_run():
    """
    Don't transfer files, just output what would happen during a real deployment.
    """
    env.dry_run = True

def deploy():
    """
    Deploy local copy of repository to target environment.
    """
    require('branch', provided_by=[master, stable, branch, ])
    _wp_deploy()
