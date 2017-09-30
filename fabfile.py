from fabric.api import env, run, cd
from fabric.colors import green, red, yellow

env.user = "webadmin"
env.hosts = ["172.104.177.182"]

def deploy():
    print "DEPLOYING============******************************************"
    with cd('public/jindalfresh/freshleafy'):
        with_virtualenv()
        run("git pull")
        run("pip install -r settings/requirements.pip")

        print "Reloading project......................"
        run("sudo supervisorctl reread")
        run("sudo supervisorctl update")

        print "Done============******************************************"

def shell():
    local('python manage.py shell')


def test_dev():
    run('ls /home/webadmin')

def project_dir():
    cd('/home/webadmin/public/jindalfresh/freshleafy')

def with_virtualenv():
    run('source /home/webadmin/.virtualenvs/jindalfresh/bin/activate')
