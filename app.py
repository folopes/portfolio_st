import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Configuração da página
st.set_page_config(
    page_title="Fabiano Lopes - Portfólio de Dados",
    page_icon="🧠",
    layout="wide"
)

# Função para converter imagem local para base64


def image_to_base64(img_path):
    img = Image.open(img_path)
    buffered = BytesIO()

    ext = img_path.split(".")[-1].upper()
    if ext in ["JPG", "JPEG"]:
        if img.mode == "RGBA":
            img = img.convert("RGB")
        img.save(buffered, format="JPEG")
    else:
        img.save(buffered, format=ext)

    return base64.b64encode(buffered.getvalue()).decode()


# Menu lateral
menu = st.sidebar.radio("📁 Navegação", ["Início", "Portfólio", "Publicações"])

# Página: Início
if menu == "Início":

    # Nome
    # Descrição profissional
    st.markdown("""
    <div style='text-align: center; font-size: 38px; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto;'>
        Fabiano Lopes</div>
    """, unsafe_allow_html=True)

    # Imagem de perfil
    img_base64 = image_to_base64("images/fabiano.jpg")

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-top: 30px;">
            <img src="data:image/jpeg;base64,{img_base64}"
                style="border-radius: 50%; width: 130px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Descrição profissional
    st.markdown("""
    <div style='text-align: justify; font-size: 18px; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto;'>
        Analista de Dados Sênior com mais de 25 anos de experiência no setor de tecnologia, especializado em desenvolvimento de sistemas, administração de bancos de dados (SQL Server) e análise de dados.
        Especialista em ferramentas ETL como Alteryx e AWS Glue, bem como em ferramentas de visualização de dados como Tableau e Power BI.
        Domínio de SQL, Python, serviços AWS (S3, Glue, Athena) e SAS. Certificação AWS Cloud Practitioner.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("##", unsafe_allow_html=True)

    # Ícones personalizados
    linkedin_icon = image_to_base64("images/linkedin.jpeg")
    github_icon = image_to_base64("images/github.png")
    substack_icon = image_to_base64("images/substack.png")

    st.markdown(f"""
    <div style='text-align: center; font-size: 22px;'>
        <a href='https://www.linkedin.com/in/fabiano-lopes79/' target='_blank' style='margin: 0 15px;'>
            <img src='data:image/png;base64,{linkedin_icon}' width='32' style='vertical-align: middle;'></a>
        <a href='https://github.com/folopes' target='_blank' style='margin: 0 15px;'>
            <img src='data:image/png;base64,{github_icon}' width='32' style='vertical-align: middle;'></a>
        <a href='https://folopes.substack.com' target='_blank' style='margin: 0 15px;'>
            <img src='data:image/png;base64,{substack_icon}' width='32' style='vertical-align: middle;'></a>
    </div>
    """, unsafe_allow_html=True)

# Página: Portfólio
elif menu == "Portfólio":
    st.title("📊 Meu Portfólio")
    st.markdown(
        "Aqui você verá os principais projetos que desenvolvi como analista de dados.")
    st.markdown("- Projeto 1: Análise de Vendas com Python e Power BI")
    st.markdown("- Projeto 2: Dashboard de Consumo Energético em Streamlit")
    st.markdown("- Projeto 3: Web Scraping de Preços com BeautifulSoup")

# Página: Publicações
elif menu == "Publicações":
    st.title("📝 Publicações")
    st.markdown(
        "Artigos, reflexões e conteúdos sobre tecnologia, dados e carreira.")
    st.markdown(
        "- [Como usar Streamlit para criar um portfólio de dados](https://folopes.substack.com)")
    st.markdown(
        "- [Automatizando relatórios com Python e Pandas](https://folopes.substack.com)")
