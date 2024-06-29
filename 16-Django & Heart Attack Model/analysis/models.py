from django.db import models

# Create your models here.
SEX_TYPE = (
    (1 , 'M') , 
    (0 , 'F')
)

EXANG_TYPE = (
    ( 1, 'Yes') , 
    ( 0, 'No')
)

CP_TYPE = (
    (1,'typical angina') , 
    (2,'atypical angina'),
    (3,'non-anginal pain'),
    (4,'asymptomatic'),
)

FBS_TYPE = (
    ( 1, 'Yes') , 
    ( 0, 'No')
)

REST_ECG_TYPE = (
    (0,'normal') , 
    (1,'having ST-T wave abnormality'),
    (2,'probable or definite left ventricular hypertrophy'),
)

TARGET_TYPE = (
    ( 1, 'Yes') , 
    ( 0, 'No')
)

class Patient(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX_TYPE)
    exang = models.IntegerField(choices=EXANG_TYPE,help_text='exercise induced angina')
    cp = models.IntegerField(choices=CP_TYPE,help_text='Chest Pain type')
    trtbps = models.IntegerField(help_text='resting blood pressure (in mm Hg)')
    chol = models.IntegerField(help_text='cholestoral in mg/dl fetched via BMI sensor')
    fbs = models.IntegerField(choices =FBS_TYPE,help_text='fasting blood sugar > 120 mg/dl')
    rest_ecg = models.IntegerField(choices=REST_ECG_TYPE,help_text='resting electrocardiographic results')
    oldpeak = models.FloatField()
    caa = models.FloatField()
    thall = models.FloatField()
    slp = models.FloatField()
    thalachh = models.FloatField()
    
    target = models.IntegerField(choices=TARGET_TYPE , null=True,blank=True)
    
    def __str__(self):
        return str(self.age)
    
    
    
    