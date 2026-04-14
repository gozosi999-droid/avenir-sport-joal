# --- 2. SYSTÈME DE DESIGN "MATRIX-NEURAL" (MAJ ANIMÉE) ---
st.markdown("""
<style>
    /* ... (Garder ton code précédent et ajouter ceci) ... */

    /* ANIMATION : SCANNER LASER */
    @keyframes scanline {
        0% { top: 0%; }
        100% { top: 100%; }
    }

    /* ANIMATION : PULSE DE SÉCURITÉ */
    @keyframes pulse-green {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(46, 204, 113, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(46, 204, 113, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(46, 204, 113, 0); }
    }

    /* STYLE DU PANNEAU LATÉRAL */
    .sidebar-monitor {
        background: rgba(255, 218, 0, 0.05);
        border: 1px solid var(--neon-gold);
        padding: 15px;
        border-radius: 10px;
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
    }

    .sidebar-monitor::after {
        content: "";
        position: absolute;
        width: 100%;
        height: 2px;
        background: var(--neon-gold);
        top: 0;
        left: 0;
        opacity: 0.2;
        animation: scanline 3s linear infinite;
    }

    .status-dot {
        height: 8px; width: 8px;
        background-color: #2ecc71;
        border-radius: 50%;
        display: inline-block;
        margin-right: 5px;
        animation: pulse-green 2s infinite;
    }

    /* JAUGE DE CHARGE ANIMÉE */
    .stProgress > div > div > div > div {
        background-color: var(--neon-gold) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION LÉGALE & CONTROL PANEL ANIMÉ ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-monitor">
            <h4 style="margin:0; color:#ffda00; font-family:'Orbitron'; font-size:14px;">📡 SYSTEM MONITOR</h4>
            <hr style="margin:10px 0; border-color:rgba(255,218,0,0.2);">
            <p style="font-size:11px; margin:0;"><span class="status-dot"></span> CONNECTION: SECURE</p>
            <p style="font-size:11px; margin:0;">🛰️ NODE: JOAL-MAIN-01</p>
            <p style="font-size:11px; margin:0;">🔒 ENCRYPTION: AES-256</p>
        </div>
    """, unsafe_allow_html=True)

    # Statistiques de performance "Live"
    st.write("🔧 **CHARGE DU SERVEUR**")
    st.progress(25) # Simulation de charge
    
    st.write("📦 **FLUX DE STOCK (Live)**")
    st.progress(65)

    st.divider()
    
    # Sélecteur de mode avec icônes
    view_mode = st.radio(
        "⚡ SÉLECTIONNER INTERFACE",
        ["🌐 Catalogue Client", "🔐 Gestion Stock (ERP)"],
        index=0
    )

    if st.button("🔄 RE-SYNC DATABASE"):
        with st.spinner("Synchronisation neuronale en cours..."):
            import time
            time.sleep(1.5)
            st.success("DATA SYNC COMPLETE")

    st.divider()
    st.markdown("<p style='font-size:10px; opacity:0.5;'>LOG_ID: " + datetime.now().strftime("%H%M%S") + "</p>", unsafe_allow_html=True)
