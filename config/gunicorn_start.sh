#!/bin/bash
NAME="freshleafy"                                  # Name of the application
DJANGODIR=/home/webadmin/public/jindalfresh/freshleafy            # Django project directory
SOCKFILE=/home/webadmin/public/jindalfresh/freshleafy/run/gunicorn.sock  # we will communicte using this unix socket
USER=webadmin                                        # the user to run as
GROUP=webadmin                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=settings.common             # which settings file should Django use
DJANGO_WSGI_MODULE=settings.wsgi                     # WSGI module name
echo "Starting $NAME as `whoami`"
#
# Activate the virtual environment
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
#
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
#
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-