import streamlit as st
import base64

# --- FONCTION TECHNIQUE POUR LE FOND D'ÉCRAN ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}
    
    /* On rend les textes plus lisibles sur le fond */
    h1, h2, h3, p {{
        color: white;
        text-shadow: 2px 2px 4px #000000;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- CONFIGURATION ---
st.set_page_config(page_title="Avenir Sport Joal", layout="wide")

# Appliquer le fond (REMPLACE "fond.jpg" PAR LE NOM DE TON IMAGE)
try:
    set_png_as_page_bg('fond.jpg')
except:
    st.warning("L'image de fond n'a pas été trouvée sur GitHub.")

# --- LE RESTE DE TON CODE (LOGO, TITRE, WHATSAPP) ---
st.image("logo.png", width=150)
st.title("🦁 AVENIR SPORT JOAL")

# Configuration de la page
st.set_page_config(page_title="Avenir Sport Joal", page_icon="⚽", layout="wide")

# --- AFFICHAGE DU LOGO ET DU TITRE ---
# On crée deux colonnes : une petite pour le logo, une grande pour le titre
col_logo, col_titre = st.columns([1, 4])

with col_logo:
    # REMPLACE "logo.png" PAR LE NOM EXACT DE TON FICHIER SUR GITHUB
    st.image("logo.png", width=150) 

with col_titre:
    st.markdown("<h1 style='margin-top: 20px;'>🦁 AVENIR SPORT JOAL</h1>", unsafe_allow_html=True)
    st.write("Le meilleur de l'équipement sportif à Joal-Fadiouth")

st.write("---")

# ... (Le reste de ton code avec les produits et les boutons WhatsApp)
# --- TON NUMÉRO WHATSAPP ---
mon_numero = "221770953766" # REMPLACE PAR TON VRAI NUMÉRO (ex: 221771234567)

# --- STYLE CSS ---
st.markdown("""
    <style>
    .price-tag {
        background-color: #ffda00;
        color: black;
        font-weight: bold;
        font-size: 20px;
        padding: 5px 15px;
        border-radius: 5px;
        display: inline-block;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #25D366; /* Vert WhatsApp */
        color: white;
        border-radius: 5px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #128C7E;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE ---
st.markdown("<h1 style='text-align: center;'>🦁 AVENIR SPORT JOAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Cliquez sur un article pour commander directement sur WhatsApp</p>", unsafe_allow_html=True)
st.write("---")

# --- GRILLE DE PRODUITS ---
col1, col2, col3, col4, col5 = st.columns(5)

# Fonction pour créer le lien WhatsApp proprement
def lien_whatsapp(produit):
    message = f"Bonjour Avenir Sport Joal, je suis intéressé par l'article : {produit}"
    return f"https://wa.me/{mon_numero}?text={message.replace(' ', '%20')}"

# Produit 1
with col1:
    st.image("https://via.placeholder.com/200x200.png?text=Chaussure+Reebok")
    st.write("**Reebok Runner**")
    st.markdown('<div class="price-tag">29.900 F</div>', unsafe_allow_html=True)
    st.link_button("🛍️ Commander", lien_whatsapp("Reebok Runner 3.0"))

# Produit 2
with col2:
    st.image("https://via.placeholder.com/200x200.png?text=Maillot+Lazio")
    st.write("**Maillot Lazio**")
    st.markdown('<div class="price-tag">23.500 F</div>', unsafe_allow_html=True)
    st.link_button("🛍️ Commander", lien_whatsapp("Maillot Lazio Macron"))

# Produit 3
with col3:
    st.image("https://via.placeholder.com/200x200.png?text=Ballon+Adidas")
    st.write("**Ballon Adidas**")
    st.markdown('<div class="price-tag">6.500 F</div>', unsafe_allow_html=True)
    st.link_button("🛍️ Commander", lien_whatsapp("Ballon Adidas EPP"))

# Produit 4
with col4:
    st.image("https://via.placeholder.com/200x200.png?text=Maillot+Verone")
    st.write("**Maillot Vérone**")
    st.markdown('<div class="price-tag">19.900 F</div>', unsafe_allow_html=True)
    st.link_button("🛍️ Commander", lien_whatsapp("Maillot Hellas Verone"))

# Produit 5
with col5:
    st.image("https://via.placeholder.com/200x200.png?text=Sneakers+Enfant")
    st.write("**Adidas Hoops**")
    st.markdown('<div class="price-tag">19.900 F</div>', unsafe_allow_html=True)
    st.link_button("🛍️ Commander", lien_whatsapp("Adidas Hoops Enfant"))

st.write("---")
st.info("📍 Boutique située à Joal-Fadiouth. Livraison possible !")

