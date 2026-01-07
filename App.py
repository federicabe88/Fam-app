import streamlit as st

# Configurazione pagina per renderla bella su mobile
st.set_page_config(page_title="Family Hub", layout="wide")

# Stile ispirato a FamilyWall - CORRETTO
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 24px; }
    .family-card {
        background-color: white; 
        padding: 15px; 
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
        margin-bottom: 10px;
        color: #31333F;
    }
    .stApp { background-color: #f8f9fa; }
    </style>
    """, unsafe_allow_html=True)

# Dashboard Principale
st.title("👨‍👩‍👧 Family Command Center")

# Simulazione Database (Stato dell'app)
if 'spesa' not in st.session_state:
    st.session_state.spesa = ["Latte 🥛", "Pane 🥖"]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📅 Prossimi Impegni")
    st.info("**Oggi 16:00** - Danza (Figlia) 🩰")
    st.warning("**Domani 09:00** - Dentista (Mamma) 🦷")
    
    st.subheader("🍲 Menù del Giorno")
    st.markdown("""
        <div class='family-card'>
            🍴 <b>Pranzo:</b> Risotto allo zafferano<br>
            🥗 <b>Cena:</b> Cotoletta e insalata
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.subheader("🛒 Spesa")
    # Visualizza la lista
    for i, item in enumerate(st.session_state.spesa):
        st.checkbox(item, key=f"item_{i}")
    
    nuovo_item = st.text_input("Aggiungi alla lista...")
    if st.button("Aggiungi"):
        if nuovo_item:
            st.session_state.spesa.append(nuovo_item)
            st.rerun()

# Sezione Spese
st.divider()
st.subheader("💰 Budget Mensile")
st.progress(0.65, text="65% del budget utilizzato")
