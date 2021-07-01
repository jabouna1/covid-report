import time;
from threading import Thread;
from . import data;
from datetime import date;

def update():
	while(True):
		data.getVaccineData();
		data.getAgeGroupData();
		data.getCountyMessages();
		data.updateDate = str(date.today());
		#Updates every week
		time.sleep(604800);


t = Thread(target=update, args=());
t.start();
	




