import streamlit as st
import random
from datetime import datetime, timedelta

# === CONFIGURACIÓN ===
st.set_page_config(page_title="🗃️Centro ERSI", layout="centered")

# === THEME CSS ===
def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
        }

        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        .block-container {
            padding-top: 0 !important;
            padding-bottom: 80px !important;
            max-width: 520px !important;
        }

        /* === Header banners === */
        .login-header {
            background: linear-gradient(135deg, #185FA5, #0C447C);
            padding: 48px 24px 32px;
            border-radius: 0 0 24px 24px;
            margin: -1rem -1rem 28px -1rem;
            text-align: center;
            color: white;
        }
        .app-header {
            background: linear-gradient(135deg, #185FA5, #0C447C);
            padding: 32px 24px 24px;
            border-radius: 0 0 20px 20px;
            margin: -1rem -1rem 24px -1rem;
            text-align: center;
            color: white;
        }
        .login-header .logo-circle,
        .app-header .logo-circle {
            width: 60px; height: 60px;
            border-radius: 50%;
            background: rgba(255,255,255,0.18);
            display: inline-flex; align-items: center; justify-content: center;
            font-size: 22px; font-weight: 700; color: white;
            margin-bottom: 10px;
        }
        .login-header h1, .app-header h1 {
            margin: 0; font-size: 22px; font-weight: 600; color: white !important;
        }
        .login-header p, .app-header p {
            margin: 4px 0 0; font-size: 13px; color: rgba(255,255,255,0.7);
        }

        /* === Inputs === */
        .stTextInput > div > div > input {
            border-radius: 10px !important;
            border: 1.5px solid #e0e4ea !important;
            padding: 10px 14px !important;
            font-size: 14px !important;
            transition: border-color 0.2s;
        }
        .stTextInput > div > div > input:focus {
            border-color: #185FA5 !important;
            box-shadow: 0 0 0 2px rgba(24,95,165,0.12) !important;
        }
        .stTextInput label, .stSelectbox label {
            font-size: 13px !important;
            font-weight: 500 !important;
            color: #6b7280 !important;
        }
        .stSelectbox > div > div {
            border-radius: 10px !important;
            border: 1.5px solid #e0e4ea !important;
        }

        /* === Primary button === */
        .stButton > button {
            background: linear-gradient(135deg, #185FA5, #1a6fc2) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 10px 24px !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(24,95,165,0.18);
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #1a6fc2, #185FA5) !important;
            box-shadow: 0 4px 14px rgba(24,95,165,0.28) !important;
            transform: translateY(-1px);
        }

        /* === Form submit === */
        .stFormSubmitButton > button {
            background: linear-gradient(135deg, #185FA5, #1a6fc2) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            width: 100% !important;
            box-shadow: 0 2px 8px rgba(24,95,165,0.18);
        }

        /* === Download button === */
        .stDownloadButton > button {
            background: transparent !important;
            color: #185FA5 !important;
            border: 1.5px solid #185FA540 !important;
            box-shadow: none !important;
        }
        .stDownloadButton > button:hover {
            background: #E6F1FB !important;
            border-color: #185FA5 !important;
            box-shadow: none !important;
        }

        /* === Logout === */
        .logout-btn button {
            background: transparent !important;
            color: #dc3545 !important;
            border: 1.5px solid #dc354540 !important;
            box-shadow: none !important;
        }
        .logout-btn button:hover {
            background: #dc354510 !important;
            border-color: #dc3545 !important;
            box-shadow: none !important;
        }

        /* === Welcome badge === */
        .welcome-badge {
            display: inline-flex; align-items: center; gap: 8px;
            background: #E6F1FB;
            border-radius: 24px;
            padding: 8px 16px;
            font-size: 13px; font-weight: 500;
            color: #0C447C;
            margin-bottom: 20px;
        }
        .welcome-badge .dot {
            width: 8px; height: 8px;
            border-radius: 50%;
            background: #185FA5;
        }

        /* === Section label === */
        .section-label {
            font-size: 12px;
            font-weight: 600;
            color: #9ca3af;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 12px;
        }

        /* === Code result === */
        .code-result {
            background: #E6F1FB;
            border-radius: 12px;
            padding: 16px;
            text-align: center;
            font-family: 'DM Mono', monospace;
            font-size: 18px;
            font-weight: 600;
            color: #0C447C;
            border: 1.5px solid #B5D4F4;
            margin: 12px 0;
        }

        /* === Alerts === */
        .stAlert { border-radius: 10px !important; }
        .stDataFrame { border-radius: 12px !important; overflow: hidden; }

        /* === Footer === */
        .custom-footer {
            position: fixed;
            left: 0; bottom: 0;
            width: 100%;
            background: rgba(255,255,255,0.95);
            border-top: 1px solid #e8ecf1;
            padding: 10px 18px;
            text-align: center;
            font-size: 11px;
            color: #9ca3af;
            z-index: 9999;
            backdrop-filter: blur(8px);
        }
        .custom-footer b { color: #374151; }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

def render_footer():
    year = datetime.now().year
    st.markdown(
        f'<div class="custom-footer">© {year} <b>Proyecto VIHCA</b> — Generador de códigos ERSI v1.2.0</div>',
        unsafe_allow_html=True,
    )

render_footer()


# === USUARIOS CON PAÍS ASIGNADO ===
USUARIOS_VALIDOS = {
    "admin_user": {"clave": "admin1589" , "pais" : "todos"},
    "honduras_user": {"clave": "8585", "pais": "Honduras"},
    "copan_user" : {"clave": "copan123", "pais": "Honduras"},
    "colon_user" : {"clave": "colon123", "pais": "Honduras"},
    "paraiso_user" : {"clave": "paraiso123", "pais": "Honduras"},
    "atlantida_user" : {"clave": "atlantida123", "pais": "Honduras"},
    "guatemala_user": {"clave": "5656", "pais": "Guatemala"},
    "guate_user_001": {"clave": "guateuser123", "pais": "Guatemala"},
    "guate_user_002": {"clave": "guateuser234", "pais": "Guatemala"},
    "guate_user_003": {"clave": "guateuser567", "pais": "Guatemala"},
    "guate_user_004": {"clave": "guateuser891", "pais": "Guatemala"},
    "guate_user_005": {"clave": "guateuser765", "pais": "Guatemala"},
    "panama_user": {"clave": "9595", "pais": "Panamá"},
    "ahuachapan_user": {"clave": "3847", "pais": "El Salvador"},
    "sonsonate_user": {"clave": "4629", "pais": "El Salvador"},
    "santa_ana_user": {"clave": "6492", "pais": "El Salvador"},
    "la_libertad_user": {"clave": "5186", "pais": "El Salvador"},
    "san_salvador_user": {"clave": "4762", "pais": "El Salvador"},
    "cuscatlan_user": {"clave": "5724", "pais": "El Salvador"},
    "la_paz_user": {"clave": "9472", "pais": "El Salvador"},
    "san_vicente_user": {"clave": "6249", "pais": "El Salvador"},
    "san_miguel_user": {"clave": "4517", "pais": "El Salvador"},
    "la_union_user": {"clave": "2194", "pais": "El Salvador"},
    "usulutan_user": {"clave": "8926", "pais": "El Salvador"},
    "nicaragua_user": {"clave": "7575", "pais": "Nicaragua"}
}

if "descargado" not in st.session_state:
    st.session_state.descargado = False
if "registro" in st.session_state and st.session_state["registro"]:
    st.warning("⚠️ Debe descargar la tabla virtual antes de cerrar sesión si ha generado códigos.")

# === SESIÓN ===
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "verificado" not in st.session_state:
    st.session_state.verificado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""
if "pais_usuario" not in st.session_state:
    st.session_state.pais_usuario = ""
if "codigo_verificacion" not in st.session_state:
    st.session_state.codigo_verificacion = None

# === LOGIN ===
if not st.session_state.logueado:
    st.markdown("""
        <div class="login-header">
            <div class="logo-circle">V</div>
            <h1>Centro ERSI</h1>
            <p>Proyecto VIHCA</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="font-size:18px; font-weight:600; margin-bottom:2px;">Iniciar sesión</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:13px; color:#6b7280; margin-bottom:18px;">Ingrese sus credenciales para continuar</p>', unsafe_allow_html=True)

    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    login = st.button("Ingresar")

    if login:
        if usuario in USUARIOS_VALIDOS and clave == USUARIOS_VALIDOS[usuario]["clave"]:
            codigo = str(random.randint(1000, 9999))
            st.session_state.codigo_verificacion = codigo
            st.session_state.usuario = usuario
            st.session_state.pais_usuario = USUARIOS_VALIDOS[usuario]["pais"]
            st.session_state.logueado = True
            st.session_state.verificado = False
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos.")

# === VERIFICACIÓN POR CÓDIGO ===
elif st.session_state.logueado and not st.session_state.verificado:
    st.markdown("""
        <div class="app-header">
            <div class="logo-circle">🔐</div>
            <h1>Verificación</h1>
            <p>Paso adicional de seguridad</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="font-size:14px; color:#6b7280; margin-bottom:14px;">Ingrese el siguiente código para continuar:</p>', unsafe_allow_html=True)
    st.code(st.session_state.codigo_verificacion, language="bash")
    codigo_ingresado = st.text_input("Código de verificación", max_chars=4)

    if st.button("Verificar"):
        if codigo_ingresado == st.session_state.codigo_verificacion:
            st.session_state.verificado = True
            st.rerun()
        else:
            st.error("Código incorrecto.")

# === CONTENIDO DE LA APP ===
elif st.session_state.verificado:
    st.markdown("""
        <div class="app-header">
            <div class="logo-circle">V</div>
            <h1>Bienvenido</h1>
            <p>Panel de herramientas</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="welcome-badge"><span class="dot"></span> {st.session_state.usuario}</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Herramientas</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧾 Generar Código ERSI"):
            st.switch_page("pages/1_Generador_Código_ERSI.py")
    with col2:
        if st.button("🔐 Generar Código QR"):
            st.switch_page("pages/2_Generador_Código_QR.py")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    if st.button("Cerrar sesión"):
        if "registro" in st.session_state and st.session_state["registro"] and not st.session_state.descargado:
            st.error("❌ Primero debes descargar la tabla virtual antes de cerrar sesión.")
        else:
            st.session_state.clear()
            st.rerun()
