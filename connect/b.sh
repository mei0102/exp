#!/bin/bash

for i in `seq 1 12`
do
    cd mv_rinia_4_$i
    python ../between_ter1.py
    python ../jage.py
    cd ../
done