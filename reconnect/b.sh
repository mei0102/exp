#!/bin/bash

for i in `seq 13 15`
do
    cd mv_rinia_4_$i
    python ../between_ter1.py
    python ../jage.py
    cd ../
done