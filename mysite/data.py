import csv;
import random;
import urllib.request as ur;
import pandas as pd;
from datetime import date
from matplotlib import rcParams
import matplotlib.pyplot as plt;

#Change font style of plots
plt.rcParams['font.family'] = 'sans-serif';
plt.rcParams['font.sans-serif'] = 'Calibri';
plt.rcParams['font.size'] = 14
plt.rcParams['text.color'] = '#3d405b';
plt.rcParams['font.weight'] = 'bold';



#Status
status = ["VAST MAJORITY", "MAJORITY", "SLIGHT MAJORITY", "HAVE", "HAVE NOT", "LARGE INCREASE", "INCREASE", "SLIGHT INCREASE","LARGE DECREASE", "DECREASE", "SLIGHT DECREASE"];
#Corresponds with status above
emojiFiles = ['svg/1F389.svg', 'svg/1f60a.svg','svg/1F60F.svg','svg/1F644.svg','svg/1F912.svg','svg/1F62D.svg'];
#Date (Moved to update loop)
#updateDate = str(date.today());

#Vaccines=======================
totalVaccineStarted = 0;
totalVaccineCompleted = 0;
percentVaccineCompleted = 0;
vaccineStatus = ["",""];
vaccineEmoji = "";

#Age Group Deaths================ 
ageGroups = ["0-19", "20-29","30-39","40-49","50-59","60-69", "70-79","80+"];
#Corrosponds with age groups above 
ageDeathCounts = [0,0,0,0,0,0,0,0];
mostDeathsGroup = "";
prevAgeDeathCounts = [0,0,0,0,0,0,0,0];
deathStatus = ["",""];
deathEmoji = "";

#County Mechanical Messages=========
counties = [];
cases = [];
caseRates = []
deaths = [];
prevCases = [];
prevDeaths = [];
caseRates = [];
deathRates = [];
prevCaseRates = [];
prevDeathRates = [];

caseIncreaseStatus = ["", "", ""];
caseIncreaseEmoji = "";

deathIncreaseStatus = ["", "", ""];
deathIncreaseEmoji = "";


caseDecreaseStatus = ["", "", ""];
caseDecreaseEmoji = "";

deathDecreaseStatus = ["", "", ""];
deathDecreaseEmoji = "";

def getVaccineData():
	global totalVaccineStarted, totalVaccineCompleted, percentVaccineCompleted, status, vaccineStatus, emojiCode, vaccineEmoji;
	
	
	#Gets csv files from source and uses panda library to get dataframe
	url = "https://coronavirus.ohio.gov/static/dashboards/vaccine_data.csv";
	vaccineData = ur.urlopen(url);
	df = pd.read_csv(vaccineData, usecols=["county","vaccines_started","vaccines_completed"]);
	
	#sums up vaccines started/completed 
	for x in df["vaccines_started"]:
		totalVaccineStarted += x;
		
	for x in df["vaccines_completed"]:
		totalVaccineCompleted += x;
	
	#percent complete
	percentVaccineCompleted = int(totalVaccineCompleted/totalVaccineStarted * 100);
	
	#severity by intervals
	pvc = percentVaccineCompleted;
	if(pvc >= 83 and pvc <= 100):
		vaccineStatus[0] = status[0];
		vaccineStatus[1] = status[3];
		vaccineEmoji = emojiFiles[0];
	elif(pvc >= 67 and pvc <= 82):
		vaccineStatus[0] = status[1];
		vaccineStatus[1] = status[3];
		vaccineEmoji = emojiFiles[1];
	elif(pvc >= 50 and pvc <= 66):
		vaccineStatus[0] = status[2];
		vaccineStatus[1] = status[3];
		vaccineEmoji = emojiFiles[2];
	elif(pvc >= 34 and pvc <= 49):
		vaccineStatus[0] = status[2];
		vaccineStatus[1] = status[4];
		vaccineEmoji = emojiFiles[3];
	elif(pvc >= 17 and pvc <= 33):
		vaccineStatus[0] = status[1];
		vaccineStatus[1] = status[4];
		vaccineEmoji = emojiFiles[4];
	elif(pvc >= 0 and pvc <= 16):
		vaccineStatus[0] = status[0];
		vaccineStatus[1] = status[4];
		vaccineEmoji = emojiFiles[5];
	
	
	
	#Creating pie chart
	plt.figure();
	labels = ['COMPLETED', 'ONLY STARTED'];
	sizes = [percentVaccineCompleted, 100 - percentVaccineCompleted];
	colors = ['#81b29a','#f4f1de'];
	explode = (0, 0);
	plt.pie(sizes, colors = colors, explode=explode, labels=labels,autopct='%1.1f%%', shadow=False, startangle=90);

	plt.axis('equal')
	#plt.show()
	plt.savefig('mysite/static/piechart.png',transparent=True);
	
	return();
	
def getAgeGroupData():

	global status, emojiFiles, deathStatus, deathEmoji, ageGroups, ageDeathCounts, mostDeathsGroup, prevAgeDeathCounts; 
	#Save last weeks data
	prevAgeDeathCounts = ageDeathCounts.copy();
	
	
	#Gets csv files from source and uses panda library to get dataframe
	url = "https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv";
	vaccineData = ur.urlopen(url);
	df = pd.read_csv(vaccineData, usecols=["Age Range","Death Due To Illness Count - County Of Residence"]);
	
	#Summing up deaths per age group
	for x in range(len(df["Age Range"])): 
		age = df["Age Range"][x];
		if(age == "0-19"):
			ageDeathCounts[0] += df["Death Due To Illness Count - County Of Residence"][x];
		elif(age == "20-29"):
			ageDeathCounts[1] += df["Death Due To Illness Count - County Of Residence"][x];
		elif(age == "30-39"):
			ageDeathCounts[2] += df["Death Due To Illness Count - County Of Residence"][x];	
		elif(age == "40-49"):
			ageDeathCounts[3] += df["Death Due To Illness Count - County Of Residence"][x];
		elif(age == "50-59"):
			ageDeathCounts[4] += df["Death Due To Illness Count - County Of Residence"][x];
		elif(age == "60-69"):
			ageDeathCounts[5] += df["Death Due To Illness Count - County Of Residence"][x];
		elif(age == "70-79"):
			ageDeathCounts[6] += df["Death Due To Illness Count - County Of Residence"][x];
		elif(age == "80+"):
			ageDeathCounts[7] += df["Death Due To Illness Count - County Of Residence"][x];
	
	mostDeathsGroup = ageGroups[ageDeathCounts.index(max(ageDeathCounts))];
	
	#Make bar graph
	plt.figure();
	plt.bar(ageGroups, ageDeathCounts, color=['#81b29a','#3d405b']);
	plt.xlabel("AGE GROUP");
	plt.ylabel("DEATHS");
	plt.savefig('mysite/static/bargraph.png',transparent=True);
	
	#FOR TESTING PURPOSES COMMENT OUT LATER
	prevAgeDeathCounts = randForTest(prevAgeDeathCounts,ageDeathCounts,200);
	
	#Finding percent change of deaths and create mechanical message
	alarmingChange = getLargestPercentChange(prevAgeDeathCounts,ageDeathCounts);
	deathStatus[1] = ageGroups[alarmingChange[0]];
	
	if(alarmingChange[1] > 66):
		deathStatus[0] = status[5];
		deathEmoji = emojiFiles[5];
	elif(alarmingChange[1] >= 33 and alarmingChange[1] <= 66):
		deathStatus[0] = status[6];
		deathEmoji = emojiFiles[4];
	elif(alarmingChange[1] >= 0 and alarmingChange[1] < 33):
		deathStatus[0] = status[7];
		deathEmoji = emojiFiles[3];
	
	return(); 

def getCountyMessages():
	global counties, cases, deaths, prevCases, prevDeaths, caseRates, deathRates, prevCaseRates, prevDeathRates, caseIncreaseStatus, caseDecreaseStatus, deathDecreaseStatus, deathIncreaseStatus;
	global caseIncreaseEmoji, caseDecreaseEmoji, deathDecreaseEmoji, deathIncreaseEmoji;
	
	prevCases = cases.copy();
	prevDeaths = deaths.copy();
	prevCaseRates = caseRates.copy();
	prevDeathRates = deathRates.copy();
	
	cases.clear();
	deaths.clear();
	caseRates.clear();
	deathRates.clear();
	
	url = "https://github.com/nytimes/covid-19-data/raw/master/live/us-counties.csv";
	vaccineData = ur.urlopen(url);
	df = pd.read_csv(vaccineData, usecols=["county","state","cases","deaths"]);
	
	for x in range(len(df["county"])):
		if(df["state"][x] == "Ohio"):
			counties.append(df["county"][x]);
			cases.append(df["cases"][x]);
			deaths.append(df["deaths"][x]);
	
	#FOR TESTING PURPOSES REMOVE LATER
	prevCases = randForTest(prevCases, cases, 500);
	prevDeaths = randForTest(prevDeaths, deaths, 500);
	
	#Get rates
	for x in range(len(cases)):
		caseRates.append(cases[x] - prevCases[x]);
		deathRates.append(deaths[x] - prevDeaths[x]);
	
	#ALSO TESTING REMOVE LATER
	for x in range(len(caseRates)):
		prevCaseRates.append(caseRates[x] + random.randint(-50,50));
		prevDeathRates.append(deathRates[x] + random.randint(-50,50));
	
	#Getting mechanical message data
	alarmingCountyCaseIncrease = getLargestPercentChange(prevCaseRates, caseRates);
	alarmingCountyDeathIncrease = getLargestPercentChange(prevDeathRates, deathRates);
	
	alarmingCountyCaseDecrease = getLargestPercentChange(caseRates, prevCaseRates);
	alarmingCountyDeathDecrease = getLargestPercentChange(deathRates, prevDeathRates);
	
	#County bad increases
	caseIncreaseStatus[0] = counties[alarmingCountyCaseIncrease[0]].upper();
	caseIncreaseStatus[2] = int(alarmingCountyCaseIncrease[1]);
	if(alarmingCountyCaseIncrease[1] > 66):
		caseIncreaseStatus[1] = status[5];
		caseIncreaseEmoji = emojiFiles[5];
		
	elif(alarmingCountyCaseIncrease[1] >= 33 and alarmingCountyCaseIncrease[1] <= 66):
		caseIncreaseStatus[1] = status[6];
		caseIncreaseEmoji = emojiFiles[4];
		
	elif(alarmingCountyCaseIncrease[1] >= 0 and alarmingCountyCaseIncrease[1] < 33):
		caseIncreaseStatus[1] = status[7];
		caseIncreaseEmoji = emojiFiles[3];
		
	deathIncreaseStatus[0] = counties[alarmingCountyDeathIncrease[0]].upper();
	deathIncreaseStatus[2] = int(alarmingCountyDeathIncrease[1]);
	if(alarmingCountyDeathIncrease[1] > 66):
		deathIncreaseStatus[1] = status[5];
		deathIncreaseEmoji = emojiFiles[5];
		
	elif(alarmingCountyDeathIncrease[1] >= 33 and alarmingCountyDeathIncrease[1] <= 66):
		deathIncreaseStatus[1] = status[6];
		deathIncreaseEmoji = emojiFiles[4];
		
	elif(alarmingCountyDeathIncrease[1] >= 0 and alarmingCountyDeathIncrease[1] < 33):
		deathIncreaseStatus[1] = status[7];
		deathIncreaseEmoji = emojiFiles[3];
	
	#County good decreases
	caseDecreaseStatus[0] = counties[alarmingCountyCaseDecrease[0]].upper();
	caseDecreaseStatus[2] = int(alarmingCountyCaseDecrease[1]);
	if(alarmingCountyCaseDecrease[1] > 66):
		caseDecreaseStatus[1] = status[8];
		caseDecreaseEmoji = emojiFiles[0];
		
	elif(alarmingCountyCaseDecrease[1] >= 33 and alarmingCountyCaseDecrease[1] <= 66):
		caseDecreaseStatus[1] = status[9];
		caseDecreaseEmoji = emojiFiles[1];
		
	elif(alarmingCountyCaseDecrease[1] >= 0 and alarmingCountyCaseDecrease[1] < 33):
		caseDecreaseStatus[1] = status[10];
		caseDecreaseEmoji = emojiFiles[2];
		
	deathDecreaseStatus[0] = counties[alarmingCountyDeathDecrease[0]].upper();
	deathDecreaseStatus[2] = int(alarmingCountyDeathDecrease[1]);
	if(alarmingCountyDeathDecrease[1] > 66):
		deathDecreaseStatus[1] = status[8];
		deathDecreaseEmoji = emojiFiles[0];
		
	elif(alarmingCountyDeathDecrease[1] >= 33 and alarmingCountyDeathDecrease[1] <= 66):
		deathDecreaseStatus[1] = status[9];
		deathDecreaseEmoji = emojiFiles[1];
		
	elif(alarmingCountyDeathDecrease[1] >= 0 and alarmingCountyDeathDecrease[1] < 33):
		deathDecreaseStatus[1] = status[10];
		deathDecreaseEmoji = emojiFiles[2];
	
	
	
	
	
	return();

#Creates fake data by taking a list and fluctuating numbers randomly
def randForTest(list, exampleList, maxChange):
	if(len(list) > 0):
		for x in range(len(exampleList)):
			list[x] = exampleList[x] - random.randint(0,maxChange);
			
	elif(len(list) == 0):
		for x in range(len(exampleList)):
			list.append(exampleList[x] - random.randint(0,maxChange));
	return list;
		

#Returns largest % change as well as index of that change in array format
def getLargestPercentChange(initialList, finalList):
	maxChange = 0.0;
	index = 0;
	
	for x in range(len(initialList)):
		if(finalList[x] != initialList[x] and initialList[x] != 0):
			change = (finalList[x]-initialList[x])/initialList[x] * 100.0;
		else:
			change = 0.0;
		
		if(change > maxChange):
			maxChange = change;
			index = x;
	
	return([index,maxChange]);
	


