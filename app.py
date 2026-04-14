import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- 1. CONFIGURATION DU NOYAU (NETTOYÉ) ---
st.set_page_config(
    page_title="AVENIR SPORT | NEURAL INTERFACE",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. MOTEUR DE DESIGN "CYBER-GOLD" (CSS TOTALEMENT NETTOYÉ) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&family=Inter:wght@300;400;700&display=swap');

    :root {
        --neon-gold: #ffda00;
        --dark-bg: #030303;
    }

    .stApp {
        background-color: var(--dark-bg);
        background-image: 
            linear-gradient(rgba(255, 218, 0, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 218, 0, 0.02) 1px, transparent 1px);
        background-size: 40px 40px;
    }

    @keyframes scanline { 0% { top: 0%; } 100% { top: 100%; } }
    @keyframes pulse-green { 0% { opacity: 0.4; } 50% { opacity: 1; } 100% { opacity: 0.4; } }

    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(40px, 8vw, 100px) !important;
        font-weight: 900;
        color: var(--neon-gold);
        text-align: center;
        letter-spacing: 12px;
        text-shadow: 0 0 20px rgba(255, 218, 0, 0.4);
        margin: 0;
        padding: 20px 0;
    }

    .sidebar-monitor {
        background: rgba(255, 218, 0, 0.05);
        border: 1px solid var(--neon-gold);
        padding: 15px;
        border-radius: 12px;
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
        font-family: 'Share Tech Mono', monospace;
    }

    .sidebar-monitor::after {
        content: "";
        position: absolute; width: 100%; height: 2px;
        background: var(--neon-gold); top: 0; left: 0;
        opacity: 0.2; animation: scanline 4s linear infinite;
    }

    .status-dot {
        height: 8px; width: 8px; background: #2ecc71;
        border-radius: 50%; display: inline-block;
        animation: pulse-green 1s infinite;
    }

    .product-box {
        background: #0a0a0a;
        border: 1px solid #222;
        border-radius: 20px;
        padding: 0;
        overflow: hidden;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .product-box:hover {
        border-color: var(--neon-gold);
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.8);
    }

    .price-cyber {
        font-family: 'Orbitron';
        color: var(--neon-gold);
        font-size: 24px;
        font-weight: 900;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SYSTÈME DE DONNÉES ---
class AvenirSystem:
    def __init__(self):
        self.data = {
            "ELITE MAILLOTS": [
                {"id": 101, "nom": "Sénégal Home Kit 2024", "prix": 15000, "genre": "Unisexe", "desc": "Qualité Thaïlande AAA - Dri-FIT", "img": "https://images.unsplash.com/photo-1599408162161-08249033327d?w=600"},
                {"id": 102, "nom": "Real Madrid Home Edition", "prix": 18500, "genre": "Homme", "desc": "Patchs UCL inclus - Tissu Premium", "img": "https://images.unsplash.com/photo-1620055375841-f5186b97771e?w=600"},
                {"id": 103, "nom": "Ensemble Training Pro", "prix": 25000, "genre": "Unisexe", "desc": "Veste + Pantalon - Slim Fit", "img": "https://images.unsplash.com/photo-1552664688-cf412ec27db2?w=600"},
            ],
            "FOOTWEAR TECH": [
                {"id": 201, "nom": "Nike Mercurial Vapor 15", "prix": 45000, "genre": "Homme", "desc": "Crampons multi-terrains FG/MG", "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600"},
                {"id": 202, "nom": "Adidas Predator Acc.", "prix": 42000, "genre": "Unisexe", "desc": "Zone Skin Grip - Précision Max", "img": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=600"},
            ],
            "ACCESSOIRES & DIVERS": [
                {"id": 301, "nom": "Protège-Tibias Carbon-X", "prix": 9500, "genre": "Unisexe", "desc": "Ultra-léger - Protection Impact", "img": "https://images.unsplash.com/photo-1511886929837-399a8a11bdca?w=600"},
                {"id": 302, "nom": "Chaussettes Grip Pro", "prix": 5000, "genre": "Unisexe", "desc": "Antidérapant Haute Densité", "img": "https://images.unsplash.com/photo-1586350977771-b3b0abd50c82?w=600"},
            ]
        }

sys = AvenirSystem()

# --- 4. CONTROL PANEL ANIMÉ (SIDEBAR) ---
with st.sidebar:
    st.markdown("""
        <div class="sidebar-monitor">
            <h3 style="color:#ffda00; margin:0; font-size:16px;">🛰️ CONTROL PANEL</h3>
            <hr style="border-color:rgba(255,218,0,0.2); margin:10px 0;">
            <p style="font-size:12px; margin:0;"><span class="status-dot"></span> SYSTEM_STATUS: ONLINE</p>
            <p style="font-size:11px; opacity:0.
