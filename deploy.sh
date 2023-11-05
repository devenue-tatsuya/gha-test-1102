#!/bin/bash
echo "111111"

ls

echo "222222"

ls client/dist

echo "33333"


rsync -acvz --delete ./client/dist/my-app/ centos@ik1-305-12529.vs.sakura.ne.jp:/usr/share/nginx/html



echo "Hello, World!"