#!/bin/bash

python outputcsv_cal.py

python analysis_cal.py



#端末間実験
python between_ter.py


#全体実験
python whole_ter.py
#↑端末数によって変える必要あり

python combine_cal_between.py
#↑端末数によって変える必要あり

python combine_cal.py
#↑端末数によって変える必要あり
