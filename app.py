import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

##############
st.sidebar.image("fondo_quimica2.png",
                 caption="Jesus Alvarado H, MSc, PhDc")

##############Pagina 1##############
def Home():
    st.markdown("# ")
    st.sidebar.markdown("# Química II")

    total1, total2 = st.columns(2, gap='large')
    with total1:
        st.info('Unidad 1: ESTRUCTURA DE LOS COMPUESTOS DEL CARBONO')
        st.write('''Generalidades del carbono / moléculas polares y no polares / 
        Polaridad de enlace, dipolo particular /
        carga formal / Naturaleza única del carbono / 
        Orbital atómico, orbital molecular, enlace pi, enlace sigma.''')
        
    with total2:
        st.info('Unidad 2: ANÁLISIS QUÍMICO DETERMINACIÓN DE FORMULAS')
        st.write ('''Análisis químico / Estructura molecular de compuestos orgánicos, formula empírica y formula
molecular, problemas / Métodos para determinar pesos moleculares.''')
    
    total3, total4 = st.columns(2, gap='large')
    with total3:
        st.info('Unidad 3: ALCANOS, ALQUENOS, ALQUINOS')
        st.write('''Definición, propiedades / Nomenclatura IUPAC y reactividad química / 
        métodos de preparación, ejercicios / El metano y su importancia / 
        Aplicación en la industria del plástico de los alquenos / 
        El acetileno / Hidrocarburos alicíclicos, nomenclatura y reacciones importantes.''')
        
    with total4:
        st.info('Unidad 4: COMPUESTOS ORGÁNICOS Y GRUPOS FUNCIONALES CARACTERISTICOS')
        st.write ('''Definición y prioridad de los grupos funcionales / 
        Nomenclatura de los compuestos poli funcionales /
        Alcoholes y fenoles, propiedades, reactividad química, métodos de preparación / 
        Éteres, estructura y propiedades, reactividad química, métodos de preparación / 
        Aldehído y cetona, estructura y propiedades, reactividad química, 
        métodos de preparación, aplicaciones industriales / 
        Ácidos carboxílicos y derivados, estructura y propiedades, 
        reactividad química, métodos de preparación, aplicaciones
        industriales / Jabones y detergentes, aceites vegetales y grasas, estructuras / 
        Aminas, Amidas y nitrilos, estructura y propiedades, reactividad química, 
        métodos de preparación, aplicaciones industriales /
        Polímeros, meros, métodos de polimerización, proteínas, 
        Monosacáridos, Disacáridos, Polisacáridos.''')

    
    
##############Pagina 2##############
def page2():
    st.markdown("# Actividad: 25/03/2024")
    st.sidebar.markdown("# ")
    
    st.info('Individual')
    st.write('''Tiempo estimado: 1 hora''')
    st.write('''Fecha de entrega: No aplica''')
    st.write ('''Repasar material introductorio sobre python en Google Colab''')
    st.write('Sugerencia: https://github.com/inefable12/CQCPE_2023_jesus/blob/main/1_ABC_Python_github.ipynb')

##
def page3():
  st.header('Más información', divider='rainbow')
  st.link_button("Github", "https://github.com/inefable12/Quimica_2_FIA_UNI/")
  st.write('''Asistencia''')

  lista = pd.DataFrame({'Nombre': ['Letona Vargas Kylie Jacqueline', 
                                    'Espinoza Peralta Mayra Andrea', 
                                    'Garcia Ignacio Lizet Alfonsina',
                                    'Villanueva Valencia Carlos Wilder',
                                    'Gonzales Carrera Keipry Niasay',
                                    'Gastello Seclen Fernanda Isabel',
                                    'Lara Giraldo Aldair Alessandro',
                                    'Lara Giraldo Italo Sebastián',
                                    'Ayala Grados Angel Sebastián',
                                    'Toribio Mamani Angel Brandon',
                                    'Maguiña Ticona Adriana Isabel',
                                    'Cuzcano Pintado Angelly del Pilar',
                                    'Torre Zarzo Ana Barbara',
                                    'Utrilla Flores María del Carmen',
                                    'Sanchez Estrada Diego André',
                                    'Ruiz Alfaro Jhohan David',
                                    'Castañeda León Nelson Mijhael',
                                    'Santiago Asencios Alondra', 
                                    'Guerrero Obregon Jose Carlos',
                                    'Medina Ramirez Carlos Sebastian',
                                    'Quispe Baltazar Marco',
                                    'Quispe Icarayme Matias Alfredo',
                                    'Miranda Tipte Brigit Magdiel',
                                    'Coronel Jaimes Gonzalo'], 
                        '18/03/2024': ["X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X"],
                        '25/03/2024': ["X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","X","X",
                                       "X","X","X","F"]
                        })
  
  st.write(lista)

  st.write('''Est''')
  st.bar_chart(
   lista, x="Nombre", y=["18/03/2024", "25/03/2024"], color=["#FF0000", "#0000FF"])

##
page_names_to_funcs = {
  "Contenido del Curso": Home,
  "Actividad": page2,
  "Consultas": page3,
}

selected_page = st.sidebar.selectbox("Selecciona una página", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
