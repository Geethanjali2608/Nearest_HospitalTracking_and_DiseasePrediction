import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
#fungal infection,allergy,dengue,covid,heart attack,arthritis,migrane,asthama,hepatitis B,gasteroenteritis
disease=['fungal infection','allergy,dengue','covid','heart attack','arthritis','migraine','asthama','hepatitis B','gasteroenteritis']
l1=['itching','skin rash','continous sneezing','shivering','joint pain','loss of sense of taste and smell','running nose','fever',
    'breathlessness','sweating','dehydration','irregular sugar level','chest pain','swelling of joints and limbs','muscle weakness',
    'decreased activity','muscle stiffness','headache','vomiting','extreme sensitivity','dizziness','wheezing','coughing',
    'troubled sleep','fatigue','loss of appetite','abdominal pain','stomach cramp','watery diarrhea']
l2=[]
for x in range(0,len(l1)):
    l2.append(0)
#testing
a=pd.read_csv("testing.csv")
a.replace({'prognosis':{'fungal infection':0,'allergy':1,'dengue':2,'covid':3,'heart attack':4,'arthritis':5,'migraine':6,'asthama':7,
                        'hepatitis B':8,'gasteroenteritis':9}},inplace=True)
xtest=a[l1]
ytest=a[["prognosis"]]
np.ravel(ytest)
#training
b=pd.read_csv("training.csv")
b.replace({'prognosis':{'fungal infection':0,'allergy':1,'dengue':2,'covid':3,'heart attack':4,'arthritis':5,'migraine':6,'asthama':7,
                        'hepatitis B':8,'gasteroenteritis':9}},inplace=True)
x=a[l1]
y=b[["prognosis"]]
np.ravel(y)
def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" ):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(x,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(xtest)
    print(accuracy_score(ytest, y_pred))
    print(accuracy_score(ytest, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")

root = Tk()
root.title(" Disease Prediction From Symptoms")
root.configure()

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)


w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)


lr = Button(root, text="Predict",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=2)


NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)

root.mainloop()