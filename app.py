import streamlit as st

# 1. Configuración de la página (Diseño ancho para aprovechar pantalla)
st.set_page_config(
    page_title="Simulador: Liderazgo del Entrenador",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilos CSS personalizados para mejorar la estética visual
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .card-caso {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin-bottom: 20px;
    }
    .feedback-box {
        background-color: #F1F5F9;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        border: 1px solid #CBD5E1;
    }
    </style>
""", unsafe_allow_html=True)

# Barra lateral informativa modificada
with st.sidebar:
    st.title("El liderazgo del entrenador")
    st.markdown("**Máster de Investigación en Ciencias del Deporte**")
    st.info("💡 **Dinámica:** Analiza el caso crítico, debate con tu grupo y selecciona el estilo de liderazgo óptimo para intervenir.")
    st.divider()
    st.caption("UCLM - Rendimiento Experto")

# Cabecera principal atractiva
st.markdown('<p class="main-header">⚽ Gabinete de Crisis: El Descanso</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Minuto 45 | Partido de eliminatoria de élite | <strong>Marcador en contra: 0-2</strong></p>', unsafe_allow_html=True)

# Pestañas principales para ordenar la sesión
pestana_inicio, pestana_casos, pestana_teoria = st.tabs(["🚀 Introducción", "📋 Simulador de Casos (4 Estilos)", "🧠 Tipos de liderazgo"])

with pestana_inicio:
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### El Escenario del Vestuario")
        st.write("""
        El equipo muestra un **bajón anímico evidente** y tensión interna tras una primera parte desastrosa. 
        Como cuerpo técnico, los 15 minutos del descanso son vitales para reestructurar el rumbo táctico 
        pero, sobre todo, para gestionar la **estabilidad emocional** y conductual de la plantilla.
        """)
        st.warning("⚠️ **Atención:** Una mala elección del estilo de liderazgo puede destruir por completo el rendimiento de la segunda mitad.")
    with col_b:
        st.info("🎯 **Objetivos de la Dinámica:**")
        st.markdown("""
        * Identificar perfiles de alta complejidad en la gestión deportiva.
        * Contrastar los 4 tipos de liderazgo del modelo teórico.
        * Evaluar el impacto que tiene el estilo del entrenador en los jugadores/as.
        """)

with pestana_casos:
    # Selector de los 4 casos clínicos
    caso_seleccionado = st.selectbox(
        "**Selecciona el caso clínico a resolver en el vestuario:**",
        [
            "🔥 Caso 1: El Capitán Veterano (Ego e Insubordinación)",
            "❄️ Caso 2: La Joven Promesa (Bloqueo Emocional y Ansiedad)",
            "⚡ Caso 3: El Fichaje Estrella (Disrupción del Propósito Colectivo)",
            "🛡️ Caso 4: El Colectivo en Indefensión Aprendida (Apático y Sin Rumbo)"
        ]
    )
    
    st.divider()

    if "Caso 1" in caso_seleccionado:
        st.markdown('<div class="card-caso">', unsafe_allow_html=True)
        st.subheader("🔥 Caso 1: El Capitán Frustrado")
        st.markdown("**Perfil:** Central titular (34 años, 12 temporadas en el club).")
        st.markdown("**Situación en el descanso:** Acumula tarjeta amarilla, error grave en el 2º gol y cuestiona al entrenador en el túnel de vestuarios cruzándose de brazos frente a los jóvenes.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        estilo_elegido = st.radio(
            "Selecciona el estilo de liderazgo que aplicas en esta intervención:",
            [
                "🌟 Liderazgo Transformacional",
                "🤝 Liderazgo Transaccional",
                "🛡️ Liderazgo Auténtico",
                "💨 Liderazgo Pasivo / Evitativo (Laissez-Faire)"
            ],
            key="estilo_1"
        )
        
        if st.button("🚀 Evaluar Estilo Aplicado", type="primary", key="btn_1"):
            if "Transformacional" in estilo_elegido:
                st.success("✅ **¡Intervención Óptima!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Cohesión del Vestuario", value="+85%", delta="Alta")
                c2.metric(label="Eficacia Táctica", value="Óptima", delta="Recuperada")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** El entrenador actúa como agente de cambio aplicando *Influencia Idealizada* (mantiene la calma bajo presión extrema en el minuto 45) y *Consideración Individualizada* (reconoce la jerarquía del veterano sin ceder en disciplina)[cite: 4].
                * **Conclusión teórica:** Alinea su experiencia con el propósito colectivo, generando autonomía y cohesión profunda en lugar de rupturas de vestuario[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Transaccional" in estilo_elegido:
                st.warning("⚠️ **¡Efecto Limitado / Riesgo de Conflicto!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Cohesión del Vestuario", value="-25%", delta="Tensión")
                c2.metric(label="Eficacia Táctica", value="Inestable", delta="Riesgo")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué es limitado:** Se basa en un intercambio contingente y correcciones punitivas[cite: 4]. Aunque útil para mantener disciplina a corto plazo, aplicar una bronca punitiva a un líder con estatus intocable desencadena un enfrentamiento de egos[cite: 4].
                * **Conclusión teórica:** Quiebra el clima de seguridad psicológica del grupo[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Auténtico" in estilo_elegido:
                st.success("✅ **¡Intervención Muy Sólida!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Cohesión del Vestuario", value="+80%", delta="Alta")
                c2.metric(label="Eficacia Táctica", value="Estable", delta="Positiva")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** Se centra en la coherencia ética, la transparencia relacional y el procesamiento equilibrado[cite: 4]. El líder admite errores sin prejuicios.
                * **Conclusión teórica:** Genera alta confianza moral y desarma la actitud defensiva del capitán[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("❌ **¡Intervención Desastrosa!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Cohesión del Vestuario", value="-70%", delta="Crítico")
                c2.metric(label="Eficacia Táctica", value="Nula", delta="Colapso")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué es desastrosa:** Representa la ausencia total de liderazgo efectivo (Laissez-Faire)[cite: 4]. El entrenador evita tomar decisiones o mediar ante el conflicto.
                * **Conclusión teórica:** Genera ambigüedad y desorientación absoluta, permitiendo que el liderazgo informal negativo destruya la autoridad del cuerpo técnico[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)

    elif "Caso 2" in caso_seleccionado:
        st.markdown('<div class="card-caso">', unsafe_allow_html=True)
        st.subheader("❄️ Caso 2: La Joven Promesa Bloqueada")
        st.markdown("**Perfil:** Extremo izquierdo (20 años, fichaje de futuro).")
        st.markdown("**Situación en el descanso:** Ha fallado un mano a mano clave. Hiperventilando, con la cabeza gacha, pidiendo no volver a tocar el balón por miedo a la presión de la grada.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        estilo_elegido = st.radio(
            "Selecciona el estilo de liderazgo que aplicas en esta intervención:",
            [
                "🌟 Liderazgo Transformacional",
                "🤝 Liderazgo Transaccional",
                "🛡️ Liderazgo Auténtico",
                "💨 Liderazgo Pasivo / Evitativo (Laissez-Faire)"
            ],
            key="estilo_2"
        )
        
        if st.button("🚀 Evaluar Estilo Aplicado", type="primary", key="btn_2"):
            if "Transformacional" in estilo_elegido or "Auténtico" in estilo_elegido:
                st.success("✅ **¡Intervención Óptima!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Confianza del Jugador", value="Alta", delta="Recuperado")
                c2.metric(label="Seguridad Psicológica", value="Óptima", delta="+")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** Aplica la *Consideración Individualizada* y transparencia relacional[cite: 4]. Atiende las necesidades emocionales específicas del deportista joven.
                * **Conclusión teórica:** Protege psicológicamente al activo frente al error, fomentando la motivación intrínseca y reduciendo la ansiedad[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Transaccional" in estilo_elegido:
                st.warning("⚠️ **¡Efecto Contraproducente!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Confianza del Jugador", value="-50%", delta="Baja")
                c2.metric(label="Seguridad Psicológica", value="Nula", delta="Riesgo")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué falla:** Basado en la exigencia de rendimiento inmediato y reprimendas punitivas[cite: 4].
                * **Conclusión teórica:** Exigir resultados bajo amedrentamiento en un jugador hiperventilando agrava su bloqueo y destruye su seguridad psicológica[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("❌ **¡Intervención Desastrosa!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Confianza del Jugador", value="-90%", delta="Colapso")
                c2.metric(label="Seguridad Psicológica", value="Inexistente", delta="Crítico")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué es desastrosa:** Omitir feedback y mostrar pasividad (Laissez-Faire) ante un jugador al borde del llanto[cite: 4].
                * **Conclusión teórica:** La ausencia de guía y soporte genera indefensión aprendida y desorientación total en el deportista[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)

    elif "Caso 3" in caso_seleccionado:
        st.markdown('<div class="card-caso">', unsafe_allow_html=True)
        st.subheader("⚡ Caso 3: El Fichaje Estrella Individualista")
        st.markdown("**Perfil:** Centrocampista ofensivo (27 años, jugador mejor pagado).")
        st.markdown("**Situación en el descanso:** Ignora las coberturas defensivas, busca exclusivamente su estadística personal y lanza las espinilleras culpando a la defensa de los goles.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        estilo_elegido = st.radio(
            "Selecciona el estilo de liderazgo que aplicas en esta intervención:",
            [
                "🌟 Liderazgo Transformacional",
                "🤝 Liderazgo Transaccional",
                "🛡️ Liderazgo Auténtico",
                "💨 Liderazgo Pasivo / Evitativo (Laissez-Faire)"
            ],
            key="estilo_3"
        )
        
        if st.button("🚀 Evaluar Estilo Aplicado", type="primary", key="btn_3"):
            if "Transformacional" in estilo_elegido:
                st.success("✅ **¡Intervención Óptima!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Compromiso Táctico", value="90%", delta="Alto")
                c2.metric(label="Alineación de Egos", value="Positiva", delta="Unificado")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** Utiliza la *Estimulación Intelectual* y la visión de un propósito colectivo superior[cite: 4]. Reta al jugador a entender que sus estadísticas dependen del bloque.
                * **Conclusión teórica:** Alinea metas individuales con el equipo sin necesidad de coerción[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Transaccional" in estilo_elegido:
                st.warning("⚠️ **¡Efecto Mixto / Disciplinario!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Compromiso Táctico", value="50%", delta="Forzado")
                c2.metric(label="Alineación de Egos", value="Tensas", delta="Control")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué es limitado:** Basado estrictamente en normas y amenaza de suplencia o multa[cite: 4]. 
                * **Conclusión teórica:** Puede frenar su ego por obligación a corto plazo, pero no genera autonomía profunda ni compromiso genuino con el modelo de juego[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Auténtico" in estilo_elegido:
                st.success("✅ **¡Intervención Sólida!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Compromiso Táctico", value="85%", delta="Alto")
                c2.metric(label="Alineación de Egos", value="Firme", delta="Valores")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** Transparencia relacional y confrontación basada en valores morales compartidos del club[cite: 4].
                * **Conclusión teórica:** Establece límites éticos claros sobre el esfuerzo colectivo exigido[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("❌ **¡Intervención Desastrosa!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Compromiso Táctico", value="10%", delta="Colapso")
                c2.metric(label="Alineación de Egos", value="Anarquía", delta="Ruptura")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué es desastrosa:** Permisividad total (Laissez-Faire)[cite: 4]. Otorgar libertad absoluta a una estrella individualista.
                * **Conclusión teórica:** Destruye el principio de autoridad del entrenador y provoca una revuelta inmediata en el resto de la plantilla al percibir trato de favor[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="card-caso">', unsafe_allow_html=True)
        st.subheader("🛡️ Caso 4: Indefensión Aprendida Colectiva")
        st.markdown("**Perfil:** Plantilla completa tras encajar dos goles en 5 minutos.")
        st.markdown("**Situación en el descanso:** Silencio sepulcral en el vestuario. Los jugadores asumen con resignación que el partido está perdido y que el rival es superior, mostrando pasividad total.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        estilo_elegido = st.radio(
            "Selecciona el estilo de liderazgo que aplicas en esta intervención:",
            [
                "🌟 Liderazgo Transformacional",
                "🤝 Liderazgo Transaccional",
                "🛡️ Liderazgo Auténtico",
                "💨 Liderazgo Pasivo / Evitativo (Laissez-Faire)"
            ],
            key="estilo_4"
        )
        
        if st.button("🚀 Evaluar Estilo Aplicado", type="primary", key="btn_4"):
            if "Transformacional" in estilo_elegido:
                st.success("✅ **¡Intervención Óptima!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Moral Colectiva", value="+90%", delta="Motivados")
                c2.metric(label="Potencial de Remontada", value="Alto", delta="Activo")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** Aplica *Motivación Inspiradora* y reto intelectual[cite: 4]. 
                * **Conclusión teórica:** Es el único estilo capaz de romper la indefensión aprendida, infundiendo una visión optimista y reavivando el propósito colectivo[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Transaccional" in estilo_elegido:
                st.warning("⚠️ **¡Efecto Insuficiente!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Moral Colectiva", value="30%", delta="Baja")
                c2.metric(label="Potencial de Remontada", value="Bajo", delta="Miedo")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué falla:** Amenazas de sanciones o exigencia basada en castigos[cite: 4].
                * **Conclusión teórica:** Ante un grupo bloqueado por la apatía, el castigo transaccional incrementa el miedo al error en lugar de reactivar la energía intrínseca[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            elif "Auténtico" in estilo_elegido:
                st.success("✅ **¡Intervención Muy Correcta!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Moral Colectiva", value="+75%", delta="Estable")
                c2.metric(label="Potencial de Remontada", value="Moderado", delta="Firme")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué funciona:** Procesamiento equilibrado y autoconciencia del entrenador[cite: 4].
                * **Conclusión teórica:** Asume su parte táctica y transmite confianza inquebrantable en los valores del grupo[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("❌ **¡Fracaso Absoluto del Cuerpo Técnico!**")
                c1, c2 = st.columns(2)
                c1.metric(label="Moral Colectiva", value="0%", delta="hundidos")
                c2.metric(label="Potencial de Remontada", value="Nulo", delta="Derrota")
                
                st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
                st.markdown("#### 🎓 Feedback Académico y Conclusiones")
                st.write("""
                * **Por qué es desastrosa:** Ausencia total de liderazgo (Laissez-Faire)[cite: 4]. Entrar al vestuario sin decir nada o demorar la intervención.
                * **Conclusión teórica:** Consolida la derrota psicológica antes de saltar al campo, evidenciando una falta absoluta de dirección técnica[cite: 4].
                """)
                st.markdown('</div>', unsafe_allow_html=True)

with pestana_teoria:
    st.subheader("🧠 Los Cuatro Estilos de Liderazgo del Entrenador")
    st.write("Para entender cómo la conducta del entrenador modula este proceso, partimos del *Full Range Leadership Model* (Bass y Riggio, adaptado al deporte por autores como Turnnidge & Côté, 2018; Lefebvre et al., 2021) y su comparativa con el liderazgo auténtico (Malloy & Kavussanu, 2021)[cite: 4]:")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("##### 🌟 Liderazgo Transformacional")
        st.write("El entrenador actúa como un agente de cambio que inspira, reta intelectualmente y empodera a sus deportistas. No se limita a dirigir tareas, sino que alinea los objetivos individuales con un propósito colectivo superior, fomentando la autonomía, la motivación intrínseca y el crecimiento personal y deportivo[cite: 4].")
        
        st.markdown("##### 🤝 Liderazgo Transaccional")
        st.write("Se basa en una relación de intercambio contingente (\"si haces X, obtienes Y\"). El entrenador establece expectativas claras, supervisa el cumplimiento de las normas y utiliza refuerzos (elogios, titularidad, minutos) o penalizaciones (correcciones punitivas, suplencia) en función del rendimiento inmediato o el error. Es eficaz para mantener el orden y la disciplina a corto plazo, pero limitado para generar autonomía profunda[cite: 4].")
        
    with col_t2:
        st.markdown("##### 🛡️ Liderazgo Auténtico")
        st.write("Como analizan Malloy y Kavussanu (2021), se centra en la coherencia ética, la transparencia relacional, la autoconciencia y el procesamiento equilibrado del entrenador. Este líder actúa conforme a sus valores morales, admite sus propios errores, escucha sin prejuicios y genera un clima de alta confianza psicológica y seguridad moral en el equipo[cite: 4].")
        
        st.markdown("##### 💨 Liderazgo Pasivo / Evitativo (Laissez-Faire)")
        st.write("Representa la ausencia de liderazgo efectivo. El entrenador evita tomar decisiones, no proporciona feedback estructurado, demora su intervención ante conflictos o errores tácticos y delega la responsabilidad sin ofrecer guía ni soporte, generando ambigüedad y desorientación en el deportista[cite: 4].")