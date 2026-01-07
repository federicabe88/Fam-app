import streamlit as st

# Stile ispirato a FamilyWall
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 24px; }
    .family-card {
        background-color: white; padding: 15px; border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 10px;
    }
    .stApp { background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_stdio=True)

# Dashboard Principale
st.title("👨‍👩‍👧 Family Command Center")

# Simulazione Database (Stato dell'app)
if 'spesa' not in st.session_state:
    st.session_state.spesa = ["Latte", "Pane"]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📅 Prossimi Impegni")
    st.info("**Oggi 16:00** - Danza (Figlia) 🩰")
    st.warning("**Domani 09:00** - Dentista (Mamma) 🦷")
    
    st.subheader("🍲 Menù del Giorno")
    with st.container():
        st.markdown("<div class='family-card'>🍴 <b>Pranzo:</b> Risotto allo zafferano<br>🥗 <b>Cena:</b> Cotoletta e insalata</div>", unsafe_allow_stdio=True)

with col2:
    st.subheader("🛒 Spesa Rapida")
    for item in st.session_state.spesa:
        st.checkbox(item, key=item)
    
    nuovo_item = st.text_input("Aggiungi...")
    if st.button("Aggiungi alla lista"):
        st.session_state.spesa.append(nuovo_item)
        st.rerun()

# Sezione Spese (Grafico rapido)
st.divider()
st.subheader("💰 Budget Mensile")
st.progress(0.65, text="65% del budget utilizzato")
