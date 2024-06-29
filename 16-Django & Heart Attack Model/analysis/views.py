from django.shortcuts import render
from .forms import PatientForm
import sklearn
import pickle


def patient_analysis(request):
    print('read model')
    model = pickle.load(open('final_model.sav', 'rb'))
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            print('----------')
            form.save()

            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            exang = form.cleaned_data['exang']
            cp = form.cleaned_data['cp']
            trtbps = form.cleaned_data['trtbps']
            chol = form.cleaned_data['chol']
            fbs = form.cleaned_data['fbs']
            rest_ecg = form.cleaned_data['rest_ecg']
            caa = form.cleaned_data['caa']
            thall = form.cleaned_data['thall']
            slp = form.cleaned_data['slp']
            oldpeak = form.cleaned_data['oldpeak']  
            thalachh = form.cleaned_data['thalachh']  
            
            
            if sex == 1:
                sex = 0
            else:
                sex = 1
                
            if exang == 0:
                exang = 1
            else:
                exang = 0
                
            if cp==1:
                cp_2 = 0
                cp_3 = 0
                cp_4 = 0
                
            elif cp == 2:
                cp_2 = 1
                cp_3 = 0
                cp_4 = 0
            
            elif cp == 3:
                cp_2 = 0
                cp_3 = 1
                cp_4 = 0
                
            elif cp == 4:
                cp_2 = 0
                cp_3 = 0
                cp_4 = 1
            
            if fbs == 1:
                fbs = 0
            else:
                fbs = 1
                
            if caa == 0 : 
                caa_2 = 0
                caa_3 = 0
                caa_4 = 0
                caa_5 = 0
                
            elif caa == 1 : 
                caa_2 = 1
                caa_3 = 0
                caa_4 = 0
                caa_5 = 0

            elif caa == 2 : 
                caa_2 = 0
                caa_3 = 1
                caa_4 = 0
                caa_5 = 0

            elif caa == 3 : 
                caa_2 = 0
                caa_3 = 0
                caa_4 = 1
                caa_5 = 0

            elif caa == 4 : 
                caa_2 = 0
                caa_3 = 0
                caa_4 = 0
                caa_5 = 1


            if thall == 0:
                thall_1 = 0
                thall_2 = 0
                thall_3 = 0

            elif thall == 1:
                thall_1 = 1
                thall_2 = 0
                thall_3 = 0


            elif thall == 2:
                thall_1 = 0
                thall_2 = 1
                thall_3 = 0
                    

            elif thall == 3:
                thall_1 = 0
                thall_2 = 0
                thall_3 = 1

            if slp == 0:
                slp_1 = 0
                slp_2 = 0

            elif slp == 1:
                slp_1 = 1
                slp_2 = 0

            elif slp == 2:
                slp_1 = 0
                slp_2 = 1
                
                
                
            if rest_ecg == 0:
                rest_ecg_1 = 0
                rest_ecg_2 = 0

            elif rest_ecg == 1:
                rest_ecg_1 = 1
                rest_ecg_2 = 0

            elif rest_ecg == 2:
                rest_ecg_1 = 0
                rest_ecg_2 = 1

            data = [[int(age),trtbps,chol,thalachh,oldpeak,sex,cp_2,cp_3,cp_4,fbs,rest_ecg_1,rest_ecg_2,exang,slp_1,slp_2,caa_2,caa_3,caa_4,caa_5,thall_1,thall_2,thall_3]]
            result = model.predict(data)
            
            print(result) 
            print(type(result))
            
            return render(request,'analysis/analysis.html',{'form':form , 'result':int(result)})
        
        else:
            print('form is not valid')
    else:
        form = PatientForm()
    return render(request,'analysis/analysis.html',{'form':form})