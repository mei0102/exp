#!/bin/bash

NUM=${10}
i=${0}
for i in `seq 1 10`
do
 ~/Scalable/qualnet/8.0/bin/qualnet mv_rinia_4_8.config seed$i -seed $i
done

# edit .sqlite in output.py
# *.config
# $i is experiment count
