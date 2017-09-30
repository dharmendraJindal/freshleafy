from fabric.api import env, run, cd
from fabric.colors import green, red, yellow

env.user = "webadmin"
env.hosts = ["172.104.177.182"]

def deploy():
    print "DEPLOYING ============******************************************"
    with cd('public/jindalfresh/freshleafy'):
        with_virtualenv()
        run("git pull")
        # run("pip install -r settings/requirements.pip")

        print "Reloading project......................"
        run("sudo service supervisor stop")
        run("sudo service supervisor start")

    print "Done============******************************************"

def migrate():
    print "Running migrations============******************************************"
    with cd('public/jindalfresh/freshleafy'):
        with_virtualenv()
        run("python manage.py migrate")
    print "Done============******************************************"
#
def with_virtualenv():
    run('source /home/webadmin/.virtualenvs/jindalfresh/bin/activate')
