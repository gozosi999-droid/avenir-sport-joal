import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURATION SYSTÈME ---
st.set_page_config(
    page_title="AVENIR SPORT | Neural Interface",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS ANIMÉ & COMPLEXE (VERSION NEURAL) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    /* Fond & Effet Matrix */
    .stApp {
        background-color: #030303;
        color: #e0e0e0;
    }

    /* ANIMATION : STATUS PULSE */
    @keyframes pulse-gold {
        0% { box-shadow: 0 0 0 0 rgba(255, 218, 0, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(255, 218, 0, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 218, 0, 0); }
    }

    /* ANIMATION : SCANNER LINE */
    @keyframes scan {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(1000%); }
    }

    /* CONTROL PANEL STYLING */
    .sidebar .stMarkdown {
        font-family: 'Share Tech Mono', monospace;
    }

    .status-box {
        background: rgba(255, 218, 0, 0.05);
        border: 1px solid #ffda00;
        padding: 15px;
        border-radius: 10px;
        position: relative;
        overflow: hidden;
    }

    .status-box::after {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 2px;
        background: #ffda00;
        animation: scan 3s linear infinite;
        opacity: 0.3;
    }

    .pulse-dot {
        height: 10px; width: 10px;
        background-color: #ffda00;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
        animation: pulse-gold 2s infinite;
    }

    /* TITRE GLITCH */
    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 100px !important;
        color: #ffda00;
        text-align: center;
        text-shadow: 3px 3px #555;
        letter-spacing: 10px;
    }

    /* PROGRESS BAR PERSONNALISÉE */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #8a6d3b , #ffda00);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BASE DE DONNÉES (EXTENSIBLE) ---
class InventorySystem:
    def __init__(self):
        self.items = [
            {"id": "AS-99", "nom": "Maillot Senegal Home", "cat": "ELITE KITS", "stock": 85, "prix": 15000},
            {"id": "AS-45", "nom": "Vapor 15 Elite", "cat": "FOOTWEAR", "stock": 12, "prix": 45000},
            {"id": "AS-12", "nom": "Jogging Tech Noir", "cat": "TRAINING", "stock": 40, "prix": 25000},
            {"id": "AS-05", "nom": "Chaussettes Grip", "cat": "ACCESSORIES", "stock": 150, "prix": 5000}
        ]

inv = InventorySystem()

# --- 4. CONTROL PANEL ANIMÉ (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🛰️ SYSTEM MONITORING")
    
    # Bloc Statut Animé
    st.markdown("""
        <div class="status-box">
            <span class="pulse-dot"></span>
            <span style="color:#ffda00; font-weight:bold;">CORE ENGINE: ACTIVE</span><br>
            <small style="color:#888;">Encodage: SSL/JOAL-PROT</small><br>
            <small style="color:#888;">Uptime: 99.9%</small>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Indicateurs de performance
    st.write("📈 CHARGE SERVEUR")
    st.progress(25)
    st.write("📦 FLUX STOCK")
    st.progress(65)
    st.write("💰 REVENU MENSUEL")
    st.progress(88)

    st.divider()
    
    # Navigation Matrix
    menu = st.radio("SÉLECTIONNER INTERFACE", ["🌐 TERMINAL CLIENT", "🔐 ACCÈS ADMIN (ERP)"])
    
    if st.button("🔄 REBOOT SYSTEM"):
        with st.spinner("Synchronisation des données..."):
            time.sleep(2)
            st.success("Base de données rafraîchie !")

# --- 5. INTERFACE CLIENT (FRONT-END) ---
if menu == "🌐 TERMINAL CLIENT":
    st.markdown('<h1 class="glitch-title">AVENIR SPORT</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # Simulation de cartes animées
    for i, item in enumerate(inv.items[:3]):
        with [col1, col2, col3][i]:
            st.markdown(f"""
                <div style="background:rgba(255,255,255,0.05); border:1px solid #333; padding:20px; border-radius:15px; border-bottom: 4px solid #ffda00;">
                    <h3 style="color:#ffda00; font-family:Orbitron;">{item['nom']}</h3>
                    <p style="color:#888; font-size:12px;">UNIT_ID: {item['id']}</p>
                    <p style="font-size:24px; font-weight:bold;">{item['prix']:,} FCFA</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("INITIER COMMANDE", f"https://wa.me/221XXXXXXXXX?text=Code_{item['id']}")

# --- 6. ACCÈS ADMIN (BACK-END COMPLEXE) ---
else:
    st.markdown("<h2 style='color:#ffda00; font-family:Orbitron;'>🛡️ ADMIN CENTRAL COMMAND</h2>", unsafe_allow_html=True)
    
    # Dashboard de statistiques complexes
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("VISITES", "1,240", "+14%")
    c2.metric("COMMANDES", "45", "+5%")
    c3.metric("STOCK TOTAL", "287 pcs", "-2")
    c4.metric("CA JOUR", "245k F", "+18%")

    st.write("### 🗃️ BASE DE DONNÉES TEMPS RÉEL")
    df = pd.DataFrame(inv.items)
    st.dataframe(df, use_container_width=True)
    
    # Zone de modification
    with st.expander("➕ AJOUTER UN NOUVEL ÉQUIPEMENT"):
        st.text_input("Nom de l'article")
        st.number_input("Prix (FCFA)", step=500)
        st.selectbox("Rayon", ["MAILLOTS", "CHAUSSURES", "ACCESSOIRES"])
        st.button("INJECTER DANS LA BASE")

# --- 7. FOOTER XXL ---
st.markdown("""
    <div style="background:#000; padding:80px; margin-top:100px; border-top: 1px solid #ffda00; text-align:center;">
        <p style="color:#ffda00; font-family:Orbitron; letter-spacing:5px;">AVENIR SPORT JOAL - NEXT GEN RETAIL</p>
        <p style="color:#444; font-size:10px;">AUTH_KEY: 8892-X-ASJ | ENCRYPTION: AES-256</p>
    </div>
""", unsafe_allow_html=True)
