import streamlit as st
import numpy as np
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

menu = st.sidebar.selectbox("Seleccione el ejercicio",["Inicio", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])


if menu == "Inicio":
    st.title("Proyecto Python")
    st.write("Estudiante: Jhon Kevin Montalvo Ccanchi")
    st.write("Módulo: Python Fundamentals")
    st.write("Hola, mi nombre es Jhon, soy de Perú, tengo 30 años, trabajo como Geologo de producción")
    st.markdown("2026")
    st.sidebar.image("alumno.png",width=200)

elif menu == "Ejercicio 1":
    st.title("Flujo de Caja")

elif menu == "Ejercicio 2":
    st.title(" Registro de productos")

elif menu == "Ejercicio 3":
    st.title("Calculo de Productividad")

elif menu == "Ejercicio 4":
    st.title("Mezcla de Concreto")


##### Ejecicio 1 

if menu =="Ejercicio 1":

    if"Inf":
        st.sidebar.image("imagen1.png",width=200)
        st.markdown("Con este aplicativo podrás registrar todos tus ingresos y gastos, finalmente obtener un balance de caja, ya sea a favor o en contra.")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=00)

    if st.button("Agregar"):
        st.session_state.movimientos.append({
            "concepto": concepto,
            "tipo": tipo,
            "valor": valor})
        
    st.write("Movimientos:")
    st.write(st.session_state.movimientos)

    ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
    gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")

    saldo = ingresos - gastos

    st.write("Ingresos:", ingresos)
    st.write("Gastos:", gastos)
    st.write("Saldo:", saldo)

    if saldo >= 0:
        st.success("Saldo a favor")
    else:
        st.error("Saldo en contra")

#### Ejercicio 2

if menu == "Ejercicio 2":

    if "Inf":
        st.sidebar.image("imagen2.png",width=200)
        st.markdown("Con este aplicativo podras registrar de mandera sensilla productos, ventas y toda informacion, para llevar un control")

    if "Productos" not in st.session_state:
        st.session_state.productos = []

        nombre = st.text_input("Nombre del producto")
        categoria = st.selectbox("Categoria",["Compra","Venta"])
        precio = st.number_input("Precio", min_value=0.0)
        cantidad = st.number_input("Cantidad", min_value=0)

    if st.button("Agregar"):

        if nombre != "" and precio > 0 and cantidad > 0:

            total = precio * cantidad

            st.session_state.productos.append([nombre, categoria, precio, cantidad, total])
            st.success("Producto agregado correctamente")

        else:
            st.error("Complete los datos correctamente")


    if len(st.session_state.productos) > 0:
        datos = np.array(st.session_state.productos, dtype=object)
        st.dataframe(datos)

        totales = datos[:,4].astype(float)
        suma_total = np.sum(totales)

        st.metric("totales",suma_total,"S/.")

### Ejercici 3

if menu == "Ejercicio 3":

    st.sidebar.image("imagen3.png", width=200)
    st.markdown("Aplicativo para el cálculo de la productividad de colaboradores")

    if "personal_prod" not in st.session_state:
        st.session_state.personal_prod = []

    unidades = st.number_input("Unidades producidas", min_value=1)
    horas = st.number_input("Horas trabajadas", min_value=0.1)
    trabajadores = st.number_input("Número de trabajadores", min_value=1)

    if st.button("Cálculo de productividad"):

        resultado = lf.calcular_productividad_laboral(unidades, horas, trabajadores)

        st.write("Resultado:", resultado)

        st.session_state.personal_prod.append([
            unidades,
            horas,
            trabajadores,
            resultado["productividad_por_hora"],
            resultado["productividad_por_trabajador"]
        ])

    if len(st.session_state.personal_prod) > 0:

        datos = np.array(st.session_state.personal_prod, dtype=object)

        encabezados = [
            "Unidades",
            "Horas",
            "Trabajadores",
            "Prod/Hora",
            "Prod/Trabajador"]

        tabla = [encabezados] + datos.tolist()

        st.write("Historial de cálculos:")
        st.dataframe(tabla)

### Ejercici 4

if menu == "Ejercicio 4":
    st.sidebar.image("imagen4.png",width=200)
    st.markdown("Con el aplicativo podra calcular la mezcla.")

    if "mezclas" not in st.session_state:
        st.session_state.mezclas = []
    
    largo = st.number_input("Largo (m)", min_value=0.1)
    ancho = st.number_input("Ancho (m)", min_value=0.1)
    espesor = st.number_input("Espesor (m)", min_value=0.01)
    desperdicio = st.number_input("Desperdicio (%)", min_value=0.0)
    dosificacion = st.number_input("Dosificación (kg/m3)", min_value=0.1)

    if st.button("Agregar"):

        mezcla = lc.MezclaConcreto(largo, ancho, espesor, desperdicio, dosificacion)
        r = mezcla.resumen()

        st.session_state.mezclas.append([
            largo, ancho, espesor, desperdicio, dosificacion,
            r["volumen_m3"], r["volumen_ajustado_m3"],
            r["cemento_kg"], r["sacos_50kg"]])

        st.success("Guardado")

    if len(st.session_state.mezclas) > 0:

        columnas = ["Largo", "Ancho", "Espesor", "Desperdicio", "Dosificación","Volumen", "Vol Ajustado", "Cemento (kg)", "Sacos"]

        tabla = []

        for fila in st.session_state.mezclas:
            tabla.append({
                columnas[0]: fila[0],
                columnas[1]: fila[1],
                columnas[2]: fila[2],
                columnas[3]: fila[3],
                columnas[4]: fila[4],
                columnas[5]: fila[5],
                columnas[6]: fila[6],
                columnas[7]: fila[7],
                columnas[8]: fila[8],})

        st.dataframe(tabla)

    if len(st.session_state.mezclas) > 0:

        idx = st.number_input("Indice actualizar", min_value=0, step=1)

        if st.button("Actualizar"):

            if idx < len(st.session_state.mezclas):

                mezcla = lc.MezclaConcreto(largo, ancho, espesor, desperdicio, dosificacion)
                r = mezcla.resumen()

                st.session_state.mezclas[idx] = [
                    largo, ancho, espesor, desperdicio, dosificacion,
                    r["volumen_m3"], r["volumen_ajustado_m3"],
                    r["cemento_kg"], r["sacos_50kg"]]

                st.success("Actualizado")
            else:
                st.error("Indice inválido")

    if len(st.session_state.mezclas) > 0:

        idx_del = st.number_input("Indice eliminar", min_value=0, step=1)

        if st.button("Eliminar"):

            if idx_del < len(st.session_state.mezclas):
                st.session_state.mezclas.pop(idx_del)
                st.success("Eliminado")
            else:
                st.error("Indice inválido")


