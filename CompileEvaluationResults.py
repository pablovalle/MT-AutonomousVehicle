# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:26:46 2022

@author: pablo
"""

import pandas as pd
import math

FILE_IN  = "Results\Experiment_Results.xlsx"
FILE_OUT ='Results\EvaluationFinal_{sheet_name}.xlsx'
#FILE_OUT ='Evaluation.xlsx'

FORMAT_IN = 'csv'
if FILE_IN.endswith('.xlsx'):
    FORMAT_IN = 'xlsx'
FORMAT_OUT = 'csv'
if FILE_OUT.endswith('.xlsx'):
    FORMAT_OUT = 'xlsx'

if FORMAT_IN == 'xlsx':
    data = pd.read_excel(FILE_IN, engine='openpyxl')
else:
    data = pd.read_csv(FILE_IN)

data = data.drop(['# of Waypoints','Error distance (Source)', 'Error distance (FollowUp)',
                 'Distance to the car Follow up', 'Distance to the car Source','Source exec time',
                 'Follow up exec time'  ],axis=1)

data['Balancing (Source)'].loc[(data['Balancing (Source)']<0.1)]=0.1
data['Balancing (FollowUp)'].loc[(data['Balancing (FollowUp)']<0.1)]=0.1
toDiscard_MRIP3=list()
toDiscard_MRIP4=list()
def calcDetection_Mrip1(data, mrip_to, mrip_td, threshold_td, threshold_to):
    
    if data['Time to destination (Source)']*threshold_td<=data['Time to destination (FollowUp)']:
        mrip_td=mrip_td+1
    if data['Balancing (Source)']>=data['Balancing (FollowUp)']*threshold_to:
        mrip_to=mrip_to+1
    
    return mrip_to, mrip_td

def calcDetection_Mrip2(data, mrip_to, mrip_td, threshold_td, threshold_to):
    if data['Time to destination (Source)']>=data['Time to destination (FollowUp)']*threshold_td:
        mrip_td=mrip_td+1

    if abs(data['Balancing (Source)']-data['Balancing (FollowUp)'])/data['Balancing (Source)']>=threshold_to:
        mrip_to=mrip_to+1
    
    return mrip_to, mrip_td

def calcDetection_Mrip3(data, mrip_to, mrip_td, threshold_td, threshold_to):
    if abs(data['Time to destination (Source)']-data['Time to destination (FollowUp)'])/data['Time to destination (Source)']>=threshold_td:
        mrip_td=mrip_td+1
    timeDiff=abs(data['Time to destination (FollowUp)'] - data['Time to destination (Source)'])/10
    if (abs(data['Balancing (Source)']-data['Balancing (FollowUp)'])-timeDiff)/max([data['Balancing (Source)'],data['Balancing (FollowUp)']])>=threshold_to and data['Test Case'] not in toDiscard_MRIP3 and data['Time to destination (Source)']!=99999:
        mrip_to=mrip_to+1
        if data['Model']==caseStudies[0]:
            toDiscard_MRIP3.append(data['Test Case'])
        
    
    return mrip_to, mrip_td

def calcDetection_Mrip4(data, mrip_to, mrip_td, threshold_td, threshold_to):
    if abs(data['Time to destination (Source)']-data['Time to destination (FollowUp)'])/data['Time to destination (Source)']>=threshold_td:
        mrip_td=mrip_td+1
    if (abs(data['Balancing (Source)']-data['Balancing (FollowUp)'])-0.2)/max([data['Balancing (Source)'],data['Balancing (FollowUp)']])>=threshold_to and data['Test Case'] not in toDiscard_MRIP4:
        mrip_to=mrip_to+1
        if data['Model']==caseStudies[0]:
            toDiscard_MRIP4.append(data['Test Case'])
    
    return mrip_to, mrip_td
def compareWithOriginal(data1, data2, mrip_to, mrip_td):

    if data1['Time to destination (Source)']<data2['Time to destination (Source)']:
        mrip_td=mrip_td+1
    if data1['Balancing (Source)']<data2['Balancing (Source)']:
        mrip_to=mrip_to+1
    
    return mrip_to, mrip_td

print("Data loaded")
nTest=100
nMrip=6
nStudies=21
caseStudies=list(dict.fromkeys(data['Model']))
#Test Cases to Discard.
toDiscard=set()
for i in range(0,nTest):
    for j in range(0,nMrip):
        if data['Time to destination (Source)'][j*nTest+i]==99999:
            toDiscard.add(data['Test Case'][j*nTest+i])
            
results_To=pd.DataFrame({"Mutant":[], "MRIP1_1":[], "MRIP1_2":[], "MRIP1_3":[], "MRIP2":[], "MRIP3":[], "MRIP4":[]})
results_Td=pd.DataFrame({"Mutant":[], "MRIP1_1":[], "MRIP1_2":[], "MRIP1_3":[], "MRIP2":[], "MRIP3":[], "MRIP4":[]})
results_ToPos=pd.DataFrame({"Mutant":[], "MRIP1_1":[], "MRIP1_2":[], "MRIP1_3":[], "MRIP2":[], "MRIP3":[], "MRIP4":[]})
results_TdPos=pd.DataFrame({"Mutant":[], "MRIP1_1":[], "MRIP1_2":[], "MRIP1_3":[], "MRIP2":[], "MRIP3":[], "MRIP4":[]})
  
            
for i in range(0,nStudies):
    mrip1_1_to=0
    mrip1_2_to=0
    mrip1_3_to=0
    mrip2_to=0
    mrip3_to=0
    mrip4_to=0
    
    mrip1_1_td=0
    mrip1_2_td=0
    mrip1_3_td=0
    mrip2_td=0
    mrip3_td=0
    mrip4_td=0
    
    mrip1_1_toPos=0
    mrip1_2_toPos=0
    mrip1_3_toPos=0
    mrip2_toPos=0
    mrip3_toPos=0
    mrip4_toPos=0
    
    mrip1_1_tdPos=0
    mrip1_2_tdPos=0
    mrip1_3_tdPos=0
    mrip2_tdPos=0
    mrip3_tdPos=0
    mrip4_tdPos=0
    print("Running on mutant: "+caseStudies[i])
    for j in range(0,nMrip):
        for k in range(0, nTest):
            if data['Test Case'][i] in toDiscard:
                continue
            indice=i*nMrip*nTest+j*nTest+k
            indice2=j*nTest+k
            if data['MRIP'][indice]=="MRIP1_1":
                mrip1_1_to, mrip1_1_td=calcDetection_Mrip1(data.iloc[indice],mrip1_1_to,mrip1_1_td,1.1,1.3)
                if i>0:
                   mrip1_1_toPos, mrip1_1_tdPos=compareWithOriginal(data.iloc[indice],data.iloc[indice2],mrip1_1_toPos,mrip1_1_tdPos)                 
            elif data['MRIP'][indice]=="MRIP1_2":
                mrip1_2_to, mrip1_2_td=calcDetection_Mrip1(data.iloc[indice],mrip1_2_to,mrip1_2_td,1.1,1.3)
                if i>0:
                   mrip1_2_toPos, mrip1_2_tdPos=compareWithOriginal(data.iloc[indice],data.iloc[indice2],mrip1_2_toPos,mrip1_2_tdPos)                 
            
            elif data['MRIP'][indice]=="MRIP1_3":
                mrip1_3_to, mrip1_3_td=calcDetection_Mrip1(data.iloc[indice],mrip1_3_to,mrip1_3_td,1.1,1.3)
                if i>0:
                   mrip1_3_toPos, mrip1_3_tdPos=compareWithOriginal(data.iloc[indice],data.iloc[indice2],mrip1_3_toPos,mrip1_3_tdPos)                 
            
            elif data['MRIP'][indice]=="MRIP2":
                mrip2_to, mrip2_td=calcDetection_Mrip2(data.iloc[indice],mrip2_to,mrip2_td,1.1,0.3)
                if i>0:
                   mrip2_toPos, mrip2_tdPos=compareWithOriginal(data.iloc[indice],data.iloc[indice2],mrip2_toPos,mrip2_tdPos)                 
            
            elif data['MRIP'][indice]=="MRIP3":
                mrip3_to, mrip3_td=calcDetection_Mrip3(data.iloc[indice],mrip3_to,mrip3_td,0.15,0.3)
                if i>0:
                   mrip3_toPos, mrip3_tdPos=compareWithOriginal(data.iloc[indice],data.iloc[indice2],mrip3_toPos,mrip3_tdPos)                 
            
            elif data['MRIP'][indice]=="MRIP4":
                mrip4_to, mrip4_td=calcDetection_Mrip4(data.iloc[indice],mrip4_to,mrip4_td,0.1,0.3)
                if i>0:
                   mrip4_toPos, mrip4_tdPos=compareWithOriginal(data.iloc[indice],data.iloc[indice2],mrip4_toPos,mrip4_tdPos)                 
            
    
    
    results_To=results_To.append({"Mutant":caseStudies[i], "MRIP1_1":mrip1_1_to, "MRIP1_2":mrip1_2_to, "MRIP1_3":mrip1_3_to, "MRIP2":mrip2_to, "MRIP3":mrip3_to, "MRIP4":mrip4_to}, ignore_index=True)
    results_Td=results_Td.append({"Mutant":caseStudies[i], "MRIP1_1":mrip1_1_td, "MRIP1_2":mrip1_2_td, "MRIP1_3":mrip1_3_td, "MRIP2":mrip2_td, "MRIP3":mrip3_td, "MRIP4":mrip4_td}, ignore_index=True)
    results_ToPos=results_ToPos.append({"Mutant":caseStudies[i], "MRIP1_1":mrip1_1_toPos, "MRIP1_2":mrip1_2_toPos, "MRIP1_3":mrip1_3_toPos, "MRIP2":mrip2_toPos, "MRIP3":mrip3_toPos, "MRIP4":mrip4_toPos}, ignore_index=True)
    results_TdPos=results_TdPos.append({"Mutant":caseStudies[i], "MRIP1_1":mrip1_1_tdPos, "MRIP1_2":mrip1_2_tdPos, "MRIP1_3":mrip1_3_tdPos, "MRIP2":mrip2_tdPos, "MRIP3":mrip3_tdPos, "MRIP4":mrip4_tdPos}, ignore_index=True)

results_To.to_excel(FILE_OUT, sheet_name="FAILURES_TO", index=False, header=False)
with pd.ExcelWriter(FILE_OUT,engine="openpyxl" ,mode='a') as writer: 
    results_Td.to_excel(writer, sheet_name="FAILURES_TD", index=False, header=False)
    results_ToPos.to_excel(writer, sheet_name="POSSIBLE_FAILURES_TO", index=False, header=False)
    results_TdPos.to_excel(writer, sheet_name="POSSIBLE_FAILURES_TD", index=False, header=False)      











