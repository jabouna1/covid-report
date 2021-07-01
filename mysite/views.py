#from django.http import HttpResponse;

from django.shortcuts import render; 
from . import data;



def index(request):
	
	context = {'update_Date' : data.updateDate, 'vaccineVar1' : data.vaccineStatus[0], 'vaccineVar2' : data.vaccineStatus[1],
	'vaccineEmoji' : data.vaccineEmoji, 'ageGroup' : data.mostDeathsGroup, 'deathStatus1' : data.deathStatus[0], 'deathStatus2' : data.deathStatus[1], 
	'deathEmoji' : data.deathEmoji, 'countyOfCaseIncrease' : data.caseIncreaseStatus[0], 'percentOfCaseIncrease' : data.caseIncreaseStatus[2], 
	'statusOfCaseIncrease' : data.caseIncreaseStatus[1], 'emojiOfCaseIncrease' : data.caseIncreaseEmoji, 'countyOfDeathIncrease' : data.deathIncreaseStatus[0],
	'percentOfDeathIncrease' : data.deathIncreaseStatus[2], 'statusOfDeathIncrease' : data.deathIncreaseStatus[1], 'emojiOfDeathIncrease' : data.deathIncreaseEmoji, 
	'countyOfCaseDecrease' : data.caseDecreaseStatus[0], 'percentOfCaseDecrease' : data.caseIncreaseStatus[2], 
	'statusOfCaseDecrease' : data.caseDecreaseStatus[1], 'emojiOfCaseDecrease' : data.caseDecreaseEmoji, 'countyOfDeathDecrease' : data.deathDecreaseStatus[0],
	'percentOfDeathDecrease' : data.deathDecreaseStatus[2], 'statusOfDeathDecrease' : data.deathDecreaseStatus[1], 'emojiOfDeathDecrease' : data.deathDecreaseEmoji};
	
	
	return render(request, 'mainpage.html', context);
	
	
