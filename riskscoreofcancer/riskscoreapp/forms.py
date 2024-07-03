from django import forms
from .models import cancerdb
class insert(forms.Form):
    Patient_Id = forms.IntegerField(label="Patient Id")
    Patient_name=forms.CharField(max_length=25,label="Patient Name")
    Age = forms.IntegerField(label="Age")
    Gender = forms.CharField(max_length=10, widget=forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]),label="Gender")
    BMI = forms.FloatField(label="BMI")
    BSA = forms.FloatField(label="BSA")
    ECOG = forms.CharField(max_length=40,widget=forms.Select(choices=[
        ('Fully active', 'Fully active'),
        ('Restricted in strenous activity', 'Restricted in strenous activity'),
        ('Capable of self-care', 'Capable of self-care'),
        ('Capable of limited self-care', 'Capable of limited self-care'),
        ('Completely disabled', 'Completely disabled'),
        ('Dead', 'Dead'),
    ]),label="ECOG")
    Substanceabuse = forms.CharField(max_length=40,widget=forms.Select(choices=[('TeeTotaler', 'TeeTotaler'), ('Not a TeeTotaler', 'Not a TeeTotaler')]))
    DiabetesCI = forms.CharField(max_length=40,widget=forms.Select(choices=[
        ('No Diabetes', 'No Diabetes'),
        ('Good control but no influence', 'Good control but no influence'),
        ('Controlled but partially influenced', 'Controlled but partially influenced'),
        ('Poor control and severely influenced', 'Poor control and severely influenced'),
    ]),label="Diabetes CI")
    HeartDiseaseCI = forms.CharField(max_length=40,widget=forms.Select(choices=[
        ('No heart Disease', 'No heart Disease'),
        ('Diagnosed but good pumping', 'Diagnosed but good pumping'),
        ('Bypass but good pumping', 'Bypass but good pumping'),
        ('Bypass but bad pumping', 'Bypass but bad pumping'),
    ]),label="HeartDisease CI")
    EjectionFraction = forms.FloatField(label="Ejection Fraction")
    Weightloss = forms.FloatField(label="WightLoss(Kg)")
    Haemoglobin = forms.FloatField(label="Haemoglobin")
    WBC = forms.FloatField(label="WBC")
    ANC = forms.FloatField(label="ANC")
    PlatletCount = forms.FloatField(label="Platlet Count(L)")
    Creatininel = forms.FloatField(label="Creatinine Level")
    Creatininec = forms.FloatField(label="Creatinine Clearance")
    Bilrubin = forms.FloatField(label="Bilirubin(mg)")
    AST = forms.FloatField(label="AST/ALT")
    Albumin = forms.FloatField(label="Albumin")
    SpO2 = forms.FloatField(label="SpO2%")
    Heartrate = forms.FloatField(label="Heart Rate")
    PriorHospitalization = forms.CharField(max_length=20, widget=forms.Select(choices=[('>6 mo back', '>6 mo back'), ('3-6 mo back', '3-6 mo back'),('<3-1 mo', '<3-1 mo'),('<1 mo','<1 mo' )]))
    BP = forms.CharField(max_length=20,label="BP(systolic/diastolic)")
    Walking = forms.CharField(max_length=20, widget=forms.Select(choices=[(">100 mt", ">100 mt"), ('50-100 mt', '50-100 mt'),('50-100 mt', '50-100 mt'),('10-50 mt','10-50 mt' ),('<5 mt', '<5 mt')]),label="Limited Walking")
    Drug = forms.CharField(max_length=100, widget=forms.Select(choices=[('TKI/Antibody', 'TKI/Antibody'), ('Chemotherapy', 'Chemotherapy')]),label="Class of Chemo agents")
    Chemoagent = forms.IntegerField(widget=forms.Select(choices=[(1,1),(2,2),(3,3)]),label="Number of ChemoAgents")
    Dosingagent = forms.CharField(max_length=20, widget=forms.Select(choices=[("QW","QW"),("Q3W","Q3W"),("Q3W,Q2W","Q3W,Q2W"),("Q2W,QW","Q2W,QW")]),label="Dosing Agent")
    Setting = forms.CharField(max_length=100,widget=forms.Select(choices=[("NACT", "NACT"), ("Adjuvant", "Adjuvant"),("Relapsed 1","Relapsed 1"),("Relapsed 2","Relapsed 2")]))
    SocialSupport = forms.CharField(max_length=20, widget=forms.Select(choices=[("Good", "Good"), ("Poor", "Poor"),("NIL","NIL")]),label="Social Support")
    MentalState = forms.CharField(max_length=20, widget=forms.Select(choices=[('Normal ,stable', 'Normal ,stable'), ("Depressed ,stable", "Depressed ,stable"), ("Emotional/unstable", "Emotional/unstable"),("Psychiatric illness", "Psychiatric illness")]),label="Mental State")
    DistanceFH = forms.CharField(max_length=20, widget=forms.Select(choices=[('Local', 'Local'), ('<50 km', '<50 km'),('50-100 km','50-100 km'),('>100 km','>100 km')]),label="Distance From Home(km)")
    CancerType = forms.CharField (max_length=100,widget=forms.Select(choices=[("Carcinoma", "Carcinoma") , ("Carcinosarcoma", "Carcinosarcoma"),("Sarcoma", "Sarcoma")]),label="Cancer Type")
    Gradeg = forms.CharField(max_length=100, widget=forms.Select(choices=[("Low Grade", "Low Grade"), ("High Grade", "High Grade")]),label="Grade")
    StageBurden = forms.CharField(max_length=100,widget=forms.Select(choices=[("None", "None"), ("Low Tumour Burden", "Low Tumour Burden"), ("High Tumour Burden", "High Tumour Burden")]),label="Stage Burden")
    ChemoTolerance = forms.CharField(max_length=100,widget=forms.Select(choices=[("Good", "Good"), ("Fatigue,neutropenia(G1,2),no fever", "Fatigue,neutropenia(G1,2),no fever"), ("Febrile Neutropenia G3/4", "Febrile Neutropenia G3/4")]),label="Chemo Tolerance")
    DuringChemo = forms.CharField(max_length=100,widget=forms.Select(choices=[("No change", "No change"), ("Down,but improved", "Down,but improved"),("PS 3,still not recovered","PS 3,still not recovered")]),label="PS during chemo")
    Cycle = forms.IntegerField(label="Cycle")
class search(forms.Form):
    Patient_Id = forms.IntegerField(label="Patient Id")
class update1(forms.Form):
    Patient_Id = forms.IntegerField(label="Patient Id")
class update(forms.ModelForm):
    
    class Meta:
        model = cancerdb
        # fields = '__all__' 
        exclude = ['m_Therapy_Suggested']

class delete1(forms.Form):
    Patient_Id = forms.IntegerField()
class display(forms.Form):
    Patient_Id = forms.IntegerField(label="Patient Id")
    Patient_name=forms.CharField(max_length=25,label="Patient Name")
    Age = forms.IntegerField(label="Age")
    Gender = forms.CharField(max_length=10, widget=forms.Select(choices=[('Male', 'Male'), ('Female', 'Female')]),label="Gender")
    BMI = forms.FloatField(label="BMI")
    BSA = forms.FloatField(label="BSA")
    ECOG = forms.CharField(max_length=40,widget=forms.Select(choices=[
        ('Fully active', 'Fully active'),
        ('Restricted in strenous activity', 'Restricted in strenous activity'),
        ('Capable of self-care', 'Capable of self-care'),
        ('Capable of limited self-care', 'Capable of limited self-care'),
        ('Completely disabled', 'Completely disabled'),
        ('Dead', 'Dead'),
    ]),label="ECOG")
    Substanceabuse = forms.CharField(max_length=40,widget=forms.Select(choices=[('TeeTotaler', 'TeeTotaler'), ('Not a TeeTotaler', 'Not a TeeTotaler')]))
    DiabetesCI = forms.CharField(max_length=40,widget=forms.Select(choices=[
        ('No Diabetes', 'No Diabetes'),
        ('Good control but no influence', 'Good control but no influence'),
        ('Controlled but partially influenced', 'Controlled but partially influenced'),
        ('Poor control and severely influenced', 'Poor control and severely influenced'),
    ]),label="Diabetes CI")
    HeartDiseaseCI = forms.CharField(max_length=40,widget=forms.Select(choices=[
        ('No heart Disease', 'No heart Disease'),
        ('Diagnosed but good pumping', 'Diagnosed but good pumping'),
        ('Bypass but good pumping', 'Bypass but good pumping'),
        ('Bypass but bad pumping', 'Bypass but bad pumping'),
    ]),label="HeartDisease CI")
    EjectionFraction = forms.FloatField(label="Ejection Fraction")
    Weightloss = forms.FloatField(label="WightLoss(Kg)")
    Haemoglobin = forms.FloatField(label="Haemoglobin")
    WBC = forms.FloatField(label="WBC")
    ANC = forms.FloatField(label="ANC")
    PlatletCount = forms.FloatField(label="Platlet Count(L)")
    Creatininel = forms.FloatField(label="Creatinine Level")
    Creatininec = forms.FloatField(label="Creatinine Clearance")
    Bilrubin = forms.FloatField(label="Bilirubin(mg)")
    AST = forms.FloatField(label="AST/ALT")
    Albumin = forms.FloatField(label="Albumin")
    SpO2 = forms.FloatField(label="SpO2%")
    Heartrate = forms.FloatField(label="Heart Rate")
    PriorHospitalization = forms.CharField(max_length=20, widget=forms.Select(choices=[('>6 mo back', '>6 mo back'), ('3-6 mo back', '3-6 mo back'),('<3-1 mo', '<3-1 mo'),('<1 mo','<1 mo' )]))
    BP = forms.CharField(max_length=20,label="BP(systolic/diastolic)")
    Walking = forms.CharField(max_length=20, widget=forms.Select(choices=[(">100 mt", ">100 mt"), ('50-100 mt', '50-100 mt'),('50-100 mt', '50-100 mt'),('10-50 mt','10-50 mt' ),('<5 mt', '<5 mt')]),label="Limited Walking")
    Drug = forms.CharField(max_length=100, widget=forms.Select(choices=[('TKI/Antibody', 'TKI/Antibody'), ('Chemotherapy', 'Chemotherapy')]),label="Class of Chemo agents")
    Chemoagent = forms.IntegerField(widget=forms.Select(choices=[(1,1),(2,2),(3,3)]),label="Number of ChemoAgents")
    Dosingagent = forms.CharField(max_length=20, widget=forms.Select(choices=[("QW","QW"),("Q3W","Q3W"),("Q3W,Q2W","Q3W,Q2W"),("Q2W,QW","Q2W,QW")]),label="Dosing Agent")
    Setting = forms.CharField(max_length=100,widget=forms.Select(choices=[("NACT", "NACT"), ("Adjuvant", "Adjuvant"),("Relapsed 1","Relapsed 1"),("Relapsed 2","Relapsed 2")]))
    SocialSupport = forms.CharField(max_length=20, widget=forms.Select(choices=[("Good", "Good"), ("Poor", "Poor"),("NIL","NIL")]),label="Social Support")
    MentalState = forms.CharField(max_length=20, widget=forms.Select(choices=[('Normal ,stable', 'Normal ,stable'), ("Depressed ,stable", "Depressed ,stable"), ("Emotional/unstable", "Emotional/unstable"),("Psychiatric illness", "Psychiatric illness")]),label="Mental State")
    DistanceFH = forms.CharField(max_length=20, widget=forms.Select(choices=[('Local', 'Local'), ('<50 km', '<50 km'),('50-100 km','50-100 km'),('>100 km','>100 km')]),label="Distance From Home(km)")
    CancerType = forms.CharField (max_length=100,widget=forms.Select(choices=[("Carcinoma", "Carcinoma") , ("Carcinosarcoma", "Carcinosarcoma"),("Sarcoma", "Sarcoma")]),label="Cancer Type")
    Gradeg = forms.CharField(max_length=100, widget=forms.Select(choices=[("Low Grade", "Low Grade"), ("High Grade", "High Grade")]),label="Grade")
    StageBurden = forms.CharField(max_length=100,widget=forms.Select(choices=[("None", "None"), ("Low Tumour Burden", "Low Tumour Burden"), ("High Tumour Burden", "High Tumour Burden")]),label="Stage Burden")
    ChemoTolerance = forms.CharField(max_length=100,widget=forms.Select(choices=[("Good", "Good"), ("Fatigue,neutropenia(G1,2),no fever", "Fatigue,neutropenia(G1,2),no fever"), ("Febrile Neutropenia G3/4", "Febrile Neutropenia G3/4")]),label="Chemo Tolerance")
    DuringChemo = forms.CharField(max_length=100,widget=forms.Select(choices=[("No change", "No change"), ("Down,but improved", "Down,but improved"),("PS 3,still not recovered","PS 3,still not recovered")]),label="PS during chemo")
    Cycle = forms.IntegerField(label="Cycle")