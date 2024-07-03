from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import cancerdb
from .forms import insert,display,search,update,update1,delete1
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect

# def password_login(request):
#     if request.method == 'POST':
#         password = request.POST.get('password')
#         if password == settings.SINGLE_PASSWORD:
#             request.session['authenticated'] = True
#             return redirect('home')  # or any other default view
#         else:
#             messages.error(request, 'Invalid password')
#     return render(request, 'password_login.html')
def password_login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password == settings.SINGLE_PASSWORD:
            # Store the information in the session to remember the login state
            request.session['authenticated'] = True
            return redirect('home')
        else:
            messages.error(request, 'Invalid password, please try again.')

    return render(request, 'password_login.html')

def custom_logout_view(request):
    logout(request)  # This will clear the session and log out the user
    return redirect('password_login/')

def home(request,id=None):
    if(request.method=='POST'):
        if not request.session.get('authenticated'):
            return redirect('password_login')
        if 'in' in request.POST:
            return HttpResponseRedirect('/insert/')
        elif 'up' in request.POST:
            return HttpResponseRedirect('/update/')
        elif 'dis' in request.POST:
            return HttpResponseRedirect('/display/')
        elif 'se' in request.POST:
            return HttpResponseRedirect('/search/')
        else:
            return HttpResponseRedirect('/delete/')
    return render(request,'home.html')
def insert_view(request):
    global pid, pname, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw , apcw, coca, di, sett, ss, dfh, ms, ct, gra, sb, pct, psdc,disthome
    form = insert()
    if request.method == 'POST':
        form = insert(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['Patient_Id']
            pname = form.cleaned_data['Patient_name']
            age = form.cleaned_data['Age']
            gender = form.cleaned_data['Gender']
            bmi = form.cleaned_data['BMI']
            bsa = form.cleaned_data['BSA']
            ecog = form.cleaned_data['ECOG']
            atta = form.cleaned_data['Substanceabuse']
            diabetes = form.cleaned_data['DiabetesCI']
            hdci = form.cleaned_data['HeartDiseaseCI']
            ef = form.cleaned_data['EjectionFraction']
            wl = form.cleaned_data['Weightloss']
            hv = form.cleaned_data['Haemoglobin']
            wbc = form.cleaned_data['WBC']
            anc = form.cleaned_data['ANC']
            pc = form.cleaned_data['PlatletCount']
            src = form.cleaned_data['Creatininel']
            cc = form.cleaned_data['Creatininec']
            bili = form.cleaned_data['Bilrubin']
            astalt = form.cleaned_data['AST']
            albu = form.cleaned_data['Albumin']
            spo = form.cleaned_data['SpO2']
            hr = form.cleaned_data['Heartrate']
            pho = form.cleaned_data['PriorHospitalization']
            bp = form.cleaned_data['BP']
            lw = form.cleaned_data['Walking']
            apcw = form.cleaned_data['Drug']
            coca = form.cleaned_data['Chemoagent']
            di = form.cleaned_data['Dosingagent']
            sett = form.cleaned_data['Setting']
            ss = form.cleaned_data['SocialSupport']
            disthome = form.cleaned_data['DistanceFH']
            dfh = form.cleaned_data['MentalState']
            ms = form.cleaned_data['CancerType']
            ct = form.cleaned_data['Gradeg']
            gra = form.cleaned_data['StageBurden']
            sb = form.cleaned_data['ChemoTolerance']
            pct = form.cleaned_data['DuringChemo']
            psdc = form.cleaned_data['Cycle']
            l2 = [pid , pname, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss,disthome , dfh, ms, ct, gra, sb, pct, psdc]
            ans = calculation_view()
            p = cancerdb(
                m_Patient_Id=pid,m_Patient_name=pname,m_Age=age, m_Gender=gender, m_BMI=bmi, m_BSA=bsa, m_ECOG=ecog, m_Substanceabuse=atta,
                m_DiabetesCI=diabetes, m_HeartDiseaseCI=hdci, m_EjectionFraction=ef, m_Weightloss=wl,
                m_Haemoglobin=hv, m_WBC=wbc, m_ANC=anc, m_PlatletCount=pc, m_Creatininel=src, m_Creatininec=cc,
                m_Bilrubin=bili, m_AST=astalt, m_Albumin=albu, m_SpO2=spo, m_Heartrate=hr, m_PriorHospitalization=pho,
                m_BP=bp, m_Walking=lw, m_Drug=apcw, m_Chemoagent=coca, m_Dosingagent=di, m_Setting=sett, m_SocialSupport=ss,m_DistanceFH=disthome,
                m_MentalState=dfh, m_CancerType=ms, m_Gradeg=ct, m_StageBurden=gra, m_ChemoTolerance=sb, m_DuringChemo=pct,
                m_Cycle=psdc,m_Therapy_Suggested=ans[38]
            )
            p.save()
            # l2 = [pid , pname, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss,disthome , dfh, ms, ct, gra, sb, pct, psdc]
            # ans = calculation_view()
            request.session['ans'] = ans
            return render(request,'calculate.html',{'post':l2,'l':ans})
    return render(request, 'insert.html', {'form': form})
def update1_view(request):
    global pid,pname, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss, dfh, ms, ct, gra, sb, pct, psdc
    form = update1()
    if request.method == 'POST':
        form = update1(request.POST)
        if form.is_valid():
            pid=form.cleaned_data['Patient_Id']
            return HttpResponseRedirect('/update/'+str(pid))
    return render(request,'update1.html',{'form':form})
def update_view(request,id):
    global pid,pname, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss, dfh, ms, ct, gra, sb, pct, psdc,ans,disthome
    p=cancerdb.objects.get(m_Patient_Id=id)
    form=update(instance=p)
    if(request.method == 'POST'):
        form=update(request.POST,instance=p)
        if(form.is_valid()):
            pid=p.m_Patient_Id
            pname=p.m_Patient_name
            age = p.m_Age
            gender = p.m_Gender
            bmi = p.m_BMI
            bsa = p.m_BSA
            ecog = p.m_ECOG
            atta = p.m_Substanceabuse
            diabetes = p.m_DiabetesCI
            hdci = p.m_HeartDiseaseCI
            ef = p.m_EjectionFraction
            wl = p.m_Weightloss
            hv = p.m_Haemoglobin
            wbc = p.m_WBC
            anc = p.m_ANC
            pc = p.m_PlatletCount
            src = p.m_Creatininel
            cc = p.m_Creatininec
            bili = p.m_Bilrubin
            astalt = p.m_AST
            albu = p.m_Albumin
            spo = p.m_SpO2
            hr = p.m_Heartrate
            pho = p.m_PriorHospitalization
            bp = p.m_BP
            lw = p.m_Walking
            apcw = p.m_Drug
            coca = p.m_Chemoagent
            di = p.m_Dosingagent
            sett = p.m_Setting
            ss = p.m_SocialSupport
            disthome = p.m_DistanceFH
            dfh = p.m_MentalState
            ms = p.m_CancerType
            ct = p.m_Gradeg
            gra = p.m_StageBurden
            sb = p.m_ChemoTolerance
            pct = p.m_DuringChemo
            psdc = p.m_Cycle
            form.save()
            l2 = [pid,pname, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss,disthome , dfh, ms, ct, gra, sb, pct, psdc]
            ans = calculation_view()
            request.session['ans'] = ans
            return render(request,'calculate.html',{'post':l2,'l':ans})
    return render(request,'update.html',{'form':form})
# def update1_view(request):
#     global pid, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss, dfh, ms, ct, gra, sb, pct, psdc,x
#     form = update1()
#     if request.method == 'POST':
#         form = update1(request.POST)
#         if form.is_valid():
#             pid=form.cleaned_data['Patient_Id']
#             p=cancerdb.objects.get(m_Patient_Id=pid)
#             p.m_Patient_Id=pid
#             x=p.m_Patient_Id
#             return HttpResponseRedirect('/update1/')
#     return render(request,'update1.html',{'form':form})
# def update_view(request):
#     global pid, age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw, apcw, coca, di, sett, ss, dfh, ms, ct, gra, sb, pct, psdc,ans
#     patient=cancerdb.objects.get(m_Patient_Id=x)
#     form=update(instance=patient)
#     if(request.method == 'POST'):
#         form=update(request.POST,instance=patient)
#         if(form.is_valid()):
#             form.save()
#             return HttpResponseRedirect('/display/')
#     return render(request,'update.html',{'form':form})
def search_view(request):
    global pid, pname , age, gender, bmi, bsa, ecog, atta, diabetes, hdci, ef, wl, hv, wbc, anc, pc, src, cc, bili, astalt, albu, spo, hr, pho, bp, lw , apcw, coca, di, sett, ss, dfh, ms, ct, gra, sb, pct, psdc,disthome,ans
    form=search()
    if(request.method == 'POST'):
        form=search(request.POST)
        if(form.is_valid()):
            pid=form.cleaned_data['Patient_Id']
            p=cancerdb.objects.get(m_Patient_Id=pid)
            pname = p.m_Patient_name
            age = p.m_Age
            gender = p.m_Gender
            bmi = p.m_BMI
            bsa = p.m_BSA
            ecog = p.m_ECOG
            atta = p.m_Substanceabuse
            diabetes = p.m_DiabetesCI
            hdci = p.m_HeartDiseaseCI
            ef = p.m_EjectionFraction
            wl = p.m_Weightloss
            hv = p.m_Haemoglobin
            wbc = p.m_WBC
            anc = p.m_ANC
            pc = p.m_PlatletCount
            src = p.m_Creatininel
            cc = p.m_Creatininec
            bili = p.m_Bilrubin
            astalt = p.m_AST
            albu = p.m_Albumin
            spo = p.m_SpO2
            hr = p.m_Heartrate
            pho = p.m_PriorHospitalization
            bp = p.m_BP
            lw = p.m_Walking
            apcw = p.m_Drug
            coca = p.m_Chemoagent
            di = p.m_Dosingagent
            sett = p.m_Setting
            ss = p.m_SocialSupport
            disthome = p.m_DistanceFH
            dfh = p.m_MentalState
            ms = p.m_CancerType
            ct = p.m_Gradeg
            gra = p.m_StageBurden
            sb = p.m_ChemoTolerance
            pct = p.m_DuringChemo
            psdc = p.m_Cycle
            ans = calculation_view()
            request.session['ans'] = ans
            return render(request,'search.html',{'form':form,'key':p,'l':ans })
    return render(request,'search.html',{'form':form})
def delete_view(request):
    form=delete1()
    if(request.method == 'POST'):
        form=delete1(request.POST)
        if(form.is_valid()):
            pid=form.cleaned_data['Patient_Id']
            p=cancerdb.objects.filter(m_Patient_Id=pid)
            p.delete()
            return HttpResponseRedirect('/display/')
            # data=cancerdb.objects.all()
            # return render(request,'delete.html',{'form':form,'temp':data})
    return render(request,'delete.html',{'form':form})
def display_view(request):
    form=cancerdb.objects.all()
    # ans = calculation_view()
    ans = request.session.get('ans')
    return render(request,'display.html',{'form':form, 'l': ans})


def calculation_view():
    global x
    val_age = 0
    val_gender = 0
    val_bmi = 0
    val_bsa = 0
    val_ecog = 0
    val_atta = 0
    val_diabetes = 0
    val_hdci = 0
    val_ef = 0
    val_wl = 0
    val_hv = 0
    val_wbc = 0
    val_anc = 0
    val_cc=0
    val_bili = 0
    val_pc = 0
    val_src = 0
    val_hr = 0
    val_spo = 0
    val_albu = 0
    val_astalt = 0
    score_bp = 0
    score_di = 0
    score_pct = 0
    score_ss = 0
    score_dfh = 0
    score_sett = 0
    score_ms = 0
    score_sb = 0
    score_ct = 0
    val_gra = 0
    val_psdc = 0
    val_coca = 0
    val_lw = 0
    val_ph = 0
    val_disthome = 0
    val_classagents = 0
    
    if age>=18 and age<=39:
        val_age=0
    elif age>=40 and age<=49:
        val_age=1
    elif age>=50 and age<=59:
        val_age=2
    elif age>=60 and age<=65:
        val_age=3
    elif age>=66 and age<=70:
        val_age=4
    elif age>=71 and age<=100:
        val_age=5

    if gender == 'Male':
        val_gender = 0
    elif gender == 'Female':
        val_gender = 1

    if bmi >= 18.5 and bmi <= 24.9:
        val_bmi = 0
    elif bmi >= 25.0 and bmi <= 29.9:
        val_bmi = 1
    elif bmi >= 30.0 or bmi < 18.5:
        val_bmi = 2

    if bsa >= 1.3 and bsa <= 1.7:
        val_bsa = 0 
    elif bsa == 1.2 or bsa == 1.8:
        val_bsa = 1
    elif bsa >= 1.9 or (bsa >= 1.0 and bsa <= 1.1):
        val_bsa = 2

    if ecog == 'Fully active':
        val_ecog = 0
    elif ecog == 'Restricted in strenous activity':
        val_ecog = 1
    elif ecog == 'Capable of self-care':
        val_ecog = 2
    elif ecog == 'Capable of limited self-care':
        val_ecog = 3
    elif ecog == 'Completely disabled':
        val_ecog = 4
    elif ecog == 'Dead':
        val_ecog = 5

    if atta == 'TeeTotaler':
        val_atta = 0
    elif atta == 'Not a TeeTotaler':
        val_atta = 1
    
    if diabetes == 'No Diabetes':
        val_diabetes = 0
    elif diabetes == 'Good control but no influence':
        val_diabetes = 1
    elif diabetes == 'Controlled but partially influenced':
        val_diabetes = 2
    elif diabetes == 'Poor control and severely influenced':
        val_diabetes = 3

    if hdci == 'No heart Disease':
        val_hdci = 0
    elif hdci == 'Diagnosed but good pumping':
        val_hdci = 1
    elif hdci == 'Bypass but good pumping':
        val_hdci = 2
    elif hdci == 'Bypass but bad pumping':
        val_hdci = 3

    if ef < 30:
        val_ef = 4
    elif ef >= 30 and ef <= 39:
        val_ef = 3
    elif ef >= 40 and ef <= 49:
        val_ef = 2
    elif ef >= 50 and ef <= 59:
        val_ef = 1
    elif ef >= 60 and ef <= 69:
        val_ef = 0

    if wl == 0:
        val_wl = 0
    elif wl < 5:
        val_wl = 1
    elif wl >= 5:
        val_wl = 2
    
    if hv >= 12.0 and hv <= 14:
        val_hv = 0
    elif hv >= 10.0 and hv <= 11.9:
        val_hv = 1
    elif hv >= 8.0 and hv <= 9.9:
        val_hv = 2
    elif hv >= 7.0 and hv <= 7.9:
        val_hv = 3
    elif hv < 6.9:
        val_hv = 4
    
    if wbc >= 6000 and wbc <= 11000:
        val_wbc = 0
    elif wbc >= 4500 and wbc < 6000:
        val_wbc = 1
    elif wbc >= 4000 and wbc < 4500:
        val_wbc = 2
    elif wbc >= 3000 and wbc < 4000:
        val_wbc = 3
    elif wbc > 0 and wbc < 3000:
        val_wbc = 4

    if anc > 0 and anc < 1500:
        val_anc = 3
    elif anc >= 1500 and anc < 2000:
        val_anc = 2
    elif anc >= 2000 and anc < 4000:
        val_anc = 1
    elif anc >= 4000:
        val_anc = 0

    if pc >= 2.5 and pc < 4.5:
        val_pc = 0
    elif pc >= 1.5 and pc < 2.5:
        val_pc = 1
    elif pc >= 1.0 and pc < 1.5:
        val_pc = 2
    elif pc >= 0.75 and pc < 1.0:
        val_pc = 3
    elif pc < 0.75:
        val_pc = 8

    if 0.7 <= src <= 1.0:
        val_src = 0
    elif 1.1 <= src <= 1.2:
        val_src = 1
    elif 1.3 <= src <= 1.39:
        val_src = 2
    elif 1.4 <= src <= 1.49:
        val_src = 3
    elif src >= 1.5:
        val_src = 4

    if 100 <= cc <=140:
        val_cc = 0
    elif 80 <= cc <= 99:
        val_cc = 1
    elif 60 <= cc <= 79:
        val_cc = 2
    elif 50 <= cc < 60:
        val_cc = 3
    elif cc <= 49:
        val_cc = 4

    if 0.1 <= bili <= 1.2:
        val_bili = 0
    elif 1.3 <= bili <= 2:
        val_bili = 1
    elif 2.1 <= bili <= 3:
        val_bili = 2
    elif bili > 3:
        val_bili = 3

    if astalt <= 40:
        val_astalt = 0
    elif 40 <= astalt <= 120:
        val_astalt = 1
    elif 120 <= astalt <= 180:
        val_astalt = 2
    elif astalt > 180:
        val_astalt = 3

    if 3.5 <= albu <= 5.0:
        val_albu = 0
    elif  3 <= albu <= 3.5:
        val_albu = 1
    elif  2.5 <= albu <= 3.0:
        val_albu = 2
    elif  2 <= albu <= 2.4:
        val_albu = 3
    elif albu <= 2:
        val_albu = 4

    if spo >= 96:
        val_spo = 0
    elif spo == 95:
        val_spo = 1
    elif spo == 93 or spo == 94:
        val_spo = 2
    elif spo <= 92:
        val_spo = 3

    if 60 <= hr <=100:
        val_hr = 0
    elif 101 <= hr <= 109:
        val_hr = 1
    elif 110 <= hr <= 130:
        val_hr = 2
    elif hr >= 131:
        val_hr = 3
    
    if pho == '>6 mo back':
        val_ph = 0
    elif pho == '3-6 mo back':
        val_ph = 1
    elif pho == '<3-1 mo':
        val_ph = 2
    elif pho == '<1 mo':
        val_ph = 3
    
    if lw == ">100 mt":
        val_lw = 0
    elif lw == '50-100 mt':
        val_lw = 1
    elif lw == '10-50 mt':
        val_lw = 2
    elif lw == '5-10 mt':
        val_lw = 3
    elif lw == '<5 mt':
        val_lw = 4
    
    if coca == 1:
        val_coca = 0 
    elif coca == 2:
        val_coca = 1
    elif coca == 3:
        val_coca = 2
    
    if psdc in range(1,4):
        val_psdc = 0
    elif psdc in range(4,7):
        val_psdc = 1
    
    if gra =="None":
        val_gra = 0
    elif gra =="Low Tumour Burden":
        val_gra = 1
    elif gra =="High Tumour Burden":
        val_gra = 2
    
    if ct == "Low Grade":
        score_ct = 0
    elif ct == "High Grade":
        score_ct = 1
        
    if apcw == 'TKI/Antibody':
        val_classagents = 0
    elif apcw == 'Chemotherapy':
        val_classagents = 1

    if sb == "Good":
        score_sb = 0
    elif sb =="Fatigue,neutropenia(G1,2),no fever":
        score_sb = 1
    elif sb ==  "Febrile Neutropenia G3/4":
        score_sb = 2
    
    if ms == "Carcinoma":
        score_ms = 0
    elif ms =="Carcinosarcoma":
        score_ms = 1                
    elif ms =="Sarcoma":
        score_ms = 2
    
    if sett == "NACT":
        score_sett = 0
    elif sett == "Adjuvant":
        score_sett = 1
    elif sett == "Relapsed 1":
        score_sett = 2
    elif sett == "Relapsed 2":
        score_sett = 3 
    
    if dfh == "Normal ,stable":
        score_dfh = 0 
    if dfh == "Depressed ,stable":
        score_dfh = 1 
    if dfh == "Emotional/unstable":
        score_dfh = 2 
    if dfh == "Psychiatric illness":
        score_dfh = 3
        
    if ss == "Good":
        score_ss = 0
    elif ss == "Poor":
        score_ss = 1
    elif ss == "NIL":
        score_ss = 2
    
    if pct == "No change":
        score_pct = 0
    elif pct == "Down,but improved":
        score_pct = 1
    elif pct == "PS 3,still not recovered":
        score_pct = 2
        
    if disthome == 'Local':
        val_disthome = 0
    elif disthome == '<50 km':
        val_disthome = 1
    elif disthome == '50-100 km':
        val_disthome = 2
    elif disthome == '>100 km':
        val_disthome = 3

    if di == "QW":
        score_di = 0
    elif (di=="Q3W" or di == "Q3W,Q2W"):
        score_di = 1
    elif di == "Q2W,QW":
        score_di = 2
    
        
    h,l = bp.split('/')
    h=int(h)
    l=int(l)
    if (h in range(110,120)) and (l in range(70,80)):
        score_bp = 0
    elif ((h in range(120,130)) and (l in range(80,90))) or ((h in range(100,110)) and (l in range(60,70))):
        score_bp = 1
    elif ((h in range(130,140)) and (l in range(90,100))) or ((h in range(90,100) and (l < 60))):
        score_bp = 2
    elif ((h in range(140,160)) and (l in range(100,110))) or (((h < 90) and (l < 60))):
        score_bp = 3
    elif h > 160 and l > 120:
        score_bp = 4

    l1 = [val_age ,val_gender ,val_bmi ,val_bsa ,val_ecog ,val_atta ,val_diabetes ,val_hdci ,val_ef ,val_wl ,val_hv ,val_wbc ,val_anc ,val_pc,val_src,val_cc,val_bili ,val_astalt ,val_albu ,val_spo ,val_hr,val_ph,score_bp ,val_lw ,val_classagents ,val_coca ,score_di,score_sett ,score_ss,val_disthome,score_dfh,score_ms ,score_ct ,val_gra ,score_sb,score_pct,val_psdc]
    sum = 0
    # max_possibile_score = 110
    for i in l1:
        sum += i
    # risk_score = round(sum / max_possibile_score,3)
    # l1.append(risk_score)

    def cal_risk(r,sum):
        r1=[]
        rs=0
        maxi = 2.873312564901347
        for i in range (len(r)):
            r1.append(1-(r[i]/sum))
            rs+=r1[i]
        r2=[]
        for i in range(len(r1)):
            r2.append(r1[i]/rs)
        res=0
        for i in range(len(r2)):
            res+=r2[i]*r[i]
    
        result = ((res - 0)/(maxi - 0))
        return round(result , 4)
    
    risk_score = cal_risk(l1,sum)
    l1.append(risk_score)
    if 0 <= risk_score < 0.7:
        l1.append('Standard Theraphy')
    elif 0.7 <= risk_score <= 1.0:
        l1.append('Reduced Theraphy')
    # elif 0.2 <= risk_score < 0.3:
    #     l1.append('Oxaliplatin (Eloxatin)')
    # elif 0.3 <= risk_score < 0.4:
    #     l1.append('Irinotecan (Camptosar)')
    # elif 0.4 <= risk_score < 0.5:
    #     l1.append('Leucovorin (Folinic Acid)')
    # elif 0.5 <= risk_score < 0.6:
    #     l1.append('Bevacizumab (Avastin)')
    # elif 0.6 <= risk_score < 0.7:
    #     l1.append('Cetuximab (Erbitux) and Panitumumab (Vectibix)')
    # elif 0.7 <= risk_score < 0.8:
    #     l1.append('Trifluridine/Tipiracil (Lonsurf)')
    # elif 0.8 <= risk_score < 0.9:
    #     l1.append('Regorafenib (Stivarga)')
    # elif 0.9 <= risk_score < 1.0:
    #     l1.append('Ramucirumab (Cyramza)')
    
    # x = l1[-1]
    return l1