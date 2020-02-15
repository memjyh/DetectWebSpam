NAME='SpamWeb' #应用的名称
DJANGODIR=/webapps/detectWebSpam/WebDjango/SpamWeb #django项目的目录
SOCKFILE=/webapps/detectWebSpam/WebDjango/run/gunicorn.sock #使用这个sock来通信
USER=jyhweb
GROUP=webapps
NUM_WORKERS=3 #gunicorn使用的工作进程数
DJANGO_SETTINGS_MODULE=SpamWeb.settings #django的配置文件
DJANGO_WSGI_MODULE=SpamWeb.wsgi #wsgi模块
LOG_DIR=/webapps/detectWebSpam/WebDjango/logs #日志目录

echo "starting $NAME as `whoami`"

#激活python虚拟运行环境
cd $DJANGODIR
source deactivate
conda activate py27
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

#如果gunicorn.sock所在目录不存在则创建
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

#启动Django

exec /root/miniconda3/envs/py27/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=unix:$SOCKFILE \
    --access-logfile=${LOG_DIR}/gunicorn_access.log
