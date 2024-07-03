# models.py
from django.db import models

class cancerdb(models.Model):
    m_Patient_Id = models.IntegerField(primary_key=True,verbose_name="Patient Id")
    m_Patient_name=models.CharField(max_length=25,default="Unknown",verbose_name="Patient Name")
    m_Age = models.IntegerField(verbose_name="Age")
    m_Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')],verbose_name="Gender")
    m_BMI = models.FloatField(verbose_name="BMI")
    m_BSA = models.FloatField(verbose_name="BSA")
    m_ECOG = models.CharField(max_length=40,choices=[
        ('Fully active', 'Fully active'),
        ('Restricted in strenous activity', 'Restricted in strenous activity'),
        ('Capable of self-care', 'Capable of self-care'),
        ('Capable of limited self-care', 'Capable of limited self-care'),
        ('Completely disabled', 'Completely disabled'),
        ('Dead', 'Dead'),
    ],verbose_name="ECOG")
    m_Substanceabuse = models.CharField(max_length=40,choices=[('TeeTotaler', 'TeeTotaler'), ('Not a TeeTotaler', 'Not a TeeTotaler')],verbose_name="Substanceabuse")
    m_DiabetesCI = models.CharField(max_length=40,choices=[
        ('No Diabetes', 'No Diabetes'),
        ('Good control but no influence', 'Good control but no influence'),
        ('Controlled but partially influenced', 'Controlled but partially influenced'),
        ('Poor control and severely influenced', 'Poor control and severely influenced'),
    ],verbose_name="Diabetes CI")
    m_HeartDiseaseCI = models.CharField(max_length=40,choices=[
        ('No heart Disease', 'No heart Disease'),
        ('Diagnosed but good pumping', 'Diagnosed but good pumping'),
        ('Bypass but good pumping', 'Bypass but good pumping'),
        ('Bypass but bad pumping', 'Bypass but bad pumping'),
    ],verbose_name="HeartDisease CI")
    m_EjectionFraction = models.FloatField(verbose_name="Ejection Fraction")
    m_Weightloss = models.FloatField(verbose_name="WightLoss(Kg)")
    m_Haemoglobin = models.FloatField(verbose_name="Haemoglobin")
    m_WBC = models.FloatField(verbose_name="WBC")
    m_ANC = models.FloatField(verbose_name="ANC")
    m_PlatletCount = models.FloatField(verbose_name="Platlet Count(L)")
    m_Creatininel = models.FloatField(verbose_name="Creatinine Level")
    m_Creatininec = models.FloatField(verbose_name="Creatinine Clearance")
    m_Bilrubin = models.FloatField(verbose_name="Bilirubin(mg)")
    m_AST = models.FloatField(verbose_name="AST/ALT")
    m_Albumin = models.FloatField(verbose_name="Albumin")
    m_SpO2 = models.FloatField(verbose_name="SpO2")
    m_Heartrate = models.FloatField(verbose_name="Heart Rate")
    m_PriorHospitalization = models.CharField(max_length=20,choices=[('>6 mo back', '>6 mo back'), ('3-6 mo back', '3-6 mo back'),('<3-1 mo', '<3-1 mo'),('<1 mo','<1 mo' )],verbose_name="PriorHospitalization")
    m_BP = models.CharField(max_length=20,verbose_name="BP(systolic/diastolic)")
    m_Walking = models.CharField(max_length=20,choices=[(">100 mt", ">100 mt"), ('50-100 mt', '50-100 mt'),('50-100 mt', '50-100 mt'),('10-50 mt','10-50 mt' ),('<5 mt', '<5 mt')],verbose_name="Limited Walking")
    m_Drug = models.CharField(max_length=100,choices=[('TKI/Antibody', 'TKI/Antibody'), ('Chemotherapy', 'Chemotherapy')],verbose_name="Class of Chemo agents")
    m_Chemoagent = models.IntegerField(choices=[(1,1),(2,2),(3,3)],verbose_name="Number of ChemoAgents")
    m_Dosingagent = models.CharField(max_length=20,choices=[("QW","QW"),("Q3W","Q3W"),("Q3W,Q2W","Q3W,Q2W"),("Q2W,QW","Q2W,QW")],verbose_name="Dosing Agent")
    m_Setting = models.CharField(max_length=100,choices=[("NACT", "NACT"), ("Adjuvant", "Adjuvant"),("Relapsed 1","Relapsed 1"),("Relapsed 2","Relapsed 2")],verbose_name="Setting")
    m_SocialSupport = models.CharField(max_length=20,choices=[("Good", "Good"), ("Poor", "Poor"),("NIL","NIL")],verbose_name="Social Support")
    m_MentalState = models.CharField(max_length=20,choices=[('Normal ,stable', 'Normal ,stable'), ("Depressed ,stable", "Depressed ,stable"), ("Emotional/unstable", "Emotional/unstable"),("Psychiatric illness", "Psychiatric illness")],verbose_name="Mental State")
    m_DistanceFH = models.CharField(max_length=20,choices=[('Local', 'Local'), ('<50 km', '<50 km'),('50-100 km','50-100 km'),('>100 km','>100 km')],verbose_name="Distance From Home(km)")
    m_CancerType = models.CharField(max_length=100,choices=[("Carcinoma", "Carcinoma") , ("Carcinosarcoma", "Carcinosarcoma"),("Sarcoma", "Sarcoma")],verbose_name="CancerType")
    m_Gradeg = models.CharField(max_length=100,choices=[("Low Grade", "Low Grade"), ("High Grade", "High Grade")],verbose_name="Grade")
    m_StageBurden = models.CharField(max_length=100,choices=[("None", "None"), ("Low Tumour Burden", "Low Tumour Burden"), ("High Tumour Burden", "High Tumour Burden")],verbose_name="StageBurden")
    m_ChemoTolerance = models.CharField(max_length=100,choices=[("Good", "Good"), ("Fatigue,neutropenia(G1,2),no fever", "Fatigue,neutropenia(G1,2),no fever"), ("Febrile Neutropenia G3/4", "Febrile Neutropenia G3/4")],verbose_name="Febrile Neutropenia G3/4")
    m_DuringChemo = models.CharField(max_length=100,choices=[("No change", "No change"), ("Down,but improved", "Down,but improved"),("PS 3,still not recovered","PS 3,still not recovered")],verbose_name="PS during chemo")
    m_Cycle = models.IntegerField(verbose_name="Cycle")
    m_Therapy_Suggested=models.CharField(max_length=100)
    