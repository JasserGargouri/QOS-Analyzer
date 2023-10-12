from pandas.core.frame import DataFrame
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from pandas import ExcelWriter
from pandas import ExcelFile

import string
import time
import base64
import csv
import sqlite3
import hashlib
img = Image.open('ico.png')
st.set_page_config(page_title='QoS Analyser', page_icon=img, layout='centered', initial_sidebar_state='auto')
image = Image.open('final2.png')

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

#***************** STYLE ********************
st.image(image, caption='')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #FFFFFF;color:#000000;border-radius:10px 10px 10px 10px;font-size: 18px; font-weight:light;font-family:Neo Sans Std;
}
</style>""", unsafe_allow_html=True)

def display_app_header(main_txt,sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#253775;text_align:center;font-size:36px;font-family:Neo Sans Std;"> {main_txt} </h2>
    <p style = "color:#BB1D3F; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
def display_app_header2(main_txt,sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#253775; font-size: 24px;font-family:Neo Sans Std;"> {main_txt} </h2>
    <p style = "color:#BB1D3F; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
def display_app_header3(main_txt,sub_txt,subsub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    subsub_txt
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#253775; text_align:center; font-size: 20px;font-family:Neo Sans Std;"> {main_txt} </h2>
    <p style = "color:#253775; font-size: 20px;font-family:Neo Sans Std;"> {sub_txt} </p>
    <p style = "color:#253775; font-size: 18px;font-family:Neo Sans Std;"> {subsub_txt} </p>

    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
def display_app_header4(main_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    subsub_txt
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#FFFFFF; text_align:center; font-size: 26px;font-family:Neo Sans Std;"> {main_txt} </h2>
    

    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
def display_app_header5(main_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    subsub_txt
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#000000; text_align:left; font-size: 26px;font-family:Neo Sans Std;"> {main_txt} </h2>
    

    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
def display_app_header6(main_txt,sub_txt,subsub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    subsub_txt
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#EE5E43; text_align:center; font-size: 20px;font-family:Neo Sans Std;"> {main_txt} </h2>
    <p style = "color:#228B22; font-size: 18px;font-family:Neo Sans Std;"> {sub_txt} </p>
    <p style = "color:#DC143C; font-size: 18px;font-family:Neo Sans Std;"> {subsub_txt} </p>

    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
def display_app_header7(main_txt,sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#253775; font-size: 20px;font-family:Neo Sans Std light;"> {main_txt} </h2>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)
#@st.cache_data(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
     background-image: url("data:image/png;base64,%s");
     background-size: cover;
     
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


#***************** PAGE STYLE ********************


font = "neo sans std"
set_png_as_page_bg('background.png')
page_title="Optimisation de la QoS des réseaux mobiles"
#display_app_header(main_txt='Optimisation de la QoS des réseaux mobiles', sub_txt='')


st.text("")

imagelog = Image.open('log.png')
ccol8111, ccl222,ccol4333= st.columns(3)

with ccl222:
	st.image(imagelog, caption='')
ccol111, ccol222,ccol333= st.columns(3)

#***************** PAGE LOGIN ********************
result = False
menu = ["Connexion","S'inscrire"]
with ccol222:
 choicd = st.selectbox("",menu)

if choicd == "Connexion":
 display_app_header2(main_txt='Section de connexion', sub_txt='')
 #st.subheader("Section de connexion")
 
 ccol11, ccol22= st.columns(2)
 with ccol11:
  display_app_header7(main_txt="Nom d'utilisateur", sub_txt='')
  username = st.text_input("",key='675')
 with 	ccol22:
  display_app_header7(main_txt="Mot de passe", sub_txt='')
  password = st.text_input("",type='password',key='6565')

 if st.checkbox("Connexion"):
     create_usertable()
     hashed_pswd = make_hashes(password)

     result = login_user(username,check_hashes(password,hashed_pswd))
     if result:
         st.success("Connecté en tant que {}".format(username))
     else:
      st.warning(" Nom d'utilisateur ou Mot de passe Incorrect ")
if choicd == "S'inscrire":
 display_app_header2(main_txt='Créer un compte', sub_txt='')
 ccol1, ccol2= st.columns(2)
 with ccol1:
  display_app_header7(main_txt="Nom d'utilisateur", sub_txt='')
  new_user = st.text_input("",key = '326546')
 with ccol2:
  display_app_header7(main_txt="Mot de passe", sub_txt='')
  new_password = st.text_input("",type='password', key = '4646')
 
 if st.button("Créer le compte"):
     create_usertable()
     add_userdata(new_user,make_hashes(new_password))
     st.success("Vous avez créé avec succès un compte valide")
     st.info("Allez dans la section Connexion pour vous connecter")

#***************** FILE INPUT ********************

if result:
 display_app_header2(main_txt='Déposez le fichier à analyser (Excel ou CSV) :', sub_txt='')

 uploaded_file = st.file_uploader("")
 if uploaded_file is not None:  
  try:
   df = pd.read_csv(uploaded_file,sep=';')
  except Exception as e :
   df = pd.read_excel(uploaded_file)
  st.text("")
  display_app_header2(main_txt='Choisir la technologie :', sub_txt='')

  Genereations=['2G','3G','4G']
  Choises=st.selectbox( '',Genereations)
  st.text("")
   
   


#***************************   3G CONFIGURATION ****************




  if Choises=='3G':

      
       


     display_app_header2(main_txt='Choisir les paramètres 3G :', sub_txt='')
     calculation3G = st.multiselect('', ('RSCP','EC/NO','Débit3G'))
     
    
    #***************** RSCP CONFIGURATION ********************


     if 'RSCP' in calculation3G:
        #display_app_header(main_txt='RSCP', sub_txt='')
        image1 = Image.open('RSCP.png')
        st.image(image1, caption='')
        
        col111, col222 = st.columns(2)
        MIN=str(df['RSCP (active)'].min())
        MAX=str(df['RSCP (active)'].max())
        MOYE=str(round((df['RSCP (active)'].mean()),1))
        FMIN=df['RSCP (active)'].min()
        FMAX=df['RSCP (active)'].max()
        FMOYE=df['RSCP (active)'].mean()
        col111, col333= st.columns(2)
        with col111:
         display_app_header4(main_txt='   RSCP MIN :'+' '+MIN)

        with col333:
         display_app_header4(main_txt='RSCP MAX  :'+' '+MAX)

        display_app_header4(main_txt='RSCP MOYENNE :'+' '+MOYE)

       
        st.write('')
        
        col7, col8,col9, col10 = st.columns(4) 
        with col7:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne couverture :')
        with col8:
         TBC = st.text_input('',key='54')
         st.write( f"{TBC}" f" ≤ VALEUR < "f"{MAX}" )
            
        with col9:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne couverture:')
        with col10:
         BC = st.text_input('')
         st.write( f"{BC}" f" ≤ VALEUR < "f"{TBC}" )
        #with col19:
        col3, col4,col5, col6 = st.columns(4) 
        with col3:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne couverture:')
        with col4:
         MC = st.text_input(' ')
         st.write( f"{MC}" f" ≤ VALEUR < "f"{BC}" ) 
        with col5:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise couverture:')
        with col6:
         MAUC = st.text_input('  ')
         st.write( f"{MAUC}" f" ≤ VALEUR < "f"{MC}" )
        st.text("")
        st.text("")
        VERIF1 = TBC
        VERIF2 = BC
        VERIF3 = MC
        VERIF4 = MAUC

        if VERIF1:
           ITBC = float(TBC)
           if((ITBC>FMAX)or(ITBC<FMIN)):
              st.error(' Verifier la Seuil du Trés bonne couverture')
              
        if VERIF2:        
           IBC = float(BC)
           if((IBC>ITBC)or(IBC<FMIN)or(IBC>FMAX)): 
               st.error ('Verifier la seuil du  bonne couverture')
        if VERIF3:
           IMC = float(MC)
           if((IMC>IBC)or(IMC<FMIN)or(IMC>FMAX)): 
             st.error ('Verifier la Seuil du  Moyenne couverture')
        if VERIF4:
           IMAUC = float(MAUC)
           if(IMAUC>IMC): 
               st.error ('Verifier la Seuil du  Mauvaise couverture')
           #if((IBC<=ITBC)and(ITBC<=FMAX)and(ITBC>=FMIN)and(IBC>=FMIN)and(IMC<=IBC)and(IMC>=FMIN)and(IMAUC<=IMC)and(IMAUC>=FMIN)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de RSCP sont verifier sans erreurs',subsub_txt='')
               
           
    
    #***************** Ec/N0 CONFIGURATION ********************    
    


     if 'EC/NO' in calculation3G:
        #display_app_header(main_txt='Ec/No', sub_txt='')
        image2 = Image.open('ECNO.png')
        st.image(image2, caption='')
        st.write('')
        
        MINec=str(df['Ec/N0 (active)'].min())
        MAXec=str(df['Ec/N0 (active)'].max())
        MOYEec=str(round((df['Ec/N0 (active)'].mean()),1))
        FMINec=df['Ec/N0 (active)'].min()
        FMAXec=df['Ec/N0 (active)'].max()
        FMOYEec=df['Ec/N0 (active)'].mean()
        col111, col222 = st.columns(2)
        with col111:
         display_app_header4(main_txt='Ec/N0 MIN :'+' '+MINec)
         
        with col222:

								 display_app_header4(main_txt='Ec/N0 MAX :'+' '+MAXec)

        display_app_header4(main_txt='Ec/N0 MOYENNE :'+' '+MOYEec)

       
        st.write('')

        col7, col8,col9, col10 = st.columns(4) 
        with col7:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne qualité:')
        with col8:
         TBQ = st.text_input('',key='54766')
         st.write( f"{TBQ}" f" ≤ VALEUR < "f"{MAXec}" )

        
        with col9:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne qualité:')
        with col10:
         BQ = st.text_input('',key='876')
         st.write( f"{BQ}" f" ≤ VALEUR < "f"{TBQ}" )

        col3, col4,col5, col6 = st.columns(4) 
        with col3:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne qualité:')
        with col4:
         MQ = st.text_input(' ',key='567')
         st.write( f"{MQ}" f" ≤ VALEUR < "f"{BQ}" ) 
        with col5:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise qualité:')
        with col6:
         MAUQ = st.text_input('  ',key='54690')
         st.write( f"{MAUQ}" f" ≤ VALEUR < "f"{MQ}" )
        st.text("")
        st.text("")
        VERIFec1 = TBQ
        VERIFec2 = BQ
        VERIFec3 = MQ
        VERIFec4 = MAUQ

        if VERIFec1:
           ITBQ = float(TBQ)
           if((ITBQ>FMAXec)or(ITBQ<FMINec)):
                st.error ('Verifier la Seuil du Trés bonne qualité')
        if VERIFec2:     
           IBQ = float(BQ) 
           if((IBQ>ITBQ)or(IBQ<FMINec)or(IBQ>FMAXec)): 
                    st.error(' Verifier la seuil du  bonne qualité')
        if VERIFec3: 
           IMQ = float(MQ)
           if((IMQ>IBQ)or(IMQ<FMINec)or(IMQ>FMAXec)): 
                    st.error(' Verifier la Seuil du  Moyenne qualité')
        if VERIFec4: 
           IMAUQ = float(MAUQ)
           if(IMAUQ>IMQ):
               st.error('Verifier la Seuil du  Mauvaise qualité')
           #if((IBQ<=ITBQ)and(ITBQ<=FMAXec)and(ITBQ>=FMINec)and(IBQ>=FMINec)and(IMQ<=IBQ)and(IMQ>=FMINec)and(IMAUQ<=IMQ)and(IMAUQ>=FMINec)):
                    #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de Ec/N0 sont verifier sans erreurs',subsub_txt='')


    #***************** Debit3G CONFIGURATION ********************
        

     if 'Débit3G' in calculation3G:
         image3 = Image.open('Debit.png')
         st.image(image3, caption='')
         st.write('')
         st.write('')
         col07, col08,col011,col09, col010 = st.columns(5)

         with col08:
          DL=st.checkbox('Down Link')

         with col09: 
          UP=st.checkbox('Up Link')
         st.write('')
         
         if DL :
             display_app_header(main_txt='Débit DownLink', sub_txt='')
             st.write('')
             
             col111111, col222222 = st.columns(2)
             MINDL3G=str(df['Application throughput downlink'].min())
             MAXDL3G=str(df['Application throughput downlink'].max())
             MOYEDL3G=str(round(df['Application throughput downlink'].mean(),1))
             FMINDL3G=df['Application throughput downlink'].min()
             FMAXDL3G=df['Application throughput downlink'].max()
             FMOYEDL3G=df['Application throughput downlink'].mean()
             with col111111:
              display_app_header4(main_txt='Débit DL MIN :'+' '+MINDL3G)
                
             with col222222:

                display_app_header4(main_txt='Débit DL MAX :'+' '+MAXDL3G)

             display_app_header4(main_txt='Débit DL MOYENNE :'+' '+MOYEDL3G)

             st.write('') 
             st.write('')
             coll7, coll8,coll9, coll10 = st.columns(4) 
             with coll7:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne DL débit:')
             with coll8:
               TBDL = st.text_input('',key='169')
               st.write( f"{TBDL}" f" ≤ VALEUR < "f"{MAXDL3G}" )

        
             with coll9:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne DL débit:')
             with coll10:
              BDL = st.text_input('',key='584')
              st.write( f"{BDL}" f" ≤ VALEUR < "f"{TBDL}" )

             coll3, coll4,coll5, coll6 = st.columns(4) 
             with coll3:
                display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne DL débit:')
             with coll4:
                MDL = st.text_input(' ',key='1644')
                st.write( f"{MDL}" f" ≤ VALEUR < "f"{BDL}" ) 
             with coll5:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise DL débit:')
             with coll6:
               MAUDL = st.text_input('  ',key='21351')
               st.write( f"{MAUDL}" f" ≤ VALEUR < "f"{MDL}" )
             st.text("")
             st.text("")
             VERIFDL1 = TBDL
             VERIFDL2 = BDL
             VERIFDL3 = MDL
             VERIFDL4 = MAUDL

             if VERIFDL1:
              ITBDL = float(TBDL)
              if((ITBDL>FMAXDL3G)or(ITBDL<FMINDL3G)):
               st.error(' Verifier la Seuil du Trés bonne DL débit')
             if VERIFDL2:
              IBDL = float(BDL)
              if((IBDL>ITBDL)or(IBDL<FMINDL3G)or(IBDL>FMAXDL3G)): 
               st.error(' Verifier la seuil du  bonne DL débit')
             if VERIFDL3:
              IMDL = float(MDL)
              if((IMDL>IBDL)or(IMDL<FMINDL3G)or(IMDL>FMAXDL3G)): 
               st.error(' Verifier la Seuil du  Moyenne DL débit')
             if VERIFDL4:
              IMAUDL = float(MAUDL)
              if(IMAUDL>IMDL): 
               st.error(' Verifier la Seuil du  Mauvaise DL débit')

              #if((IBDL<=ITBDL)and(ITBDL<=FMAXDL3G)and(ITBDL>=FMINDL3G)and(IBDL>=FMINDL3G)and(IMDL<=IBDL)and(IMDL>=FMINDL3G)and(IMAUDL<=IMDL)and(IMAUDL>=FMINDL3G)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de DL débit sont verifier sans erreurs',subsub_txt='')
         if UP :
             display_app_header(main_txt='Débit UpLink', sub_txt='')
             st.write('')
             
             col1111111, col2222222 = st.columns(2)
             MINUL3G=str(df['Application throughput uplink'].min())
             MAXUL3G=str(df['Application throughput uplink'].max())
             MOYEUL3G=str(round(df['Application throughput uplink'].mean(),1))
             FMINUL3G=df['Application throughput uplink'].min()
             FMAXUL3G=df['Application throughput uplink'].max()
             FMOYEUL3G=df['Application throughput uplink'].mean()
             with col1111111:
              display_app_header4(main_txt='Débit UL MIN :'+' '+MINUL3G)
                
             with col2222222:

                display_app_header4(main_txt='Débit UL MAX :'+' '+MAXUL3G)

             display_app_header4(main_txt='Débit UL MOYENNE :'+' '+MOYEUL3G)

             st.write('')
             st.write('')
             cooll7, cooll8,cooll9, cooll10 = st.columns(4) 
             with cooll7:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne UL débit:')
             with cooll8:
               TBUL = st.text_input('',key='2161')
               st.write( f"{TBUL}" f" ≤ VALEUR < "f"{MAXUL3G}" )

        
             with cooll9:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne UL débit:')
             with cooll10:
              BUL = st.text_input('',key='66546')
              st.write( f"{BUL}" f" ≤ VALEUR < "f"{TBUL}" )

             cooll3, cooll4,cooll5, cooll6 = st.columns(4) 
             with cooll3:
                display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne UL débit:')
             with cooll4:
                MUL = st.text_input(' ',key='3378')
                st.write( f"{MUL}" f" ≤ VALEUR < "f"{BUL}" ) 
             with cooll5:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise UL débit:')
             with cooll6:
               MAUUL = st.text_input('  ',key='646')
               st.write( f"{MAUUL}" f" ≤ VALEUR < "f"{MUL}" )
             st.text("")
             st.text("")
             VERIFUL1 = TBUL
             VERIFUL2 = BUL
             VERIFUL3 = MUL
             VERIFUL4 = MAUUL
             
             if VERIFUL1:
              ITBUL = float(TBUL)
              if((ITBUL>FMAXUL3G)or(ITBUL<FMINUL3G)):
               st.error(' Verifier la Seuil du Trés bonne UL débit')
             if VERIFUL2:
              IBUL = float(BUL)
              if((IBUL>ITBUL)or(IBUL<FMINUL3G)or(IBUL>FMAXUL3G)): 
               st.error(' Verifier la seuil du  bonne UL débit')
             if VERIFUL3:
              IMUL = float(MUL)
              if((IMUL>IBUL)or(IMUL<FMINUL3G)or(IMUL>FMAXUL3G)): 
               st.error(' Verifier la Seuil du  Moyenne UL débit')
             if VERIFUL4:
              IMAUUL = float(MAUUL)
              if(IMAUUL>IMUL): 
               st.error(' Verifier la Seuil du  Mauvaise UL débit')
              #if((IBUL<=ITBUL)and(ITBUL<=FMAXUL3G)and(ITBUL>=FMINUL3G)and(IBUL>=FMINUL3G)and(IMUL<=IBUL)and(IMUL>=FMINUL3G)and(IMAUUL<=IMUL)and(IMAUUL>=FMINUL3G)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de UL débit sont verifier sans erreurs',subsub_txt='')
         
#***************************   4G CONFIGURATION ****************



    
  if Choises=='4G':
     display_app_header2(main_txt='Choisir les paramètres 4G :', sub_txt='')
     calculation4G = st.multiselect('', ('RSRP','RSRQ','Débit4G')) 

    

     
    #***************************   RSRP  CONFIGURATION ****************



     if 'RSRP' in calculation4G:
      
      image1 = Image.open('RSRP.png')
      st.image(image1, caption='')
      st.write('')
      col1111, col2222= st.columns(2)
      MIN4G=str(df['RSRP (pcell)'].min())
      MAX4G=str(df['RSRP (pcell)'].max())
      MOYE4G=str(round(df['RSRP (pcell)'].mean(),1))
      
      with col1111:
       display_app_header4(main_txt='MIN :'+' '+MIN4G)
         
      with col2222:
 
         display_app_header4(main_txt='MAX :'+' '+MAX4G)

      display_app_header4(main_txt='MOYENNE :'+' '+MOYE4G)

       
      st.write('')
      
      FMIN4G=df['RSRP (pcell)'].min()
      FMAX4G=df['RSRP (pcell)'].max()
      FMOYE4G=df['RSRP (pcell)'].mean()
      col7, col8,col9, col10 = st.columns(4) 
      with col7:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne couverture:')
      with col8:
       TBC4G = st.text_input('',key='547656')
       st.write( f"{TBC4G}" f" ≤ VALEUR < "f"{MAX4G}" )

        
      with col9:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne couverture:')
      with col10:
       BC4G = st.text_input('',key='87546')
       st.write( f"{BC4G}" f" ≤ VALEUR < "f"{TBC4G}" )

      col3, col4,col5, col6 = st.columns(4) 
      with col3:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne couverture:')
      with col4:
       MC4G = st.text_input(' ',key='5656727')
       st.write( f"{MC4G}" f" ≤ VALEUR < "f"{BC4G}" ) 
      with col5:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise couverture:')
      with col6:
       MAUC4G = st.text_input('  ',key='5469980')
       st.write( f"{MAUC4G}" f" ≤ VALEUR < "f"{MC4G}" )
      st.text("")
      st.text("")
      VERIF1 = TBC4G
      VERIF2 = BC4G
      VERIF3 = MC4G
      VERIF4 = MAUC4G
         
      if VERIF1:
           ITBC4G = float(TBC4G)
           if((ITBC4G>FMAX4G)or(ITBC4G<FMIN4G)):
              st.error(' Verifier la Seuil du Trés bonne couverture')
      if VERIF2:
           IBC4G = float(BC4G)
           if((IBC4G>ITBC4G)or(IBC4G<FMIN4G)or(IBC4G>FMAX4G)): 
               st.error(' Verifier la seuil du  bonne couverture')
      if VERIF3:
           IMC4G = float(MC4G)
           if((IMC4G>IBC4G)or(IMC4G<FMIN4G)or(IMC4G>FMAX4G)): 
               st.error(' Verifier la Seuil du  Moyenne couverture')
      if VERIF4:
           IMAUC4G = float(MAUC4G)
           if(IMAUC4G>IMC4G)or(IMAUC4G<FMIN4G): 
               st.error('Verifier la Seuil du  Mauvaise couverture')
           #if((IBC4G<=ITBC4G)and(ITBC4G<=FMAX4G)and(ITBC4G>=FMIN4G)and(IBC4G>=FMIN4G)and(IMC4G<=IBC4G)and(IMC4G>=FMIN4G)and(IMAUC4G<=IMC4G)and(IMAUC4G>=FMIN4G)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de RSRP sont verifier sans erreurs',subsub_txt='')
    #***************************   RSRQ  CONFIGURATION ****************
     
     if 'RSRQ' in calculation4G:
      #display_app_header(main_txt='RSRQ', sub_txt='')
      image2 = Image.open('RSRQ.png')
      st.image(image2, caption='')
      st.write('')
      col11111, col22222 = st.columns(2)
      MINsc4G=str(df['RSRQ (pcell)'].min())
      MAXsc4G=str(df['RSRQ (pcell)'].max())
      MOYEsc4G=str(round(df['RSRQ (pcell)'].mean(),1))
      FMINsc4G=df['RSRQ (pcell)'].min()
      FMAXsc4G=df['RSRQ (pcell)'].max()
      FMOYEsc4G=df['RSRQ (pcell)'].mean()
      
      with col11111:
       display_app_header4(main_txt='RSRQ MIN :'+' '+MINsc4G)
         
      with col22222:
   
         display_app_header4(main_txt='RSRQ MAX :'+' '+MAXsc4G)


      display_app_header4(main_txt='RSRQ MOYENNE :'+' '+MOYEsc4G)

      st.write('')

      col77, col88,col99, col100 = st.columns(4) 
      with col77:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne Qualié:')
      with col88:
       TBCsc4G = st.text_input('',key='5476')
       st.write( f"{TBCsc4G}" f" ≤ VALEUR < "f"{MAXsc4G}" )

        
      with col99:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne Qualité:')
      with col100:
       BCsc4G = st.text_input('',key='6783753')
       st.write( f"{BCsc4G}" f" ≤ VALEUR < "f"{TBCsc4G}" )

      col33, col44,col55, col66 = st.columns(4) 
      with col33:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne Qualité:')
      with col44:
       MCsc4G = st.text_input(' ',key='7387')
       st.write( f"{MCsc4G}" f" ≤ VALEUR < "f"{BCsc4G}" ) 
      with col55:
       display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise Qualité:')
      with col66:
       MAUCsc4G = st.text_input('  ',key='3783')
       st.write( f"{MAUCsc4G}" f" ≤ VALEUR < "f"{MCsc4G}" )
       st.text("")
      st.text("")
      VERIFsc1 = TBCsc4G
      VERIFsc2 = BCsc4G
      VERIFsc3 = MCsc4G
      VERIFsc4 = MAUCsc4G
         
      if VERIFsc1:
           ITBCsc4G = float(TBCsc4G)
           if((ITBCsc4G>FMAXsc4G)or(ITBCsc4G<FMINsc4G)):
              st.error(' Verifier la Seuil du Trés bonne couverture')
      if VERIFsc2:
           IBCsc4G = float(BCsc4G)
           if((IBCsc4G>ITBCsc4G)or(IBCsc4G<FMINsc4G)or(IBCsc4G>FMAXsc4G)): 
               st.error(' Verifier la seuil du bonne couverture')
      if VERIFsc3:
           IMCsc4G = float(MCsc4G)
           if((IMCsc4G>IBCsc4G)or(IMCsc4G<FMINsc4G)or(IMCsc4G>FMAXsc4G)): 
               st.error(' Verifier la Seuil du Moyenne couverture')
      if VERIFsc4:
           IMAUCsc4G = float(MAUCsc4G)
           if(IMAUCsc4G>IMCsc4G)or(IMAUCsc4G<FMINsc4G): 
               st.error(' Verifier la Seuil du Mauvaise couverture')
      
           #if((IBCsc4G<=ITBCsc4G)and(ITBCsc4G<=FMAXsc4G)and(ITBCsc4G>=FMINsc4G)and(IBCsc4G>=FMINsc4G)and(IMCsc4G<=IBCsc4G)and(IMCsc4G>=FMINsc4G)and(IMAUCsc4G<=IMCsc4G)and(IMAUCsc4G>=FMINsc4G)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de RSRQ sont verifier sans erreurs',subsub_txt='')
    #***************************   DEBIT  CONFIGURATION ****************
     if 'Débit4G' in calculation4G:
         #display_app_header(main_txt='RLC throughput', sub_txt='')
         image3 = Image.open('Debit.png')
         st.image(image3, caption='')
         st.write('')
         st.write('')
         col07, col08,col011,col09, col010 = st.columns(5)

         with col08:
          DL=st.checkbox('Down Link')

         with col09: 
          UP=st.checkbox('Up Link')
         st.write('')
         
         if DL :
             display_app_header(main_txt='Débit Down Link', sub_txt='')
             st.write('')
             
             col111111, col222222= st.columns(2)
             MINDL4G=str(df['RLC downlink throughput'].min())
             MAXDL4G=str(df['RLC downlink throughput'].max())
             MOYEDL4G=str(round(df['RLC downlink throughput'].mean(),1))
             FMINDL4G=df['RLC downlink throughput'].min()
             FMAXDL4G=df['RLC downlink throughput'].max()
             FMOYEDL4G=df['RLC downlink throughput'].mean()        
             with col111111:
              display_app_header4(main_txt='Débit DL MIN :'+' '+MINDL4G)
                
             with col222222:

                display_app_header4(main_txt='Débit DL MAX :'+' '+MAXDL4G)

             display_app_header4(main_txt='Débit DL MOYENNE :'+' '+MOYEDL4G)

             st.write('') 
             st.write('')
             coll7, coll8,coll9, coll10 = st.columns(4) 
             with coll7:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne DL débit:')
             with coll8:
               TBDL = st.text_input('',key='169')
               st.write( f"{TBDL}" f" ≤ VALEUR < "f"{MAXDL4G}" )

        
             with coll9:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne DL débit:')
             with coll10:
              BDL = st.text_input('',key='584')
              st.write( f"{BDL}" f" ≤ VALEUR < "f"{TBDL}" )

             coll3, coll4,coll5, coll6 = st.columns(4) 
             with coll3:
                display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne DL débit:')
             with coll4:
                MDL = st.text_input(' ',key='1644')
                st.write( f"{MDL}" f" ≤ VALEUR < "f"{BDL}" ) 
             with coll5:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise DL débit:')
             with coll6:
               MAUDL = st.text_input('  ',key='21351')
               st.write( f"{MAUDL}" f" ≤ VALEUR < "f"{MDL}" )
             st.text("")
             st.text("")
             VERIFDL1 = TBDL
             VERIFDL2 = BDL
             VERIFDL3 = MDL
             VERIFDL4 = MAUDL
             
             if VERIFDL1:
              ITBDL = float(TBDL)
              if((ITBDL>FMAXDL4G)or(ITBDL<FMINDL4G)):
               st.error(' Verifier la Seuil du Trés bonne DL débit')
             if VERIFDL2:
              IBDL = float(BDL)
              if((IBDL>ITBDL)or(IBDL<FMINDL4G)or(IBDL>FMAXDL4G)): 
               st.error(' Verifier la seuil du bonne DL débit')
             if VERIFDL3:
              IMDL = float(MDL)
              if((IMDL>IBDL)or(IMDL<FMINDL4G)or(IMDL>FMAXDL4G)): 
               st.error(' Verifier la Seuil du Moyenne DL débit')
             if VERIFDL4:
              IMAUDL = float(MAUDL)
              if(IMAUDL>IMDL)or(IMAUDL<FMINDL4G): 
               st.error('Verifier la Seuil du Mauvaise DL débit')
              #if((IBDL<=ITBDL)and(ITBDL<=FMAXDL4G)and(ITBDL>=FMINDL4G)and(IBDL>=FMINDL4G)and(IMDL<=IBDL)and(IMDL>=FMINDL4G)and(IMAUDL<=IMDL)and(IMAUDL>=FMINDL4G)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de DL débit sont verifier sans erreurs',subsub_txt='')


         if UP :
             display_app_header(main_txt='Débit Up Link', sub_txt='')
             st.write('')
             
             col1111111, col2222222= st.columns(2)
             MINUL4G=str(df['RLC uplink throughput'].min())
             MAXUL4G=str(df['RLC uplink throughput'].max())
             MOYEUL4G=str(round(df['RLC uplink throughput'].mean(),1))
             FMINUL4G=df['RLC uplink throughput'].min()
             FMAXUL4G=df['RLC uplink throughput'].max()
             FMOYEUL4G=df['RLC uplink throughput'].mean()
             with col1111111:
              display_app_header4(main_txt='Débit UL MIN :'+' '+MINUL4G)
                
             with col2222222:

                display_app_header4(main_txt='Débit UL MAX :'+' '+MAXUL4G)

             display_app_header4(main_txt='Débit UL MOYENNE :'+' '+MOYEUL4G)

             st.write('')
             st.write('')
             cooll7, cooll8,cooll9, cooll10 = st.columns(4) 
             with cooll7:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne UL débit:')
             with cooll8:
               TBUL = st.text_input('',key='2161')
               st.write( f"{TBUL}" f" ≤ VALEUR < "f"{MAXUL4G}" )

        
             with cooll9:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne UL débit:')
             with cooll10:
              BUL = st.text_input('',key='66546')
              st.write( f"{BUL}" f" ≤ VALEUR < "f"{TBUL}" )

             cooll3, cooll4,cooll5, cooll6 = st.columns(4) 
             with cooll3:
                display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne UL débit:')
             with cooll4:
                MUL = st.text_input(' ',key='3378')
                st.write( f"{MUL}" f" ≤ VALEUR < "f"{BUL}" ) 
             with cooll5:
               display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise UL débit:')
             with cooll6:
               MAUUL = st.text_input('  ',key='646')
               st.write( f"{MAUUL}" f" ≤ VALEUR < "f"{MUL}" )
             st.text("")
             st.text("")
             VERIFUL1 = TBUL
             VERIFUL2 = BUL
             VERIFUL3 = MUL
             VERIFUL4 = MAUUL
             
             if VERIFUL1:
              ITBUL = float(TBUL)
              if((ITBUL>FMAXUL4G)or(ITBUL<FMINUL4G)):
               st.error(' Verifier la Seuil du Trés bonne UL débit')
             if VERIFUL2:
              IBUL = float(BUL)
              if((IBUL>ITBUL)or(IBUL<FMINUL4G)or(IBUL>FMAXUL4G)): 
               st.error(' Verifier la seuil du bonne UL débit')
             if VERIFUL3:
              IMUL = float(MUL)
              if((IMUL>IBUL)or(IMUL<FMINUL4G)or(IMUL>FMAXUL4G)): 
               st.error(' Verifier la Seuil du Moyenne UL débit')
             if VERIFUL4:
              IMAUUL = float(MAUUL)
              if(IMAUUL>IMUL)or(IMAUUL<FMINUL4G): 
               st.error(' Verifier la Seuil du Mauvaise UL débit')
              #if((IBUL<=ITBUL)and(ITBUL<=FMAXUL4G)and(ITBUL>=FMINUL4G)and(IBUL>=FMINUL4G)and(IMUL<=IBUL)and(IMUL>=FMINUL4G)and(IMAUUL<=IMUL)and(IMAUUL>=FMINUL4G)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de UL débit sont verifier sans erreurs',subsub_txt='')

#***************************   2G  CONFIGURATION ****************
   
   
   
  if Choises=='2G':
     display_app_header2(main_txt='Choisir les paramètres 2G :', sub_txt='')
     calculation2G = st.multiselect('', ('RXLEV','RXQUAL'))
     if 'RXLEV' in calculation2G:
      image1 = Image.open('RXLEV.png')
      st.image(image1, caption='')
      st.write('')
      
      MIN=str(df['RXLEV (active)'].min())
      MAX=str(df['RXLEV (active)'].max())
      MOYE=str(round((df['RXLEV (active)'].mean()),1))
      FMIN=df['RXLEV (active)'].min()
      FMAX=df['RXLEV (active)'].max()
      FMOYE=df['RXLEV (active)'].mean()
      col111, col333= st.columns(2)
      with col111:
         display_app_header4(main_txt='   RXLEV MIN :'+' '+MIN )  
      with col333:
         display_app_header4(main_txt='RXLEV MAX  :'+' '+MAX)

      display_app_header4(main_txt='RXLEV MOYENNE :'+' '+MOYE)

       
      st.write('')      
      
      col7, col8,col9, col10 = st.columns(4) 
      with col7:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne couverture :')
      with col8:
       TBC = st.text_input('',key='4342')
       st.write( f"{TBC}" f" ≤ VALEUR < "f"{MAX}" )
            
      with col9:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne couverture:')
      with col10:
       BC = st.text_input('')
       st.write( f"{BC}" f" ≤ VALEUR < "f"{TBC}" )
        #with col19:
      col3, col4,col5, col6 = st.columns(4) 
      with col3:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne couverture:')
      with col4:
       MC = st.text_input(' ')
       st.write( f"{MC}" f" ≤ VALEUR < "f"{BC}" ) 
      with col5:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise couverture:')
      with col6:
         MAUC = st.text_input('  ')
         st.write( f"{MAUC}" f" ≤ VALEUR < "f"{MC}" )
      st.text("")
      st.text("")
      VERIF1 = TBC
      VERIF2 = BC
      VERIF3 = MC
      VERIF4 = MAUC
      
      if VERIF1:
         ITBC = float(TBC)
         if((ITBC>FMAX)or(ITBC<FMIN)):
            st.error(' Verifier la Seuil du Trés bonne couverture')
      if VERIF2:
         IBC = float(BC)
         if((IBC>ITBC)or(IBC<FMIN)or(IBC>FMAX)): 
            st.error(' Verifier la seuil du  bonne couverture')
      if VERIF3:
         IMC = float(MC)
         if((IMC>IBC)or(IMC<FMIN)or(IMC>FMAX)): 
            st.error(' Verifier la Seuil du  Moyenne couverture')
      if VERIF4:
         IMAUC = float(MAUC)
         if(IMAUC>IMC)or(IMAUC<FMIN): 
            st.error(' Verifier la Seuil du  Mauvaise couverture')
           #if((IBC<=ITBC)and(ITBC<=FMAX)and(ITBC>=FMIN)and(IBC>=FMIN)and(IMC<=IBC)and(IMC>=FMIN)and(IMAUC<=IMC)and(IMAUC>=FMIN)):
               #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de RXLEV sont verifier sans erreurs',subsub_txt='')
     if 'RXQUAL' in calculation2G:
        image2 = Image.open('RXQUAL.png')
        st.image(image2, caption='')
        st.write('')
        #col111, col222,col333,col444= st.columns(4)
        MINec=str(df['RXQUAL (active)'].min())
        MAXec=str(df['RXQUAL (active)'].max())
        MOYEec=str(round((df['RXQUAL (active)'].mean()),1))
        FMINec=df['RXQUAL (active)'].min()
        FMAXec=df['RXQUAL (active)'].max()
        FMOYEec=df['RXQUAL (active)'].mean()

        col1111, col3333= st.columns(2)
        with col1111:
         display_app_header4(main_txt='   RXQUAL MIN :'+' '+MINec)
          
   
        with col3333:
         display_app_header4(main_txt='RXQUAL MAX  :'+' '+MAXec)

        display_app_header4(main_txt='RXQUAL MOYENNE :'+' '+MOYEec)

        col7, col8,col9, col10 = st.columns(4) 
        with col7:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du trés bonne qualité:')
        with col8:
         TBQ = st.text_input('',key='975')
         st.write( f"{TBQ}" f" ≤ VALEUR < "f"{MAXec}" )

        
        with col9:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du bonne qualité:')
        with col10:
         BQ = st.text_input('',key='3453')
         st.write( f"{BQ}" f" ≤ VALEUR < "f"{TBQ}" )

        col3, col4,col5, col6 = st.columns(4) 
        with col3:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du moyenne qualité:')
        with col4:
         MQ = st.text_input(' ',key='9334')
         st.write( f"{MQ}" f" ≤ VALEUR < "f"{BQ}" ) 
        with col5:
         display_app_header3(main_txt='', sub_txt='',subsub_txt='Seuil du mauvaise qualité:')
        with col6:
         MAUQ = st.text_input('  ',key='934')
         st.write( f"{MAUQ}" f" ≤ VALEUR < "f"{MQ}" )
        st.text("")
        st.text("")
        VERIFsc1 = TBQ
        VERIFsc2 = BQ
        VERIFsc3 = MQ
        VERIFsc4 = MAUQ
      
        if VERIFsc1:
         ITBQ = float(TBQ)
         if((ITBQ>FMAXec)or(ITBQ<FMINec)):
            st.error(' Verifier la Seuil du Trés bonne couverture')
        if VERIFsc2:
         IBQ = float(BQ)
         if((IBQ>ITBQ)or(IBQ<FMINec)or(IBQ>FMAXec)): 
            st.error(' Verifier la seuil du  bonne couverture')
        if VERIFsc3:
         IMQ = float(MQ)
         if((IMQ>IBQ)or(IMQ<FMINec)or(IMQ>FMAXec)): 
            st.error(' Verifier la Seuil du  Moyenne couverture')
        if VERIFsc4:
         IMAUQ = float(MAUQ)
         if(IMAUQ>IMQ)or(IMAUQ<FMINec): 
            st.error(' Verifier la Seuil du  Mauvaise couverture')
         #if((IBQ<=ITBQ)and(ITBQ<=FMAXec)and(ITBQ>=FMINec)and(IBQ>=FMINec)and(IMQ<=IBQ)and(IMQ>=FMINec)and(IMAUQ<=IMQ)and(IMAUQ>=FMINec)):
            #display_app_header6(main_txt='', sub_txt='✅ Tout les seuils de Ec/N0 sont verifier sans erreurs',subsub_txt='')

#***************** bouton calculer ********************
  st.text("")
  st.text("")
  calculate = st.button('Calculer')
  if calculate:
       #latest_iteration = st.empty()
       #bar = st.progress(0)
       #for i in range(100):
            #latest_iteration.text(f'Loading {i+1}')
            #bar.progress(i + 1)
            #time.sleep(0.01)


        
    #***************** 2G AFFICHAGE ********************
       if Choises=='2G':
            if 'RXLEV' in calculation2G:
              if((IBC<=ITBC)and(ITBC<=FMAX)and(ITBC>=FMIN)and(IBC>=FMIN)and(IMC<=IBC)and(IMC>=FMIN)and(IMAUC<=IMC)and(IMAUC>=FMIN)):
               st.image(image1, caption='')
               st.write('')
               
               STBC=df.loc[(df['RXLEV (active)']<0)]
               STBC.reset_index(inplace=True)
               time=(STBC.iloc[:,1:2])
               quarter1=0
               quarter2=int(len(time)/7)
               quarter3=int(len(time)*2/7)
               quarter4=int(len(time)*3/7)
               quarter5=int(len(time)*4/7)
               quarter6=int(len(time)*5/7)
               quarter7=int(len(time)*6/7)
               quarter8=int(len(time)-1)															
               fig5 = px.line(STBC, x='Time', y="RXLEV (active)")
               fig5.update_layout(

               title={
                    'text': "Courbe de RXLEV 📶",
                  'y':0.95,
                   'x':0.5,
                   'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  title_font_size=30,
                  legend_title="Légende :",
                  legend_title_font_color="#4C7497",
    
                   font=dict(
                     family="Neo Sans Std ",
                  size=16,
                       color="#4C7497",
       
        
        
                        )
                   )
               fig5.update_xaxes(
                  tickangle = 0,
               tickvals=[time.Time[quarter1],time.Time[quarter2],time.Time[quarter3],time.Time[quarter4], time.Time[quarter5], ( time.Time[quarter6]),(time.Time[quarter7]),time.Time[quarter8]],
                  ticktext=[(str(time.Time[quarter1])[0:8]),(str(time.Time[quarter2])[0:8]),(str(time.Time[quarter3])[0:8]),(str(time.Time[quarter4])[0:8]),(str(time.Time[quarter5])[0:8]),(str(time.Time[quarter6])[0:8]),(str(time.Time[quarter7])[0:8]),(str(time.Time[quarter8])[0:8])],
                   title_font = {"size": 20},
                   )
               #st.image(image2, caption='')
               st.plotly_chart(fig5, use_container_width=True)
               #display_app_header(main_txt='RSCP', sub_txt='')
               
               fig= px.histogram(df, x=df['RXLEV (active)'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

               fig.update_layout(

                   title={
                     'text': "Répartitions de RXLEV 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))
               st.plotly_chart(fig, use_container_width=True)

               

               ITBC = float(TBC)
               IBC = float(BC)
               IMC = float(MC)
               IMAUC = float(MAUC)
               VTBC=df.loc[(df['RXLEV (active)']>=ITBC)]
               VBC=df.loc[(df['RXLEV (active)']<=ITBC)&(df['RXLEV (active)']>=IBC)]
               VMC=df.loc[(df['RXLEV (active)']<=IBC)&(df['RXLEV (active)']>=IMC)]
               VMAUC=df.loc[(df['RXLEV (active)']<=IMC)&(df['RXLEV (active)']>=IMAUC)]
               (echantillant)=len(VMAUC)+len(VBC)+len(VMC)+len(VTBC)
               pourc_MAUC=(len(VMAUC)/echantillant)*100
               pourc_MC=(len(VMC)/echantillant)*100
               pourc_BC=(len(VBC)/echantillant)*100
               pourc_TBC=(len(VTBC)/echantillant)*100
                  
               import plotly.graph_objects as go
               labels = ['Trés bonne Couverture','bonne Couverture','Moyenne Couverture','Mauvaise Couverture']
               colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
               values = [pourc_TBC, pourc_BC, pourc_MC, pourc_MAUC]

               fig2 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2))
                               )])
               
               fig2.update_layout(
                   

                   title={
                      'text': "Couverture 📶",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
                   
           
           
                    )
               )
               fig2.update_traces (pull=[0,0,0,0.1],textposition='inside')
               fig2.update_coloraxes(colorbar_bordercolor="#555",colorbar_borderwidth=2,colorbar_bgcolor="rgba(45,44,65,45)")
               
               st.plotly_chart(fig2, use_container_width=True)

              else:
                 st.image(image1, caption='')
                 st.write('')
                 st.error('Verifier les erreurs des seuils de RXLEV') 
            if 'RXQUAL' in calculation2G:
             if((IBQ<=ITBQ)and(ITBQ<=FMAXec)and(ITBQ>=FMINec)and(IBQ>=FMINec)and(IMQ<=IBQ)and(IMQ>=FMINec)and(IMAUQ<=IMQ)and(IMAUQ>=FMINec)):
              st.image(image2, caption='')
              st.write('')
              ETBC=df.loc[(df['RXQUAL (active)']<0)]
              ETBC.reset_index(inplace=True)
              timesc=(ETBC.iloc[:,1:2])
              quartersc1=0
              quartersc2=int(len(timesc)/7)
              quartersc3=int(len(timesc)*2/7)
              quartersc4=int(len(timesc)*3/7)
              quartersc5=int(len(timesc)*4/7)
              quartersc6=int(len(timesc)*5/7)
              quartersc7=int(len(timesc)*6/7)
              quartersc8=int(len(timesc)-1)														
              fig6 = px.line(ETBC, x='Time', y="RXQUAL (active)")
              fig6.update_layout(

              title={
                    'text': "Courbe de RXQUAL 📶",
                  'y':0.95,
                   'x':0.5,
                   'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  title_font_size=30,
                  legend_title="Légende :",
                  legend_title_font_color="#4C7497",
    
                   font=dict(
                     family="Neo Sans Std ",
                  size=16,
                       color="#4C7497",
       
        
        
                        )
                   )
              fig6.update_xaxes(
              tickangle = 0,
              tickvals=[timesc.Time[quartersc1],timesc.Time[quartersc2],timesc.Time[quartersc3],timesc.Time[quartersc4], timesc.Time[quartersc5], ( timesc.Time[quartersc6]),(timesc.Time[quartersc7]),timesc.Time[quartersc8]],
              ticktext=[(str(timesc.Time[quartersc1])[0:8]),(str(timesc.Time[quartersc2])[0:8]),(str(timesc.Time[quartersc3])[0:8]),(str(timesc.Time[quartersc4])[0:8]),(str(timesc.Time[quartersc5])[0:8]),(str(timesc.Time[quartersc6])[0:8]),(str(timesc.Time[quartersc7])[0:8]),(str(timesc.Time[quartersc8])[0:8])],
                   title_font = {"size": 20},
                   )
               #st.image(image2, caption='')
              st.plotly_chart(fig6, use_container_width=True)
              
              fig3= px.histogram(df, x=df['RXQUAL (active)'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

              fig3.update_layout(

                   title={
                     'text': "Répartitions de RXQUAL 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))
              st.plotly_chart(fig3, use_container_width=True)

               

              ITBQ = float(TBQ)
              IBQ = float(BQ)
              IMQ = float(MQ)
              IMAUQ = float(MAUQ)
              VTBQ=df.loc[(df['RXQUAL (active)']>=ITBQ)]
              VBQ=df.loc[(df['RXQUAL (active)']<=ITBQ)&(df['RXQUAL (active)']>=IBQ)]
              VMQ=df.loc[(df['RXQUAL (active)']<=IBQ)&(df['RXQUAL (active)']>=IMQ)]
              VMAUQ=df.loc[(df['RXQUAL (active)']<=IMQ)&(df['RXQUAL (active)']>=IMAUQ)]
              (echantillantQ)=len(VMAUQ)+len(VBQ)+len(VMQ)+len(VTBQ)
              pourc_MAUQ=(len(VMAUQ)/echantillantQ)*100
              pourc_MQ=(len(VMQ)/echantillantQ)*100
              pourc_BQ=(len(VBQ)/echantillantQ)*100
              pourc_TBQ=(len(VTBQ)/echantillantQ)*100
                  
              import plotly.graph_objects as go
              labelsQ = ['Trés bonne Qualité','bonne Qualité','Moyenne Qualité','Mauvaise Qualité']
              colorsQ = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
              valuesQ = [pourc_TBQ, pourc_BQ, pourc_MQ, pourc_MAUQ]
              fig4 = go.Figure(data=[go.Pie(labels=labelsQ, values=valuesQ,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colorsQ, line=dict(color='#FFFFFF', width=2))
                               )])
               
              fig4.update_layout(
                   

                   title={
                      'text': "Qualité 📡",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
                   
           
           
                    )
               )
              fig4.update_traces (pull=[0,0,0,0.05],textposition='inside')
              fig4.update_coloraxes(colorbar_bordercolor="#555",colorbar_borderwidth=2,colorbar_bgcolor="rgba(45,44,65,45)")

              st.plotly_chart(fig4, use_container_width=True)
             else:
              st.image(image2, caption='')
              st.write('')                 
              st.error('Verifier les erreurs des seuils de RXQUAL')    
    #***************** 3G AFFICHAGE ********************
       if Choises=='3G':
           

         #***************** RSCP AFFICHAGE ********************

   

           if 'RSCP' in calculation3G:
              if((IBC<=ITBC)and(ITBC<=FMAX)and(ITBC>=FMIN)and(IBC>=FMIN)and(IMC<=IBC)and(IMC>=FMIN)and(IMAUC<=IMC)):
               image1 = Image.open('RSCP.png')
               st.image(image1, caption='')
               st.write('')
               STBC=df.loc[(df['RSCP (active)']<0)]
               STBC.reset_index(inplace=True)
               time=(STBC.iloc[:,1:2])
               quarter1=0
               quarter2=int(len(time)/7)
               quarter3=int(len(time)*2/7)
               quarter4=int(len(time)*3/7)
               quarter5=int(len(time)*4/7)
               quarter6=int(len(time)*5/7)
               quarter7=int(len(time)*6/7)
               quarter8=int(len(time)-1)
               #STBC=df.loc[(df['RSCP (active)']<0)]
               fig5 = px.line(STBC, x='Time', y="RSCP (active)")
               fig5.update_layout(

               title={
                    'text': "Courbe de RSCP 📶",
                  'y':0.95,
                   'x':0.5,
                   'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  title_font_size=30,
                  legend_title="Légende :",
                  legend_title_font_color="#4C7497",
    
                   font=dict(
                     family="Neo Sans Std ",
                  size=16,
                       color="#4C7497",
       
        
        
                        )
                   )
               fig5.update_xaxes(
                tickangle = 0,
                tickvals=[time.Time[quarter1],time.Time[quarter2],time.Time[quarter3],time.Time[quarter4], time.Time[quarter5], ( time.Time[quarter6]),(time.Time[quarter7]),time.Time[quarter8]],
                ticktext=[(str(time.Time[quarter1])[0:8]),(str(time.Time[quarter2])[0:8]),(str(time.Time[quarter3])[0:8]),(str(time.Time[quarter4])[0:8]),(str(time.Time[quarter5])[0:8]),(str(time.Time[quarter6])[0:8]),(str(time.Time[quarter7])[0:8]),(str(time.Time[quarter8])[0:8])],
                   title_font = {"size": 20},
                   )
               
               #st.image(image2, caption='')
               st.plotly_chart(fig5, use_container_width=True)
               #display_app_header(main_txt='RSCP', sub_txt='')
               
               fig= px.histogram(df, x=df['RSCP (active)'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

               fig.update_layout(

                   title={
                     'text': "Répartitions de RSCP 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))
               st.plotly_chart(fig, use_container_width=True)

               

               ITBC = float(TBC)
               IBC = float(BC)
               IMC = float(MC)
               IMAUC = float(MAUC)
               VTBC=df.loc[(df['RSCP (active)']>=ITBC)]
               VBC=df.loc[(df['RSCP (active)']<=ITBC)&(df['RSCP (active)']>=IBC)]
               VMC=df.loc[(df['RSCP (active)']<=IBC)&(df['RSCP (active)']>=IMC)]
               VMAUC=df.loc[(df['RSCP (active)']<=IMC)&(df['RSCP (active)']>=IMAUC)]
               (echantillant)=len(VMAUC)+len(VBC)+len(VMC)+len(VTBC)
               pourc_MAUC=(len(VMAUC)/echantillant)*100
               pourc_MC=(len(VMC)/echantillant)*100
               pourc_BC=(len(VBC)/echantillant)*100
               pourc_TBC=(len(VTBC)/echantillant)*100
                  
               import plotly.graph_objects as go
               labels = ['Trés bonne Couverture','bonne Couverture','Moyenne Couverture','Mauvaise Couverture']
               colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
               values = [pourc_TBC, pourc_BC, pourc_MC, pourc_MAUC]

               fig2 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2))
                               )])
               
               fig2.update_layout(
                   

                   title={
                      'text': "Diagramme circulaire de RSCP 📶",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
                   
           
           
                    )
               )
               fig2.update_traces (pull=[0,0,0,0.1],textposition='inside')
               fig2.update_coloraxes(colorbar_bordercolor="#555",colorbar_borderwidth=2,colorbar_bgcolor="rgba(45,44,65,45)")
               
               st.plotly_chart(fig2, use_container_width=True)
               
              else:
               st.image(image1, caption='')
               st.write('')
               st.error('Verifier les erreurs des seuils de RSCP') 
         #***************** Ec/N0 AFFICHAGE ********************

           if 'EC/NO' in calculation3G:
            
            if((IBQ<=ITBQ)and(ITBQ<=FMAXec)and(ITBQ>=FMINec)and(IBQ>=FMINec)and(IMQ<=IBQ)and(IMQ>=FMINec)and(IMAUQ<=IMQ)):
             image2 = Image.open('ECNO.png')
             st.image(image2, caption='')
             st.write('')
             ETBC=df.loc[(df['Ec/N0 (active)']<0)]
             ETBC.reset_index(inplace=True)
             timesc=(ETBC.iloc[:,1:2])
             quartersc1=0
             quartersc2=int(len(timesc)/7)
             quartersc3=int(len(timesc)*2/7)
             quartersc4=int(len(timesc)*3/7)
             quartersc5=int(len(timesc)*4/7)
             quartersc6=int(len(timesc)*5/7)
             quartersc7=int(len(timesc)*6/7)
             quartersc8=int(len(timesc)-1)
             
             fig6 = px.line(ETBC, x='Time', y="Ec/N0 (active)")
             fig6.update_layout(

             title={
                    'text': "Courbe de EcNO 📶",
                  'y':0.95,
                   'x':0.5,
                   'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  title_font_size=30,
                  legend_title="Légende :",
                  legend_title_font_color="#4C7497",
    
                   font=dict(
                     family="Neo Sans Std ",
                  size=16,
                       color="#4C7497",
       
        
        
                        )
                   )
             fig6.update_xaxes(
              tickangle = 0,
              tickvals=[timesc.Time[quartersc1],timesc.Time[quartersc2],timesc.Time[quartersc3],timesc.Time[quartersc4], timesc.Time[quartersc5], ( timesc.Time[quartersc6]),(timesc.Time[quartersc7]),timesc.Time[quartersc8]],
              ticktext=[(str(timesc.Time[quartersc1])[0:8]),(str(timesc.Time[quartersc2])[0:8]),(str(timesc.Time[quartersc3])[0:8]),(str(timesc.Time[quartersc4])[0:8]),(str(timesc.Time[quartersc5])[0:8]),(str(timesc.Time[quartersc6])[0:8]),(str(timesc.Time[quartersc7])[0:8]),(str(timesc.Time[quartersc8])[0:8])],
                   title_font = {"size": 20},
                   )
               
             #st.image(image2, caption='')
             st.plotly_chart(fig6, use_container_width=True)             

             fig3= px.histogram(df, x=df['Ec/N0 (active)'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

             fig3.update_layout(

                   title={
                     'text': "Répartitions de Ec/No 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
                     
           
                    ))
             st.plotly_chart(fig3, use_container_width=True)

               

             ITBQ = float(TBQ)
             IBQ = float(BQ)
             IMQ = float(MQ)
             IMAUQ = float(MAUQ)
             VTBQ=df.loc[(df['Ec/N0 (active)']>=ITBQ)]
             VBQ=df.loc[(df['Ec/N0 (active)']<=ITBQ)&(df['Ec/N0 (active)']>=IBQ)]
             VMQ=df.loc[(df['Ec/N0 (active)']<=IBQ)&(df['Ec/N0 (active)']>=IMQ)]
             VMAUQ=df.loc[(df['Ec/N0 (active)']<=IMQ)&(df['Ec/N0 (active)']>=IMAUQ)]
             (echantillantQ)=len(VMAUQ)+len(VBQ)+len(VMQ)+len(VTBQ)
             pourc_MAUQ=(len(VMAUQ)/echantillantQ)*100
             pourc_MQ=(len(VMQ)/echantillantQ)*100
             pourc_BQ=(len(VBQ)/echantillantQ)*100
             pourc_TBQ=(len(VTBQ)/echantillantQ)*100
                  
             import plotly.graph_objects as go
             labelsQ = ['Trés bonne Qualité','bonne Qualité','Moyenne Qualité','Mauvaise Qualité']
             colorsQ = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
             valuesQ = [pourc_TBQ, pourc_BQ, pourc_MQ, pourc_MAUQ]
             fig4 = go.Figure(data=[go.Pie(labels=labelsQ, values=valuesQ,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colorsQ, line=dict(color='#FFFFFF', width=2))
                               )])
               
             fig4.update_layout(
                   

                   title={
                      'text': "Qualité 📡",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
                   
           
           
                    )
               )
             fig4.update_traces (pull=[0,0,0,0.05],textposition='inside')
             fig4.update_coloraxes(colorbar_bordercolor="#555",colorbar_borderwidth=2,colorbar_bgcolor="rgba(45,44,65,45)")

             st.plotly_chart(fig4, use_container_width=True)
            else:
             image2 = Image.open('ECNO.png')
             st.image(image2, caption='')                 
             st.error('Verifier les erreurs des seuils de Ec/N0')        
 
         #***************** Debit 3G ********************
           if 'Débit3G' in calculation3G:
             image3 = Image.open('DEBIT.png')
             st.image(image3, caption='')
             st.write('')
             if DL :

              if((IBDL<=ITBDL)and(ITBDL<=FMAXDL3G)and(ITBDL>=FMINDL3G)and(IBDL>=FMINDL3G)and(IMDL<=IBDL)and(IMDL>=FMINDL3G)and(IMAUDL<=IMDL)):


               display_app_header(main_txt='Débit Down Link', sub_txt='')
                 
               st.write('')
               DLTBC=df.loc[(df['Application throughput downlink']>0)]
               fig7 = px.line(DLTBC, x='Time', y="Application throughput downlink")
               DLTBC.reset_index(inplace=True)
               timescDL=(DLTBC.iloc[:,1:2])
               quarterscDL1=0
               quarterscDL2=int(len(timescDL)/7)
               quarterscDL3=int(len(timescDL)*2/7)
               quarterscDL4=int(len(timescDL)*3/7)
               quarterscDL5=int(len(timescDL)*4/7)
               quarterscDL6=int(len(timescDL)*5/7)
               quarterscDL7=int(len(timescDL)*6/7)
               quarterscDL8=int(len(timescDL)-1)															
               fig7.update_layout(

               title={
                    'text': "Courbe de DL Débit 📶",
                  'y':0.95,
                   'x':0.5,
                   'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  title_font_size=30,
                  legend_title="Légende :",
                  legend_title_font_color="#4C7497",
    
                   font=dict(
                     family="Neo Sans Std ",
                  size=16,
                       color="#4C7497",
       
        
        
                        )
                   )
               fig7.update_xaxes(
               tickangle = 0,
               tickvals=[timescDL.Time[quarterscDL1],timescDL.Time[quarterscDL2],timescDL.Time[quarterscDL3],timescDL.Time[quarterscDL4], timescDL.Time[quarterscDL5], ( timescDL.Time[quarterscDL6]),(timescDL.Time[quarterscDL7]),timescDL.Time[quarterscDL8]],
               ticktext=[(str(timescDL.Time[quarterscDL1])[0:8]),(str(timescDL.Time[quarterscDL2])[0:8]),(str(timescDL.Time[quarterscDL3])[0:8]),(str(timescDL.Time[quarterscDL4])[0:8]),(str(timescDL.Time[quarterscDL5])[0:8]),(str(timescDL.Time[quarterscDL6])[0:8]),(str(timescDL.Time[quarterscDL7])[0:8]),(str(timescDL.Time[quarterscDL8])[0:8])],
                   title_font = {"size": 20},
                   ) 
               #display_app_header(main_txt='RSRP', sub_txt='')
               #st.image(image2, caption='')
               fig8= px.histogram(df, x=df['Application throughput downlink'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

               fig8.update_layout(

                   title={
                     'text': "Répartitions de Débit DownLink 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))

               st.plotly_chart(fig7, use_container_width=True)
               st.plotly_chart(fig8, use_container_width=True)

               

               ITBC4G = float(TBDL)
               IBC4G = float(BDL)
               IMC4G = float(MDL)
               IMAUC4G = float(MAUDL)
               VTBC4G=df.loc[(df['Application throughput downlink']>=ITBC4G)]
               VBC4G=df.loc[(df['Application throughput downlink']<=ITBC4G)&(df['Application throughput downlink']>=IBC4G)]
               VMC4G=df.loc[(df['Application throughput downlink']<=IBC4G)&(df['Application throughput downlink']>=IMC4G)]
               VMAUC4G=df.loc[(df['Application throughput downlink']<=IMC4G)&(df['Application throughput downlink']>=IMAUC4G)]
               (echantillant)=len(VMAUC4G)+len(VBC4G)+len(VMC4G)+len(VTBC4G)
               pourc_MAUC4G=(len(VMAUC4G)/echantillant)*100
               pourc_MC4G=(len(VMC4G)/echantillant)*100
               pourc_BC4G=(len(VBC4G)/echantillant)*100
               pourc_TBC4G=(len(VTBC4G)/echantillant)*100
                  
               import plotly.graph_objects as go
               labels = ['Trés bonne DL Debit','bonne DL Debit','Moyenne DL Debit','Mauvaise DL Debit']
               colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
               values = [pourc_TBC4G, pourc_BC4G, pourc_MC4G, pourc_MAUC4G]

               fig9 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#ffffff', width=2))
                               )])
               fig9.update_traces(textposition='inside', pull=[0,0,0,0.1] )
               fig9.update_layout(

                   title={
                      'text': "DL Debit 📶",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
          
           
           
                    )
               )

               st.plotly_chart(fig9, use_container_width=True)
              else :
               display_app_header(main_txt='Débit Down Link', sub_txt='')
               st.write('')                 
               st.error('Verifier les erreurs des seuils de DL Debit')      
             if UP :

              if((IBUL<=ITBUL)and(ITBUL<=FMAXUL3G)and(ITBUL>=FMINUL3G)and(IBUL>=FMINUL3G)and(IMUL<=IBUL)and(IMUL>=FMINUL3G)and(IMAUUL<=IMUL)):


               display_app_header(main_txt='Débit Up Link', sub_txt='')
               st.write('')
               ULTBC=df.loc[(df['Application throughput uplink']>0)]
               fig10 = px.line(ULTBC, x='Time', y="Application throughput uplink")
               ULTBC.reset_index(inplace=True)
               timescUL=(ULTBC.iloc[:,1:2])
               quarterscUL1=0
               quarterscUL2=int(len(timescUL)/7)
               quarterscUL3=int(len(timescUL)*2/7)
               quarterscUL4=int(len(timescUL)*3/7)
               quarterscUL5=int(len(timescUL)*4/7)
               quarterscUL6=int(len(timescUL)*5/7)
               quarterscUL7=int(len(timescUL)*6/7)
               quarterscUL8=int(len(timescUL)-1)																		
               fig10.update_layout(

               title={
                    'text': "Courbe de UL Débit 📶",
                  'y':0.95,
                   'x':0.5,
                   'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  title_font_size=30,
                  legend_title="Légende :",
                  legend_title_font_color="#4C7497",
    
                   font=dict(
                     family="Neo Sans Std ",
                  size=16,
                       color="#000000",
       
        
        
                        )
                   )
               fig10.update_xaxes(
               tickangle = 0,
               tickvals=[timescUL.Time[quarterscUL1],timescUL.Time[quarterscUL2],timescUL.Time[quarterscUL3],timescUL.Time[quarterscUL4], timescUL.Time[quarterscUL5], ( timescUL.Time[quarterscUL6]),(timescUL.Time[quarterscUL7]),timescUL.Time[quarterscUL8]],
               ticktext=[(str(timescUL.Time[quarterscUL1])[0:8]),(str(timescUL.Time[quarterscUL2])[0:8]),(str(timescUL.Time[quarterscUL3])[0:8]),(str(timescUL.Time[quarterscUL4])[0:8]),(str(timescUL.Time[quarterscUL5])[0:8]),(str(timescUL.Time[quarterscUL6])[0:8]),(str(timescUL.Time[quarterscUL7])[0:8]),(str(timescUL.Time[quarterscUL8])[0:8])],
                   title_font = {"size": 20},
                   ) 
               #display_app_header(main_txt='RSRP', sub_txt='')
               #st.image(image2, caption='')
               fig11= px.histogram(df, x=df['Application throughput uplink'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

               fig11.update_layout(

                   title={
                     'text': "Répartitions de Débit UpLink 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))
               st.plotly_chart(fig10, use_container_width=True)
               st.plotly_chart(fig11, use_container_width=True)

               

               ITBU4G = float(TBUL)
               IBU4G = float(BUL)
               IMU4G = float(MUL)
               IMAUU4G = float(MAUUL)
               VTBU4G=df.loc[(df['Application throughput uplink']>=ITBU4G)]
               VBU4G=df.loc[(df['Application throughput uplink']<=ITBU4G)&(df['Application throughput uplink']>=IBU4G)]
               VMU4G=df.loc[(df['Application throughput uplink']<=IBU4G)&(df['Application throughput uplink']>=IMU4G)]
               VMAUU4G=df.loc[(df['Application throughput uplink']<=IMU4G)&(df['Application throughput uplink']>=IMAUU4G)]
               (echantillantUL)=len(VMAUU4G)+len(VBU4G)+len(VMU4G)+len(VTBU4G)
               pourc_MAUU4G=(len(VMAUU4G)/echantillantUL)*100
               pourc_MU4G=(len(VMU4G)/echantillantUL)*100
               pourc_BU4G=(len(VBU4G)/echantillantUL)*100
               pourc_TBU4G=(len(VTBU4G)/echantillantUL)*100
                  
               import plotly.graph_objects as go
               labels = ['Trés bonne UL Debit','bonne UL Debit','Moyenne UL Debit','Mauvaise UL Debit']
               colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
               values = [pourc_TBU4G, pourc_BU4G, pourc_MU4G, pourc_MAUU4G]

               fig12 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#ffffff', width=2))
                               )])
               fig12.update_traces(textposition='inside', pull=[0,0,0,0.1] )
               fig12.update_layout(

                   title={
                      'text': "UL Debit 📶",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
          
           
           
                    )
               )
               st.plotly_chart(fig12, use_container_width=True)
              else :
               display_app_header(main_txt='Débit Up Link', sub_txt='')
               st.write('')                 
               st.error('Verifier les erreurs des seuils de UL Debit')

         #***************** Ec/N0 /// RSCP ********************
           if 'RSCP' in calculation3G: 
            if 'EC/NO' in calculation3G:
             display_app_header4(main_txt='Points avec bonne couverture et mauvaise qualité :')
             st.write('')
             BC_MQ=df.loc[((df['RSCP (active)']>=IBC)&(df['Ec/N0 (active)']<=IMAUQ))]
             st.write(BC_MQ)									       
    #***************** 4G AFFICHAGE ********************
      
      
       if Choises=='4G':



        #***************** RSRP AFFICHAGE ********************




           if 'RSRP' in calculation4G:
              if((IBC4G<=ITBC4G)and(ITBC4G<=FMAX4G)and(ITBC4G>=FMIN4G)and(IBC4G>=FMIN4G)and(IMC4G<=IBC4G)and(IMC4G>=FMIN4G)and(IMAUC4G<=IMC4G)and(IMAUC4G>=FMIN4G)):

               image1 = Image.open('RSRP.png')
               st.image(image1, caption='')
               st.write('')

               STBC=df.loc[(df['RSRP (pcell)']<0)]
               STBC.reset_index(inplace=True)
               time=(STBC.iloc[:,1:2])
               quarter1=0
               quarter2=int(len(time)/7)
               quarter3=int(len(time)*2/7)
               quarter4=int(len(time)*3/7)
               quarter5=int(len(time)*4/7)
               quarter6=int(len(time)*5/7)
               quarter7=int(len(time)*6/7)
               quarter8=int(len(time)-1)															
               fig = px.line(STBC, x='Time', y="RSRP (pcell)")
               fig.update_layout(
         
               title={
                    'text': "Courbe de RSRP 📶",
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    title_font_color="#3176BC",
                    title_font_size=30,
                    legend_title="Légende :",
                    legend_title_font_color="#4C7497",
    
                    font=dict(
                        family="Neo Sans Std ",
                       size=16,
                        color="#4C7497",
       
        
        
                         )
                    )
               fig.update_xaxes(
                tickangle = 0,
                tickvals=[time.Time[quarter1],time.Time[quarter2],time.Time[quarter3],time.Time[quarter4], time.Time[quarter5], ( time.Time[quarter6]),(time.Time[quarter7]),time.Time[quarter8]],
                ticktext=[(str(time.Time[quarter1])[0:8]),(str(time.Time[quarter2])[0:8]),(str(time.Time[quarter3])[0:8]),(str(time.Time[quarter4])[0:8]),(str(time.Time[quarter5])[0:8]),(str(time.Time[quarter6])[0:8]),(str(time.Time[quarter7])[0:8]),(str(time.Time[quarter8])[0:8])],
                    title_font = {"size": 20},
                    )
               st.plotly_chart(fig, use_container_width=True)

               fig1= px.histogram(df, x=df['RSRP (pcell)'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

               fig1.update_layout(

                   title={
                     'text': "Répartitions de RSRP 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))
               st.plotly_chart(fig1, use_container_width=True)

               

               ITBC4G = float(TBC4G)
               IBC4G = float(BC4G)
               IMC4G = float(MC4G)
               IMAUC4G = float(MAUC4G)
               VTBC4G=df.loc[(df['RSRP (pcell)']>=ITBC4G)]
               VBC4G=df.loc[(df['RSRP (pcell)']<=ITBC4G)&(df['RSRP (pcell)']>=IBC4G)]
               VMC4G=df.loc[(df['RSRP (pcell)']<=IBC4G)&(df['RSRP (pcell)']>=IMC4G)]
               VMAUC4G=df.loc[(df['RSRP (pcell)']<=IMC4G)&(df['RSRP (pcell)']>=IMAUC4G)]
               (echantillant)=len(VMAUC4G)+len(VBC4G)+len(VMC4G)+len(VTBC4G)
               pourc_MAUC4G=(len(VMAUC4G)/echantillant)*100
               pourc_MC4G=(len(VMC4G)/echantillant)*100
               pourc_BC4G=(len(VBC4G)/echantillant)*100
               pourc_TBC4G=(len(VTBC4G)/echantillant)*100
                  
               import plotly.graph_objects as go
               labels = ['Trés bonne Couverture','bonne Couverture','Moyenne Couverture','Mauvaise Couverture']
               colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
               values = [pourc_TBC4G, pourc_BC4G, pourc_MC4G, pourc_MAUC4G]

               fig2 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#ffffff', width=2))
                               )])
               fig2.update_traces(textposition='inside', pull=[0,0,0,0.1] )
               fig2.update_layout(

                   title={
                      'text': "Couverture 📶",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
          
           
           
                    )
               )
               st.plotly_chart(fig2, use_container_width=True)
              else :
               st.image(image1, caption='')
               st.write('')                 
               st.error('Verifier les erreurs des seuils de RSRP')

        #***************** RSRQ AFFICHAGE ********************

           if 'RSRQ' in calculation4G :
              if((IBCsc4G<=ITBCsc4G)and(ITBCsc4G<=FMAXsc4G)and(ITBCsc4G>=FMINsc4G)and(IBCsc4G>=FMINsc4G)and(IMCsc4G<=IBCsc4G)and(IMCsc4G>=FMINsc4G)and(IMAUCsc4G<=IMCsc4G)and(IMAUCsc4G>=FMINsc4G)):
               
               
               image2 = Image.open('RSRQ.png')
               st.image(image2, caption='')
               st.write('')    
               ETBC=df.loc[(df['RSRQ (pcell)']<0)]
               ETBC.reset_index(inplace=True)
               timesc=(ETBC.iloc[:,1:2])
               quartersc1=0
               quartersc2=int(len(timesc)/7)
               quartersc3=int(len(timesc)*2/7)
               quartersc4=int(len(timesc)*3/7)
               quartersc5=int(len(timesc)*4/7)
               quartersc6=int(len(timesc)*5/7)
               quartersc7=int(len(timesc)*6/7)
               quartersc8=int(len(timesc)-1)
             															
               fig5 = px.line(ETBC, x='Time', y="RSRQ (pcell)")
               fig5.update_layout(
         
               title={
                    'text': "Courbe de RSRQ 📶",
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                    title_font_color="#3176BC",
                    title_font_size=30,
                    legend_title="Légende :",
                    legend_title_font_color="#4C7497",
    
                    font=dict(
                        family="Neo Sans Std ",
                       size=16,
                        color="#4C7497",
       
        
        
                         )
                    )
               fig5.update_xaxes(
               tickangle = 0,
               tickvals=[timesc.Time[quartersc1],timesc.Time[quartersc2],timesc.Time[quartersc3],timesc.Time[quartersc4], timesc.Time[quartersc5], ( timesc.Time[quartersc6]),(timesc.Time[quartersc7]),timesc.Time[quartersc8]],
               ticktext=[(str(timesc.Time[quartersc1])[0:8]),(str(timesc.Time[quartersc2])[0:8]),(str(timesc.Time[quartersc3])[0:8]),(str(timesc.Time[quartersc4])[0:8]),(str(timesc.Time[quartersc5])[0:8]),(str(timesc.Time[quartersc6])[0:8]),(str(timesc.Time[quartersc7])[0:8]),(str(timesc.Time[quartersc8])[0:8])],
                    title_font = {"size": 20},
                    )
               st.plotly_chart(fig5, use_container_width=True)

               fig3= px.histogram(df, x=df['RSRQ (pcell)'],
                      title='Histogram of bills 📊📡',
                      color_discrete_sequence=['#3176BC'])

               fig3.update_layout(

                   title={
                     'text': "Répartitions de RSRQ 📊",
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
                  title_font_color="#3176BC",
                  legend_title_font_color="#4C7497",
                  title_font_size=30,
      
                  font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#4C7497",
          
           
           
                    ))
               st.plotly_chart(fig3, use_container_width=True)

               

               ITBCsc4G = float(TBCsc4G)
               IBCsc4G = float(BCsc4G)
               IMCsc4G = float(MCsc4G)
               IMAUCsc4G = float(MAUCsc4G)
               VTBCsc4G=df.loc[(df['RSRQ (pcell)']>=ITBCsc4G)]
               VBCsc4G=df.loc[(df['RSRQ (pcell)']<=ITBCsc4G)&(df['RSRQ (pcell)']>=IBCsc4G)]
               VMCsc4G=df.loc[(df['RSRQ (pcell)']<=IBCsc4G)&(df['RSRQ (pcell)']>=IMCsc4G)]
               VMAUCsc4G=df.loc[(df['RSRQ (pcell)']<=IMCsc4G)&(df['RSRQ (pcell)']>=IMAUCsc4G)]
               (echantillantQ)=len(VMAUCsc4G)+len(VBCsc4G)+len(VMCsc4G)+len(VTBCsc4G)
               pourc_MAUCsc4G=(len(VMAUCsc4G)/echantillantQ)*100
               pourc_MCsc4G=(len(VMCsc4G)/echantillantQ)*100
               pourc_BCsc4G=(len(VBCsc4G)/echantillantQ)*100
               pourc_TBCsc4G=(len(VTBCsc4G)/echantillantQ)*100
                  
               import plotly.graph_objects as go
               labelsQ = ['Trés bonne Qualité','bonne Qualité','Moyenne Qualité','Mauvaise Qualité']
               colorsQ = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
               valuesQ = [pourc_TBCsc4G, pourc_BCsc4G, pourc_MCsc4G, pourc_MAUCsc4G]

               fig4 = go.Figure(data=[go.Pie(labels=labelsQ, values=valuesQ,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colorsQ, line=dict(color='#ffffff', width=2))
                               )])
               fig4.update_traces(textposition='inside', pull=[0,0,0,0.1] )
               fig4.update_layout(

                   title={
                      'text': "Qualité 📶",
                      'y':0.9,
                      'x':0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
                   title_font_color="#3176BC",
                   title_font_size=30,
                   legend_title="Légende :",
                   legend_title_font_color="#4C7497",
                   font=dict(
                      family="Neo Sans Std ",
                      size=16,
                      color="#000000",
          
           
           
                    )
               )
               st.plotly_chart(fig4, use_container_width=True)
              else :
               st.image(image2, caption='')
               st.write('')                  
               st.error('Verifier les erreurs des seuils de RSRQ')   
   


        #***************** DEBIT AFFICHAGE ********************
           if 'Débit4G' in calculation4G :
                     image3 = Image.open('Debit.png')
                     st.image(image3, caption='')                     
                     st.write('')
                     if DL: 

                       display_app_header(main_txt='Débit Down Link', sub_txt='')
                       st.write('')       
                       if((IBDL<=ITBDL)and(ITBDL<=FMAXDL4G)and(ITBDL>=FMINDL4G)and(IBDL>=FMINDL4G)and(IMDL<=IBDL)and(IMDL>=FMINDL4G)and(IMAUDL<=IMDL)and(IMAUDL>=FMINDL4G)):
      
				
                        DLTBC=df.loc[(df['RLC downlink throughput']>0)]
                        DLTBC.reset_index(inplace=True)
                        timescDL=(DLTBC.iloc[:,1:2])
                        quarterscDL1=0
                        quarterscDL2=int(len(timescDL)/7)
                        quarterscDL3=int(len(timescDL)*2/7)
                        quarterscDL4=int(len(timescDL)*3/7)
                        quarterscDL5=int(len(timescDL)*4/7)
                        quarterscDL6=int(len(timescDL)*5/7)
                        quarterscDL7=int(len(timescDL)*6/7)
                        quarterscDL8=int(len(timescDL)-1)																									
                        fig7 = px.line(DLTBC, x='Time', y="RLC downlink throughput")
                        fig7.update_layout(
         
                        title={
                             'text': "Courbe de Débit DownLink 📶",
                           'y':0.95,
                            'x':0.5,
                            'xanchor': 'center',
                              'yanchor': 'top'},
                           title_font_color="#3176BC",
                           title_font_size=30,
                           legend_title="Légende :",
                           legend_title_font_color="#4C7497",
    
                            font=dict(
                              family="Neo Sans Std ",
                           size=16,
                                color="#4C7497",
       
        
        
                                 )
                            )
                        fig7.update_xaxes(
                          tickangle = 0,
                          tickvals=[timescDL.Time[quarterscDL1],timescDL.Time[quarterscDL2],timescDL.Time[quarterscDL3],timescDL.Time[quarterscDL4], timescDL.Time[quarterscDL5], ( timescDL.Time[quarterscDL6]),(timescDL.Time[quarterscDL7]),timescDL.Time[quarterscDL8]],
                          ticktext=[(str(timescDL.Time[quarterscDL1])[0:8]),(str(timescDL.Time[quarterscDL2])[0:8]),(str(timescDL.Time[quarterscDL3])[0:8]),(str(timescDL.Time[quarterscDL4])[0:8]),(str(timescDL.Time[quarterscDL5])[0:8]),(str(timescDL.Time[quarterscDL6])[0:8]),(str(timescDL.Time[quarterscDL7])[0:8]),(str(timescDL.Time[quarterscDL8])[0:8])],
                            title_font = {"size": 20},
                            ) 
                        
                        fig8= px.histogram(df, x=df['RLC downlink throughput'],
                              title='Histogram of bills 📊📡',
                              color_discrete_sequence=['#3176BC'])

                        fig8.update_layout(

                           title={
                              'text': "Répartitions de Débit DownLink 📊",
                              'y':0.9,
                              'x':0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
                           title_font_color="#3176BC",
                           legend_title_font_color="#4C7497",
                           title_font_size=30,
               
                           font=dict(
                              family="Neo Sans Std ",
                              size=16,
                              color="#4C7497",
                  
                  
                  
                           ))
                        st.plotly_chart(fig7, use_container_width=True)
                        st.plotly_chart(fig8, use_container_width=True)

               

                        ITBC4G = float(TBDL)
                        IBC4G = float(BDL)
                        IMC4G = float(MDL)
                        IMAUC4G = float(MAUDL)
                        VTBC4G=df.loc[(df['RLC downlink throughput']>=ITBC4G)]
                        VBC4G=df.loc[(df['RLC downlink throughput']<=ITBC4G)&(df['RLC downlink throughput']>=IBC4G)]
                        VMC4G=df.loc[(df['RLC downlink throughput']<=IBC4G)&(df['RLC downlink throughput']>=IMC4G)]
                        VMAUC4G=df.loc[(df['RLC downlink throughput']<=IMC4G)&(df['RLC downlink throughput']>=IMAUC4G)]
                        (echantillant)=len(VMAUC4G)+len(VBC4G)+len(VMC4G)+len(VTBC4G)
                        pourc_MAUC4G=(len(VMAUC4G)/echantillant)*100
                        pourc_MC4G=(len(VMC4G)/echantillant)*100
                        pourc_BC4G=(len(VBC4G)/echantillant)*100
                        pourc_TBC4G=(len(VTBC4G)/echantillant)*100
                  
                        import plotly.graph_objects as go
                        labels = ['Trés bonne DL Debit','bonne DL Debit','Moyenne DL Debit','Mauvaise DL Debit']
                        colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
                        values = [pourc_TBC4G, pourc_BC4G, pourc_MC4G, pourc_MAUC4G]

                        fig9 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#ffffff', width=2))
                               )])
                        fig9.update_traces(textposition='inside', pull=[0,0,0,0.1] )
                        fig9.update_layout(

                            title={
                               'text': "Débit DownLink 📶",
                               'y':0.9,
                               'x':0.5,
                               'xanchor': 'center',
                               'yanchor': 'top'},
                            title_font_color="#3176BC",
                            title_font_size=30,
                            legend_title="Légende :",
                            legend_title_font_color="#4C7497",
                            font=dict(
                               family="Neo Sans Std ",
                               size=16,
                               color="#000000",
          
           
           
                             )
                        )

                        st.plotly_chart(fig9, use_container_width=True)
                       else :

                        st.write('')	
                        st.error('Verifier les erreurs des seuils de DL Debit')   
    
                     if UP :
                       display_app_header(main_txt='Débit Up Link', sub_txt='')     

                       if((IBUL<=ITBUL)and(ITBUL<=FMAXUL4G)and(ITBUL>=FMINUL4G)and(IBUL>=FMINUL4G)and(IMUL<=IBUL)and(IMUL>=FMINUL4G)and(IMAUUL<=IMUL)and(IMAUUL>=FMINUL4G)):

                        ULTBC=df.loc[(df['RLC uplink throughput']>0)]
                        ULTBC.reset_index(inplace=True)
                        timescUL=(ULTBC.iloc[:,1:2])
                        quarterscUL1=0
                        quarterscUL2=int(len(timescUL)/7)
                        quarterscUL3=int(len(timescUL)*2/7)
                        quarterscUL4=int(len(timescUL)*3/7)
                        quarterscUL5=int(len(timescUL)*4/7)
                        quarterscUL6=int(len(timescUL)*5/7)
                        quarterscUL7=int(len(timescUL)*6/7)
                        quarterscUL8=int(len(timescUL)-1)																									
                        fig10 = px.line(ULTBC, x='Time', y="RLC uplink throughput")
                        fig10.update_layout(

                        title={
                             'text': "Courbe de Débit UpLink 📶",
                           'y':0.95,
                            'x':0.5,
                            'xanchor': 'center',
                              'yanchor': 'top'},
                           title_font_color="#3176BC",
                           title_font_size=30,
                           legend_title="Légende :",
                           legend_title_font_color="#4C7497",
    
                            font=dict(
                              family="Neo Sans Std ",
                           size=16,
                                color="#4C7497",
       
        
        
                                 )
                            )
                        fig10.update_xaxes(
                        tickangle = 0,
                        tickvals=[timescUL.Time[quarterscUL1],timescUL.Time[quarterscUL2],timescUL.Time[quarterscUL3],timescUL.Time[quarterscUL4], timescUL.Time[quarterscUL5], ( timescUL.Time[quarterscUL6]),(timescUL.Time[quarterscUL7]),timescUL.Time[quarterscUL8]],
                        ticktext=[(str(timescUL.Time[quarterscUL1])[0:8]),(str(timescUL.Time[quarterscUL2])[0:8]),(str(timescUL.Time[quarterscUL3])[0:8]),(str(timescUL.Time[quarterscUL4])[0:8]),(str(timescUL.Time[quarterscUL5])[0:8]),(str(timescUL.Time[quarterscUL6])[0:8]),(str(timescUL.Time[quarterscUL7])[0:8]),(str(timescUL.Time[quarterscUL8])[0:8])],
                            title_font = {"size": 20},
                            ) 
                        #display_app_header(main_txt='RSRP', sub_txt='')
                        #st.image(image2, caption='')
                        fig11= px.histogram(df, x=df['RLC uplink throughput'],
                               title='Histogram of bills 📊📡',
                               color_discrete_sequence=['#3176BC'])

                        fig11.update_layout(

                            title={
                              'text': "Répartitions de Débit UpLink 📊",
                              'y':0.9,
                              'x':0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
                           title_font_color="#3176BC",
                           legend_title_font_color="#4C7497",
                           title_font_size=30,
      
                           font=dict(
                               family="Neo Sans Std ",
                               size=16,
                               color="#4C7497",
          
           
           
                             ))
                        st.write('')					
                        st.plotly_chart(fig10, use_container_width=True)
                        st.plotly_chart(fig11, use_container_width=True)

               

                        ITBU4G = float(TBUL)
                        IBU4G = float(BUL)
                        IMU4G = float(MUL)
                        IMAUU4G = float(MAUUL)
                        VTBU4G=df.loc[(df['RLC uplink throughput']>=ITBU4G)]
                        VBU4G=df.loc[(df['RLC uplink throughput']<=ITBU4G)&(df['RLC uplink throughput']>=IBU4G)]
                        VMU4G=df.loc[(df['RLC uplink throughput']<=IBU4G)&(df['RLC uplink throughput']>=IMU4G)]
                        VMAUU4G=df.loc[(df['RLC uplink throughput']<=IMU4G)&(df['RLC uplink throughput']>=IMAUU4G)]
                        (echantillantUL)=len(VMAUU4G)+len(VBU4G)+len(VMU4G)+len(VTBU4G)
                        pourc_MAUU4G=(len(VMAUU4G)/echantillantUL)*100
                        pourc_MU4G=(len(VMU4G)/echantillantUL)*100
                        pourc_BU4G=(len(VBU4G)/echantillantUL)*100
                        pourc_TBU4G=(len(VTBU4G)/echantillantUL)*100
                  
                        import plotly.graph_objects as go
                        labels = ['Trés bonne UL Debit','bonne UL Debit','Moyenne UL Debit','Mauvaise UL Debit']
                        colors = ['57B947',  '#EEC51A','#F59339', '#EE5E43']
                        values = [pourc_TBU4G, pourc_BU4G, pourc_MU4G, pourc_MAUU4G]

                        fig12 = go.Figure(data=[go.Pie(labels=labels, values=values,textfont_size=20, textinfo='percent',
                                insidetextorientation='radial',marker=dict(colors=colors, line=dict(color='#ffffff', width=2))
                               )])
                        fig12.update_traces(textposition='inside', pull=[0,0,0,0.1] )
                        fig12.update_layout(

                            title={
                               'text': "Débit UpLink 📶",
                               'y':0.9,
                               'x':0.5,
                               'xanchor': 'center',
                               'yanchor': 'top'},
                            title_font_color="#3176BC",
                            title_font_size=30,
                            legend_title="Légende :",
                            legend_title_font_color="#4C7497",
                            font=dict(
                               family="Neo Sans Std ",
                               size=16,
                               color="#000000",
          
           
           
                             )
                        )
                        st.plotly_chart(fig12, use_container_width=True)
                       else :
                        
                        st.write('')                          
                        st.error('Verifier les erreurs des seuils de UL Debit')


              
         #***************** RSRP/RSRQ AFFICHAGE ********************
           if 'RSRQ' in calculation4G:
            if 'RSRP' in calculation4G:
             display_app_header4(main_txt='Points avec bonne couverture et mauvaise qualité :')
             st.write('')
             BC4G_MQ=df.loc[((df['RSRP (pcell)']>=IBC4G)&(df['RSRQ (pcell)']<=IMAUCsc4G))]
             st.write(BC4G_MQ)
                

    
