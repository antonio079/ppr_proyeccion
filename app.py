import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.title('PROYECCIÓN DEL VALOR DEL DINERO EN EL TIEMPO :sunglasses:')

st.header('IMAGINA SER 65 AÑOS')
st.write('Estas simulaciones son estimaciones en base a datos históricos:blue_book:') 

st.divider()

pb = st.number_input("Prima basica (UDIs)", value=3000.0, placeholder="Escribe aqui...")
st.write("El valor escrito es ", pb," UDIs")

pp = st.number_input("Prima planeada (UDIs)", value=1000.0, placeholder="Escribe aqui...")
st.write("El valor escrito es ", pp," UDIs")

plazo = st.number_input("Plazo de aportación ", value=15, placeholder="Escribe aqui...")
st.write("El valor escrito es ", plazo," años")

plazo_total = st.number_input("Plazo de protección ", value=30, placeholder="Escribe aqui...")
st.write("El valor escrito es ", plazo_total," años")

udi = st.number_input("Valor de la UDI ", value=8.5, placeholder="Escribe aqui...")
st.write("El valor escrito es ", udi)

inf = st.number_input("Inflación ", value=0.045, placeholder="Escribe aqui...")
st.write("El valor escrito es ", inf)


def proyeccion(pb=3000.0, pad=0.0, plazo=15.0, tiempo_total=30.0, udi=8.5, inf = 0.045):
    """
    pb = Prima Basica (UDIs)
    plazo = Plazo de aportacion
    tiempo_total = Tiempo total de inversion
    pad =  Prima Adicional
    udi = Unidad De Inversión
    inf = Inflación 
    """
    tasa_anual = 0.02

    datos = np.zeros([3,int(tiempo_total)])    
    datos[0,0] = pb + pad
    datos[1,0] = udi
        
    for i in range(tiempo_total-1):
        if i < plazo:
            datos[0,i+1] =+ datos[0,i]*(1.0+tasa_anual) + pb + pad
            datos[1,i+1] =+ datos[1,i]*(1.0+inf) 
        else:
            datos[0,i+1] =+ datos[0,i]*(1.0+tasa_anual)
            datos[1,i+1] =+ datos[1,i]*(1.0+inf) 
            
    datos[2,:] = datos[0,:] * datos[1,:]  
                
    return datos

data = proyeccion(pb, pp, plazo, plazo_total, udi, inf)

fig = px.bar(data[2,:])
fig.update_layout(showlegend=True, autosize=False, width=900, height=450, bargap=0.05,
                  template='seaborn', title=("<b> Fondo M.N."), title_x=0.5,
                  xaxis_title=("Año"), yaxis_title=("MXN"))
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.divider()

 







