import streamlit as st

# Função para a página inicial


def home():
    st.title("Bem-vindo ao meu Portfólio!")
    st.write("""
    Olá! Sou um Analista de Dados com experiência em análise exploratória, visualização de dados,
    machine learning e inteligência artificial. Este site foi feito com Streamlit para apresentar
    meus projetos e compartilhar conteúdos que venho produzindo.
    """)
    st.image("minha_foto.jpg", width=200, caption="Seu Nome")

# Função para a página de portfólio


def portfolio():
    st.title("Portfólio de Projetos")
    st.write("Aqui estão alguns dos meus projetos em ciência de dados:")

    projetos = [
        {
            "titulo": "Análise de Vendas com Python",
            "descricao": "Dashboard interativo com Streamlit para análise de dados de vendas.",
            "link": "https://github.com/seuusuario/projeto-vendas"
        },
        {
            "titulo": "Predição de Preços de Imóveis",
            "descricao": "Modelo de machine learning para prever preços com base em características dos imóveis.",
            "link": "https://github.com/seuusuario/projeto-imoveis"
        },
        {
            "titulo": "Web Scraping de Dados Econômicos",
            "descricao": "Extração automatizada de indicadores do IBGE e Banco Central.",
            "link": "https://github.com/seuusuario/projeto-scraping"
        }
    ]

    for projeto in projetos:
        st.subheader(projeto["titulo"])
        st.write(projeto["descricao"])
        st.markdown(f"[Ver no GitHub]({projeto['link']})")

# Função para a página de publicações


def publicacoes():
    st.title("Publicações")

    posts = [
        {
            "titulo": "Como organizar um projeto de ciência de dados",
            "conteudo": "Neste artigo explico boas práticas para organizar pastas, scripts e notebooks..."
        },
        {
            "titulo": "Introdução à Análise Exploratória de Dados",
            "conteudo": "Veja como iniciar uma análise exploratória com Pandas, Matplotlib e Seaborn..."
        },
        {
            "titulo": "Streamlit: criando dashboards com Python",
            "conteudo": "Aprenda como criar interfaces interativas para seus projetos com Streamlit."
        }
    ]

    for post in posts:
        st.subheader(post["titulo"])
        st.write(post["conteudo"])
        st.markdown("---")


# Menu lateral
menu = st.sidebar.radio("Navegação", ["Início", "Portfólio", "Publicações"])

# Exibição de acordo com o menu
if menu == "Início":
    home()
elif menu == "Portfólio":
    portfolio()
elif menu == "Publicações":
    publicacoes()
