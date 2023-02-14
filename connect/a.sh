#!/bin/bash

for i in `seq 0 12`
do
    echo "cd mv_rinia_4_$i"
    echo "python ../between_ter1.py"
    echo "python ../jage.py"
    echo "cd ../"
done