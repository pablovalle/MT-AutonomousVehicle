import pandas as pd
import xlsxwriter

variable_range_time=1
variable_range_balancing=0.15
data= pd.read_excel("Experiment_Results.xlsx")
data= data.drop(['# of Waypoints','Error distance (Source)', 'Error distance (FollowUp)',
                 'Distance to the car Follow up', 'Distance to the car Source','Source exec time',
                 'Follow up exec time'  ],axis=1)

i=0
time=[]
balancing=[]
verdict="PASS"

MRIP_1_1_Data=[]
MRIP_1_2_Data=[]
MRIP_1_3_Data=[]
MRIP_2_Data=[]
MRIP_3_Data=[]
MRIP_4_Data=[]
RESULT_1_1=[]
RESULT_1_2=[]
RESULT_1_3=[]
RESULT_2=[]
RESULT_3=[]
RESULT_4=[]
RESULT_1_1_FDR=[]
RESULT_1_2_FDR=[]
RESULT_1_3_FDR=[]
RESULT_2_FDR=[]
RESULT_3_FDR=[]
RESULT_4_FDR=[]


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
    elif data.loc[i,"MRIP"]=="MRIP1_4":
        MRIP_4_Data.append(data.loc[i,:])


class Result:
    def __init__(self,Model,MRIP,TestCase, TD, TO):
        self.TD = TD
        self.TO = TO
        self.Model=Model
        self.MRIP=MRIP
        self.TestCase=TestCase
    
    def setTD(self,TD):
        self.TD=TD
    def setTO(self,TO):
        self.TO=TO
    def see(self):
        print("--------------------------------------------------")
        print("Model: "+self.Model)
        print("MRIP: "+self.MRIP)
        print("TestCase: "+str(self.TestCase))
        print("TD Verdict: "+self.TD)
        print("TO Verdict: "+self.TO)

#MRIP 1.1 -> TD_F<=TD_S /  TO_F>=TO_S
for i in range(0,len(MRIP_1_1_Data)):
    result=Result(MRIP_1_1_Data[i].loc['Model'],MRIP_1_1_Data[i].loc['MRIP'],MRIP_1_1_Data[i].loc['Test Case'],"","")
    '''
    if MRIP_1_1_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_1_1_Data[i].loc['Time to destination (FollowUp)']:
        result.setTD("PASS")
    else:
        result.setTD("FAIL")
    if MRIP_1_1_Data[i].loc['Balancing (FollowUp)']>=MRIP_1_1_Data[i].loc['Balancing (Source)']-(MRIP_1_1_Data[i].loc['Time to destination (Source)']/100):
        result.setTO("PASS")
    else:
        result.setTO("FAIL")
    RESULT_1_1.append(result)
    '''
    sobran=i%100
    if i>100:
        if MRIP_1_1_Data[i].loc['Time to destination (Source)']-MRIP_1_1_Data[sobran].loc['Time to destination (Source)']<0:
            result.setTD("FAIL")
        else:
            result.setTD("PASS")
        if abs(MRIP_1_1_Data[i].loc['Balancing (Source)']-MRIP_1_1_Data[sobran].loc['Balancing (Source)'])<0:
            result.setTO("FAIL")
        else:
            result.setTO("PASS")
        RESULT_1_1_FDR.append(result)
    
#MRIP 1.2-> TD_F<=TD_S / TO_F>=TO_S
for i in range(0,len(MRIP_1_2_Data)):
    result=Result(MRIP_1_2_Data[i].loc['Model'],MRIP_1_2_Data[i].loc['MRIP'],MRIP_1_2_Data[i].loc['Test Case'],"","")
    '''
    if MRIP_1_2_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_1_2_Data[i].loc['Time to destination (FollowUp)']:
        result.setTD("PASS")
    else:
        result.setTD("FAIL")
    if MRIP_1_2_Data[i].loc['Balancing (FollowUp)']>=MRIP_1_1_Data[i].loc['Balancing (Source)']-(MRIP_1_1_Data[i].loc['Time to destination (Source)']/100):
        result.setTO("PASS")
    else:
        result.setTO("FAIL")
    RESULT_1_2.append(result)
    ''' 
    sobran=i%100
    if i>100:
        if MRIP_1_2_Data[i].loc['Time to destination (Source)']-MRIP_1_2_Data[sobran].loc['Time to destination (Source)']<0:
            result.setTD("FAIL")
        else:
            result.setTD("PASS")
        if MRIP_1_2_Data[i].loc['Balancing (Source)']-MRIP_1_2_Data[sobran].loc['Balancing (Source)']<0:
            result.setTO("FAIL")
        else:
            result.setTO("PASS")
        RESULT_1_2_FDR.append(result)
    
#MRIP 1.3-> TD_F<=TD_S / TO_F>=TO_S
for i in range(0,len(MRIP_1_3_Data)):
    result=Result(MRIP_1_3_Data[i].loc['Model'],MRIP_1_3_Data[i].loc['MRIP'],MRIP_1_3_Data[i].loc['Test Case'],"","")
    '''
    if MRIP_1_3_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_1_3_Data[i].loc['Time to destination (FollowUp)']:
        result.setTD("PASS")
    else:
        result.setTD("FAIL")
    if MRIP_1_3_Data[i].loc['Balancing (FollowUp)']>=MRIP_1_1_Data[i].loc['Balancing (Source)']-(MRIP_1_1_Data[i].loc['Time to destination (Source)']/100):
        result.setTO("PASS")
    else:
        result.setTO("FAIL")
    RESULT_1_3.append(result)
    '''    
    sobran=i%100
    if i>100:
        if MRIP_1_3_Data[i].loc['Time to destination (Source)']-MRIP_1_3_Data[sobran].loc['Time to destination (Source)']<0:
            result.setTD("FAIL")
        else:
            result.setTD("PASS")
        if MRIP_1_3_Data[i].loc['Balancing (Source)']-MRIP_1_3_Data[sobran].loc['Balancing (Source)']<0:
            result.setTO("FAIL")
        else:
            result.setTO("PASS")
        RESULT_1_3_FDR.append(result)
    
#MRIP 3 TD_F==TD_S / TO_F==TO_S
for i in range(0,len(MRIP_3_Data)):
    result=Result(MRIP_3_Data[i].loc['Model'],MRIP_3_Data[i].loc['MRIP'],MRIP_3_Data[i].loc['Test Case'],"","")
    
    if MRIP_3_Data[i].loc['Time to destination (Source)']*1.15>=MRIP_3_Data[i].loc['Time to destination (FollowUp)'] and MRIP_3_Data[i].loc['Time to destination (Source)']*0.85<=MRIP_3_Data[i].loc['Time to destination (FollowUp)']:
        result.setTD("PASS")
    else:
        result.setTD("FAIL")
    if MRIP_3_Data[i].loc['Balancing (FollowUp)']<=MRIP_3_Data[i].loc['Balancing (Source)']+(MRIP_3_Data[i].loc['Time to destination (Source)']/50) and MRIP_3_Data[i].loc['Balancing (FollowUp)']>=MRIP_3_Data[i].loc['Balancing (Source)']-(MRIP_3_Data[i].loc['Time to destination (Source)']/50):
        result.setTO("PASS")
    else:
        result.setTO("FAIL")
    RESULT_3.append(result)
    '''    
    sobran=i%100
    if i>100:
        if MRIP_3_Data[i].loc['Time to destination (Source)']-MRIP_3_Data[sobran].loc['Time to destination (Source)']<0:
            result.setTD("FAIL")
        else:
            result.setTD("PASS")
        if MRIP_3_Data[i].loc['Balancing (Source)']-MRIP_3_Data[sobran].loc['Balancing (Source)']<0:
            result.setTO("FAIL")
        else:
            result.setTO("PASS")
        RESULT_3_FDR.append(result)
    '''
#MRIP 4 TD_F==TD_S / TO_F==TO_S
for i in range(0,len(MRIP_4_Data)):
    result=Result(MRIP_4_Data[i].loc['Model'],MRIP_4_Data[i].loc['MRIP'],MRIP_4_Data[i].loc['Test Case'],"","")
    '''
    if MRIP_4_Data[i].loc['Time to destination (Source)']*1.1>=MRIP_4_Data[i].loc['Time to destination (FollowUp)'] and MRIP_4_Data[i].loc['Time to destination (Source)']*0.90<=MRIP_4_Data[i].loc['Time to destination (FollowUp)']:
        result.setTD("PASS")
    else:
        result.setTD("FAIL")
    if MRIP_4_Data[i].loc['Balancing (FollowUp)']<=MRIP_4_Data[i].loc['Balancing (Source)']+(MRIP_4_Data[i].loc['Time to destination (Source)']/80) and MRIP_4_Data[i].loc['Balancing (FollowUp)']>=MRIP_4_Data[i].loc['Balancing (Source)']-(MRIP_4_Data[i].loc['Time to destination (Source)']/80):
        result.setTO("PASS")
    else:
        result.setTO("FAIL")
    RESULT_4.append(result)
    '''    
    sobran=i%100
    if i>100:
        if MRIP_4_Data[i].loc['Time to destination (Source)']-MRIP_4_Data[sobran].loc['Time to destination (Source)']<0:
            result.setTD("FAIL")
        else:
            result.setTD("PASS")
        if MRIP_4_Data[i].loc['Balancing (Source)']-MRIP_4_Data[sobran].loc['Balancing (Source)']<0:
            result.setTO("FAIL")
        else:
            result.setTO("PASS")
        RESULT_4_FDR.append(result)
    
#MRIP 2 TD_F>=TD_S / TO_F==TO_S

for i in range(0,len(MRIP_2_Data)):
    result=Result(MRIP_2_Data[i].loc['Model'],MRIP_2_Data[i].loc['MRIP'],MRIP_2_Data[i].loc['Test Case'],"","")
    '''
    if MRIP_2_Data[i].loc['Time to destination (FollowUp)']>=MRIP_2_Data[i].loc['Time to destination (Source)']*0.90:
        result.setTD("PASS")
    else:
        result.setTD("FAIL")
    if MRIP_2_Data[i].loc['Balancing (FollowUp)']>=MRIP_2_Data[i].loc['Balancing (Source)']-(MRIP_2_Data[i].loc['Time to destination (Source)']/100) and MRIP_2_Data[i].loc['Balancing (FollowUp)']<=MRIP_2_Data[i].loc['Balancing (Source)']+(MRIP_2_Data[i].loc['Time to destination (Source)']/100) :
        result.setTO("PASS")
    else:
        result.setTO("FAIL")
    RESULT_2.append(result)
    '''    
    sobran=i%100
    if i>100:
        if MRIP_2_Data[i].loc['Time to destination (Source)']-MRIP_2_Data[sobran].loc['Time to destination (Source)']<0:
            result.setTD("FAIL")
        else:
            result.setTD("PASS")
        if MRIP_2_Data[i].loc['Balancing (Source)']-MRIP_2_Data[sobran].loc['Balancing (Source)']<0:
            result.setTO("FAIL")
        else:
            result.setTO("PASS")
        RESULT_2_FDR.append(result)
    
'''
workbook=xlsxwriter.Workbook('Results_MRIP1_1.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_1_1:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP1_2.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_1_2:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP1_3.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_1_3:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP2.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_2:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP4.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_4:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()
'''

workbook=xlsxwriter.Workbook('Results_MRIP3.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_3:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()
'''
workbook=xlsxwriter.Workbook('Results_MRIP1_1_FDR.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_1_1_FDR:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP1_2_FDR.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_1_2_FDR:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP1_3_FDR.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_1_3_FDR:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP2_FDR.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_2_FDR:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP3_FDR.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_3_FDR:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()

workbook=xlsxwriter.Workbook('Results_MRIP4_FDR.xlsx')
worksheet=workbook.add_worksheet()
row=0
col=0
for result in RESULT_4_FDR:
    worksheet.write(row,col,result.Model)
    worksheet.write(row,col+1,result.MRIP)
    worksheet.write(row,col+2,result.TD)
    worksheet.write(row,col+3,result.TO)
    row+=1
workbook.close()
'''
