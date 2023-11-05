#!/bin/bash

rsync -acvz --delete ./client/dist/client/ centos@ik1-305-12529.vs.sakura.ne.jp:/usr/share/nginx/html

echo "Success!"