#!/usr/bin/env python
# coding: utf-8

# In[3]:


nama=input("Masukkan nama anda : ")
nim=input("Masukkan nim anda : ")
kkm = 70
teori = float(input("Masukkan nilai teori anda : "))
praktik = float(input("Masukan nilai praktik anda : "))
if teori and praktik >=kkm:
    print("Selamat %s, anda lulus!" %nama)
elif teori >=kkm and praktik <=kkm:
    print ("Mohon maaf %s, anda harus mengulang ujian praktik anda" %nama)
elif teori<kkm and praktik >=kkm:
    print("Mohon maaf %s, anda harus mengulang ujian teori anda" %nama)
else :
    print("Mohon maaf %s, anda harus mengulang ujian teori dan praktik anda" %nama)


# In[ ]:




