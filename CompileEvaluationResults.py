#!/usr/bin/env python3

import pandas as pd
import math

FILE_IN  = "Experiment_Results.xlsx"
FILE_OUT ='EvaluationFinal2_{sheet_name}.xlsx'
#FILE_OUT ='Evaluation.xlsx'

FORMAT_IN = 'csv'
if FILE_IN.endswith('.xlsx'):
    FORMAT_IN = 'xlsx'
FORMAT_OUT = 'csv'
if FILE_OUT.endswith('.xlsx'):
    FORMAT_OUT = 'xlsx'

variable_range_time=1
variable_range_balancing=0.15

if FORMAT_IN == 'xlsx':
    data = pd.read_excel(FILE_IN, engine='openpyxl')
else:
    data = pd.read_csv(FILE_IN)

data = data.drop(['# of Waypoints','Error distance (Source)', 'Error distance (FollowUp)',
                 'Distance to the car Follow up', 'Distance to the car Source','Source exec time',
                 'Follow up exec time'  ],axis=1)

print("Data loaded")
i=0
time=[]
balancing=[]
nTest=100

td="PASS"
to="PASS"
td_fdr="PASS"
to_fdr="PASS"

MRIP_1_1_Data=[]
MRIP_1_2_Data=[]
MRIP_1_3_Data=[]
MRIP_2_Data=[]
MRIP_3_Data=[]
MRIP_4_Data=[]
result_1_1=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_1_2=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_1_3=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_2=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_3=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_4=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_1_1_FDR=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_1_2_FDR=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_1_3_FDR=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_2_FDR=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_3_FDR=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})
result_4_FDR=pd.DataFrame({'Model': [], 'MRIP': [], 'TestCase': [],'TD Verdict': [],'TO Verdict': []})


#DIVIDIR DATA POR CADA MRIP
for i in range(0,len(data)):
    if data.loc[i,"MRIP"]=="MRIP1_1":
        MRIP_1_1_Data.append(data.loc[i,:])
    elif data.loc[i,"MRIP"]=="MRIP1_2":
        MRIP_1_2_Data.append(data.loc[i,:])
    elif data.loc[i,"MRIP"]=="MRIP1_3":
        MRIP_1_3_Data.append(data.loc[i,:])
    elif data.loc[i,"MRIP"]=="MRIP2":
        MRIP_2_Data.append(data.loc[i,:])
    elif data.loc[i,"MRIP"]=="MRIP3":
        MRIP_3_Data.append(data.loc[i,:])
    elif data.loc[i,"MRIP"]=="MRIP4":
        MRIP_4_Data.append(data.loc[i,:])

print("Evaluating")

#MRIP 1.1 -> TD_F<=TD_S /  TO_F>=TO_S
print('  MRIP1.1')
for i in range(0,len(MRIP_1_1_Data)):
    if MRIP_1_1_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_1_1_Data[i].loc['Time to destination (FollowUp)']:
        td="PASS"
    else:
        td="FAIL"
    if MRIP_1_1_Data[i].loc['Balancing (FollowUp)']>=MRIP_1_1_Data[i].loc['Balancing (Source)']-(MRIP_1_1_Data[i].loc['Time to destination (Source)']/100):
        to="PASS"
    else:
        to="FAIL"
    result_1_1=result_1_1.append({'Model': MRIP_1_1_Data[i].loc['Model'],'MRIP':MRIP_1_1_Data[i].loc['MRIP'],'TestCase':MRIP_1_1_Data[i].loc['Test Case'],'TD Verdict': td,'TO Verdict': to},ignore_index=True)
    
    sobran=i%100
    if i>99:
        if MRIP_1_1_Data[i].loc['Time to destination (Source)']-MRIP_1_1_Data[sobran].loc['Time to destination (Source)']<0:
            td_fdr="FAIL"
        else:
            td_fdr="PASS"
        if MRIP_1_1_Data[i].loc['Balancing (Source)']-MRIP_1_1_Data[sobran].loc['Balancing (Source)']<0:
            to_fdr="FAIL"
        else:
            to_fdr="PASS"
        result_1_1_FDR=result_1_1_FDR.append({'Model': MRIP_1_1_Data[i].loc['Model'],'MRIP':MRIP_1_1_Data[i].loc['MRIP'],'TestCase':MRIP_1_1_Data[i].loc['Test Case'],'TD Verdict': td_fdr,'TO Verdict': to_fdr},ignore_index=True)

#MRIP 1.2-> TD_F<=TD_S / TO_F>=TO_S
print('  MRIP1.2')
for i in range(0,len(MRIP_1_2_Data)):
    if MRIP_1_2_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_1_2_Data[i].loc['Time to destination (FollowUp)']:
        td="PASS"
    else:
        td="FAIL"
    if MRIP_1_2_Data[i].loc['Balancing (FollowUp)']>=MRIP_1_1_Data[i].loc['Balancing (Source)']-(MRIP_1_1_Data[i].loc['Time to destination (Source)']/100):
        to="PASS"
    else:
        to="FAIL"
    result_1_2=result_1_2.append({'Model': MRIP_1_2_Data[i].loc['Model'],'MRIP':MRIP_1_2_Data[i].loc['MRIP'],'TestCase':MRIP_1_2_Data[i].loc['Test Case'],'TD Verdict': td,'TO Verdict': to},ignore_index=True)
    
    
    sobran=i%100
    if i>99:
        if MRIP_1_2_Data[i].loc['Time to destination (Source)']-MRIP_1_2_Data[sobran].loc['Time to destination (Source)']<0:
            td_fdr="FAIL"
        else:
            td_fdr="PASS"
        if MRIP_1_2_Data[i].loc['Balancing (Source)']-MRIP_1_2_Data[sobran].loc['Balancing (Source)']<0:
            to_fdr="FAIL"
        else:
            to_fdr="PASS"
        result_1_2_FDR=result_1_2_FDR.append({'Model': MRIP_1_2_Data[i].loc['Model'],'MRIP':MRIP_1_2_Data[i].loc['MRIP'],'TestCase':MRIP_1_2_Data[i].loc['Test Case'],'TD Verdict': td_fdr,'TO Verdict': to_fdr},ignore_index=True)

    
#MRIP 1.3-> TD_F<=TD_S / TO_F>=TO_S
print('  MRIP1.3')
for i in range(0,len(MRIP_1_3_Data)):
    if MRIP_1_3_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_1_3_Data[i].loc['Time to destination (FollowUp)']:
        td="PASS"
    else:
        td="FAIL"
    if MRIP_1_3_Data[i].loc['Balancing (FollowUp)']>=MRIP_1_1_Data[i].loc['Balancing (Source)']-(MRIP_1_1_Data[i].loc['Time to destination (Source)']/100):
        to="PASS"
    else:
        to="FAIL"
    result_1_3=result_1_3.append({'Model': MRIP_1_3_Data[i].loc['Model'],'MRIP':MRIP_1_3_Data[i].loc['MRIP'],'TestCase':MRIP_1_3_Data[i].loc['Test Case'],'TD Verdict': td,'TO Verdict': to},ignore_index=True)
    
        
    sobran=i%100
    if i>99:
        if MRIP_1_3_Data[i].loc['Time to destination (Source)']-MRIP_1_3_Data[sobran].loc['Time to destination (Source)']<0:
            td_fdr="FAIL"
        else:
            td_fdr="PASS"
        if MRIP_1_3_Data[i].loc['Balancing (Source)']-MRIP_1_3_Data[sobran].loc['Balancing (Source)']<0:
            to_fdr="FAIL"
        else:
            to_fdr="PASS"
        result_1_3_FDR=result_1_3_FDR.append({'Model': MRIP_1_3_Data[i].loc['Model'],'MRIP':MRIP_1_3_Data[i].loc['MRIP'],'TestCase':MRIP_1_3_Data[i].loc['Test Case'],'TD Verdict': td_fdr,'TO Verdict': to_fdr},ignore_index=True)

   
#MRIP 3 TD_F==TD_S / TO_F==TO_S
print('  MRIP3')
for i in range(0,len(MRIP_3_Data)):
    if MRIP_3_Data[i].loc['Time to destination (Source)']*1.05>=MRIP_3_Data[i].loc['Time to destination (FollowUp)'] and MRIP_3_Data[i].loc['Time to destination (Source)']*0.95<=MRIP_3_Data[i].loc['Time to destination (FollowUp)']:
        td="PASS"
    else:
        td="FAIL"
    if MRIP_3_Data[i].loc['Balancing (FollowUp)']<=MRIP_3_Data[i].loc['Balancing (Source)']+(MRIP_3_Data[i].loc['Time to destination (Source)']/50) and MRIP_3_Data[i].loc['Balancing (FollowUp)']>=MRIP_3_Data[i].loc['Balancing (Source)']-(MRIP_3_Data[i].loc['Time to destination (Source)']/50):
        to="PASS"
    else:
        to="FAIL"
    result_3=result_3.append({'Model': MRIP_3_Data[i].loc['Model'],'MRIP':MRIP_3_Data[i].loc['MRIP'],'TestCase':MRIP_3_Data[i].loc['Test Case'],'TD Verdict': td,'TO Verdict': to},ignore_index=True)
    
      
    sobran=i%100
    if i>99:
        if MRIP_3_Data[i].loc['Time to destination (Source)']-MRIP_3_Data[sobran].loc['Time to destination (Source)']<0:
            td_fdr="FAIL"
        else:
            td_fdr="PASS"
        if MRIP_3_Data[i].loc['Balancing (Source)']-MRIP_3_Data[sobran].loc['Balancing (Source)']<0:
            to_fdr="FAIL"
        else:
            to_fdr="PASS"
        result_3_FDR=result_3_FDR.append({'Model': MRIP_3_Data[i].loc['Model'],'MRIP':MRIP_3_Data[i].loc['MRIP'],'TestCase':MRIP_3_Data[i].loc['Test Case'],'TD Verdict': td_fdr,'TO Verdict': to_fdr},ignore_index=True)

   
#MRIP 4 TD_F==TD_S / TO_F==TO_S
print('  MRIP4')
for i in range(0,len(MRIP_4_Data)):
    if MRIP_4_Data[i].loc['Time to destination (Source)']*1.05>=MRIP_4_Data[i].loc['Time to destination (FollowUp)'] and MRIP_4_Data[i].loc['Time to destination (Source)']*0.95<=MRIP_4_Data[i].loc['Time to destination (FollowUp)']:
        td="PASS"
    else:
        td="FAIL"
    if MRIP_4_Data[i].loc['Balancing (FollowUp)']<=MRIP_4_Data[i].loc['Balancing (Source)']+(MRIP_4_Data[i].loc['Time to destination (Source)']/80) and MRIP_4_Data[i].loc['Balancing (FollowUp)']>=MRIP_4_Data[i].loc['Balancing (Source)']-(MRIP_4_Data[i].loc['Time to destination (Source)']/80):
        to="PASS"
    else:
        to="FAIL"
    result_4=result_4.append({'Model': MRIP_4_Data[i].loc['Model'],'MRIP':MRIP_4_Data[i].loc['MRIP'],'TestCase':MRIP_4_Data[i].loc['Test Case'],'TD Verdict': td,'TO Verdict': to},ignore_index=True)
    
       
    sobran=i%100
    if i>99:
        if MRIP_4_Data[i].loc['Time to destination (Source)']-MRIP_4_Data[sobran].loc['Time to destination (Source)']<0:
            td_fdr="FAIL"
        else:
            td_fdr="PASS"
        if MRIP_4_Data[i].loc['Balancing (Source)']-MRIP_4_Data[sobran].loc['Balancing (Source)']<0:
            to_fdr="FAIL"
        else:
            to_fdr="PASS"
        result_4_FDR=result_4_FDR.append({'Model': MRIP_4_Data[i].loc['Model'],'MRIP':MRIP_4_Data[i].loc['MRIP'],'TestCase':MRIP_4_Data[i].loc['Test Case'],'TD Verdict': td_fdr,'TO Verdict': to_fdr},ignore_index=True)

   
#MRIP 2 TD_F>=TD_S / TO_F==TO_S
print('  MRIP2')
for i in range(0,len(MRIP_2_Data)):
    if MRIP_2_Data[i].loc['Time to destination (FollowUp)']>=MRIP_2_Data[i].loc['Time to destination (Source)']*0.90:
       td="PASS"
    else:
        td="FAIL"
    if MRIP_2_Data[i].loc['Balancing (FollowUp)']>=MRIP_2_Data[i].loc['Balancing (Source)']-(MRIP_2_Data[i].loc['Time to destination (Source)']/100) and MRIP_2_Data[i].loc['Balancing (FollowUp)']<=MRIP_2_Data[i].loc['Balancing (Source)']+(MRIP_2_Data[i].loc['Time to destination (Source)']/100) :
        to="PASS"
    else:
        to="FAIL"
    result_2=result_2.append({'Model': MRIP_2_Data[i].loc['Model'],'MRIP':MRIP_2_Data[i].loc['MRIP'],'TestCase':MRIP_2_Data[i].loc['Test Case'],'TD Verdict': td,'TO Verdict': to},ignore_index=True)
    
        
    sobran=i%100
    if i>99:
        if MRIP_2_Data[i].loc['Time to destination (Source)']-MRIP_2_Data[sobran].loc['Time to destination (Source)']<0:
            td_fdr="FAIL"
        else:
           td_fdr="PASS"
        if MRIP_2_Data[i].loc['Balancing (Source)']-MRIP_2_Data[sobran].loc['Balancing (Source)']<0:
            to_fdr="FAIL"
        else:
            to_fdr="PASS"
        result_2_FDR=result_2_FDR.append({'Model': MRIP_2_Data[i].loc['Model'],'MRIP':MRIP_2_Data[i].loc['MRIP'],'TestCase':MRIP_2_Data[i].loc['Test Case'],'TD Verdict': td_fdr,'TO Verdict': to_fdr},ignore_index=True)

print('Compiling results')


def changeVerdict(result, testCase, VerdictType):
    
    
    result.loc[result['TestCase']==testCase , VerdictType]="PASS"
    
    return result
        

#Poner todos los falsos FAIL a PASS
failures=pd.DataFrame({});
for i in range(0,100):
    
    if result_1_1['TD Verdict'][i]=="FAIL":
        result_1_1=changeVerdict(result_1_1,result_1_1['TestCase'][i], "TD Verdict")
        result_1_1['TD Verdict'][i]="FAIL"
    if result_1_1['TO Verdict'][i]=="FAIL":
        result_1_1=changeVerdict(result_1_1,result_1_1['TestCase'][i], "TO Verdict")
        result_1_1['TO Verdict'][i]="FAIL"
    if result_1_2['TD Verdict'][i]=="FAIL":
        result_1_2=changeVerdict(result_1_2,result_1_2['TestCase'][i], "TD Verdict")
        result_1_2['TD Verdict'][i]="FAIL"
    if result_1_2['TO Verdict'][i]=="FAIL":
        result_1_2=changeVerdict(result_1_2,result_1_2['TestCase'][i], "TO Verdict")
        result_1_2['TO Verdict'][i]="FAIL"
    if result_1_3['TD Verdict'][i]=="FAIL":
        result_1_3=changeVerdict(result_1_3,result_1_3['TestCase'][i], "TD Verdict")
        result_1_3['TD Verdict'][i]="FAIL"
    if result_1_3['TO Verdict'][i]=="FAIL":
        result_1_3=changeVerdict(result_1_3,result_1_3['TestCase'][i], "TO Verdict")
        result_1_3['TO Verdict'][i]="FAIL"
    if result_2['TD Verdict'][i]=="FAIL":
        result_2=changeVerdict(result_2,result_2['TestCase'][i], "TD Verdict")
        result_2['TD Verdict'][i]="FAIL"
    if result_2['TO Verdict'][i]=="FAIL":
        result_2=changeVerdict(result_2,result_2['TestCase'][i], "TO Verdict")
        result_2['TO Verdict'][i]="FAIL"
    
    if result_3['TD Verdict'][i]=="FAIL":
        result_3=changeVerdict(result_3,result_3['TestCase'][i], "TD Verdict")
        result_3['TD Verdict'][i]="FAIL"
    if result_3['TO Verdict'][i]=="FAIL":
        result_3=changeVerdict(result_3,result_3['TestCase'][i], "TO Verdict")
        result_3['TO Verdict'][i]="FAIL"
    
    if result_4['TD Verdict'][i]=="FAIL":
        result_4=changeVerdict(result_4,result_4['TestCase'][i], "TD Verdict")
        result_4['TD Verdict'][i]="FAIL"
    if result_4['TO Verdict'][i]=="FAIL":
        result_4=changeVerdict(result_4,result_4['TestCase'][i], "TO Verdict")
        result_4['TO Verdict'][i]="FAIL"
    
    
a=0   
def getMutantDetectionRate(result, verdict):
    mutantDetectionTo=[]
    mutantDetectionTd=[]
    j=0
    detectedTo=0
    detectedTd=0
    for i in range(0, len(result)):
        if math.floor(i/nTest) > j:
            j=j+1
            mutantDetectionTo.append(detectedTo)
            mutantDetectionTd.append(detectedTd)
            detectedTo=0
            detectedTd=0
        if result['TO Verdict'][i]== verdict:
            detectedTo=detectedTo+1
        if result['TD Verdict'][i]== verdict:
            detectedTd=detectedTd+1
    mutantDetectionTo.append(detectedTo)
    mutantDetectionTd.append(detectedTd)
    return mutantDetectionTo, mutantDetectionTd
#Sacar metricas de cada uno.
resutl_1_1_FailuresTo, resutl_1_1_FailuresTd =getMutantDetectionRate(result_1_1,"FAIL")
resutl_1_2_FailuresTo, resutl_1_2_FailuresTd =getMutantDetectionRate(result_1_2,"FAIL")
resutl_1_3_FailuresTo, resutl_1_3_FailuresTd =getMutantDetectionRate(result_1_3,"FAIL")
resutl_2_FailuresTo, resutl_2_FailuresTd =getMutantDetectionRate(result_2,"FAIL")
resutl_3_FailuresTo, resutl_3_FailuresTd =getMutantDetectionRate(result_3,"FAIL")
resutl_4_FailuresTo, resutl_4_FailuresTd =getMutantDetectionRate(result_4,"FAIL")

#FDR=Sumar todos los que tengan PASS-> Estos son los que pueden fallar
resutl_1_1_PosFailuresTo, resutl_1_1_PosFailuresTd =getMutantDetectionRate(result_1_1_FDR,"PASS")
resutl_1_2_PosFailuresTo, resutl_1_2_PosFailuresTd =getMutantDetectionRate(result_1_2_FDR,"PASS")
resutl_1_3_PosFailuresTo, resutl_1_3_PosFailuresTd =getMutantDetectionRate(result_1_3_FDR,"PASS")
resutl_2_PosFailuresTo, resutl_2_PosFailuresTd =getMutantDetectionRate(result_2_FDR,"PASS")
resutl_3_PosFailuresTo, resutl_3_PosFailuresTd =getMutantDetectionRate(result_3_FDR,"PASS")
resutl_4_PosFailuresTo, resutl_4_PosFailuresTd =getMutantDetectionRate(result_4_FDR,"PASS")

resutl_1_1_FailuresTo.insert(0,"MRIP1_1")
resutl_1_1_FailuresTd.insert(0,"MRIP1_1")
resutl_1_1_PosFailuresTo.insert(0,"MRIP1_1")
resutl_1_1_PosFailuresTd.insert(0,"MRIP1_1")

resutl_1_2_FailuresTo.insert(0,"MRIP1_2")
resutl_1_2_FailuresTd.insert(0,"MRIP1_2")
resutl_1_2_PosFailuresTo.insert(0,"MRIP1_2")
resutl_1_2_PosFailuresTd.insert(0,"MRIP1_2")

resutl_1_3_FailuresTo.insert(0,"MRIP1_3")
resutl_1_3_FailuresTd.insert(0,"MRIP1_3")
resutl_1_3_PosFailuresTo.insert(0,"MRIP1_3")
resutl_1_3_PosFailuresTd.insert(0,"MRIP1_3")

resutl_2_FailuresTo.insert(0,"MRIP2")
resutl_2_FailuresTd.insert(0,"MRIP2")
resutl_2_PosFailuresTo.insert(0,"MRIP2")
resutl_2_PosFailuresTd.insert(0,"MRIP2")

resutl_3_FailuresTo.insert(0,"MRIP3")
resutl_3_FailuresTd.insert(0,"MRIP3")
resutl_3_PosFailuresTo.insert(0,"MRIP3")
resutl_3_PosFailuresTd.insert(0,"MRIP3")

resutl_4_FailuresTo.insert(0,"MRIP4")
resutl_4_FailuresTd.insert(0,"MRIP4")
resutl_4_PosFailuresTo.insert(0,"MRIP4")
resutl_4_PosFailuresTd.insert(0,"MRIP4")

names=["", "Original", "Mutant1", "Mutant2", "Mutant3", "Mutant4", "Mutant5", "Mutant6", "Mutant7"
       , "Mutant8", "Mutant9", "Mutant10", "Mutant11", "Mutant12", "Mutant13", "Mutant14", "Mutant15"
       , "Mutant16", "Mutant17", "Mutant18", "Mutant19", "Mutant20"]
names1=["", "Mutant1", "Mutant2", "Mutant3", "Mutant4", "Mutant5", "Mutant6", "Mutant7"
       , "Mutant8", "Mutant9", "Mutant10", "Mutant11", "Mutant12", "Mutant13", "Mutant14", "Mutant15"
       , "Mutant16", "Mutant17", "Mutant18", "Mutant19", "Mutant20"]
To= []
To.append(names)
To.append(resutl_1_1_FailuresTo)
To.append(resutl_1_2_FailuresTo)
To.append(resutl_1_3_FailuresTo)
To.append(resutl_2_FailuresTo)
To.append(resutl_3_FailuresTo)
To.append(resutl_4_FailuresTo)

Td= []
Td.append(names)
Td.append(resutl_1_1_FailuresTd)
Td.append(resutl_1_2_FailuresTd)
Td.append(resutl_1_3_FailuresTd)
Td.append(resutl_2_FailuresTd)
Td.append(resutl_3_FailuresTd)
Td.append(resutl_4_FailuresTd)

PossibleTo= []
PossibleTo.append(names1)
PossibleTo.append(resutl_1_1_PosFailuresTo)
PossibleTo.append(resutl_1_2_PosFailuresTo)
PossibleTo.append(resutl_1_3_PosFailuresTo)
PossibleTo.append(resutl_2_PosFailuresTo)
PossibleTo.append(resutl_3_PosFailuresTo)
PossibleTo.append(resutl_4_PosFailuresTo)

PossibleTd= []
PossibleTd.append(names1)
PossibleTd.append(resutl_1_1_PosFailuresTd)
PossibleTd.append(resutl_1_2_PosFailuresTd)
PossibleTd.append(resutl_1_3_PosFailuresTd)
PossibleTd.append(resutl_2_PosFailuresTd)
PossibleTd.append(resutl_3_PosFailuresTd)
PossibleTd.append(resutl_4_PosFailuresTd)

if FORMAT_OUT == 'xlsx':
    pd.DataFrame(To).T.to_excel(FILE_OUT, sheet_name="FAILURES_TO", index=False, header=False)
    with pd.ExcelWriter(FILE_OUT,engine="openpyxl" ,mode='a') as writer: 
        pd.DataFrame(Td).T.to_excel(writer, sheet_name="FAILURES_TD", index=False, header=False)
        pd.DataFrame(PossibleTo).T.to_excel(writer, sheet_name="POSSIBLE_FAILURES_TO", index=False, header=False)
        pd.DataFrame(PossibleTd).T.to_excel(writer, sheet_name="POSSIBLE_FAILURES_TD", index=False, header=False)
else:
    pd.DataFrame(To).T.to_csv(FILE_OUT.format(sheet_name='FAILURES_TO'), index=False, header=False)
    pd.DataFrame(Td).T.to_csv(FILE_OUT.format(sheet_name='FAILURES_TD'), index=False, header=False)
    pd.DataFrame(PossibleTo).T.to_csv(FILE_OUT.format(sheet_name='POSSIBLE_FAILURES_TO'), index=False, header=False)
    pd.DataFrame(PossibleTd).T.to_csv(FILE_OUT.format(sheet_name='POSSIBLE_FAILURES_TD'), index=False, header=False)
