
import streamlit as st
import random

# Configuração inicial do aplicativo
st.set_page_config(page_title="Histomatch: Explore o Microcosmo", layout="centered")

# Cabeçalho do jogo
st.title("Histomatch: Explore o Microcosmo")
st.subheader("Teste seus conhecimentos em Histologia e divirta-se aprendendo!")

# Início do jogo
st.write("Responda às perguntas abaixo e descubra o quanto você sabe sobre tecidos e células.")

# Lista de 20 perguntas
questions = [
    {"question": "Qual tecido possui células cilíndricas com microvilosidades e é encontrado no intestino?",
     "options": ["Tecido Epitelial de Revestimento", "Tecido Conjuntivo", "Tecido Muscular", "Tecido Nervoso"],
     "answer": "Tecido Epitelial de Revestimento"},
    {"question": "Qual corante é utilizado para evidenciar fibras colágenas?",
     "options": ["Hematoxilina", "Eosina", "Tricrômico de Masson", "Azul de Toluidina"],
     "answer": "Tricrômico de Masson"},
    {"question": "Qual tecido armazena lipídeos e fornece isolamento térmico?",
     "options": ["Tecido Muscular", "Tecido Adiposo", "Tecido Nervoso", "Tecido Conjuntivo Denso"],
     "answer": "Tecido Adiposo"},
    {"question": "Qual estrutura do tecido epitelial aumenta a absorção no intestino?",
     "options": ["Microvilosidades", "Cílios", "Junções Oclusivas", "Desmossomos"],
     "answer": "Microvilosidades"},
    {"question": "Qual tecido conecta músculos aos ossos?",
     "options": ["Tecido Conjuntivo Denso", "Tecido Adiposo", "Tecido Epitelial", "Tecido Nervoso"],
     "answer": "Tecido Conjuntivo Denso"},
    {"question": "Qual célula é responsável pela produção de melanina?",
     "options": ["Melanócito", "Queratinócito", "Fibroblasto", "Macrófago"],
     "answer": "Melanócito"},
    {"question": "Qual tecido possui fibras elásticas para suportar pressão arterial?",
     "options": ["Tecido Conjuntivo Elástico", "Tecido Adiposo", "Tecido Muscular", "Tecido Nervoso"],
     "answer": "Tecido Conjuntivo Elástico"},
    {"question": "Qual tecido é especializado na condução de impulsos elétricos?",
     "options": ["Tecido Nervoso", "Tecido Muscular", "Tecido Conjuntivo", "Tecido Epitelial"],
     "answer": "Tecido Nervoso"},
    {"question": "Qual tecido muscular possui estriações e é voluntário?",
     "options": ["Muscular Esquelético", "Muscular Liso", "Muscular Cardíaco", "Tecido Epitelial"],
     "answer": "Muscular Esquelético"},
    {"question": "Qual célula está presente no tecido conjuntivo e secreta fibras colágenas?",
     "options": ["Fibroblasto", "Macrófago", "Mastócito", "Adipócito"],
     "answer": "Fibroblasto"},
    {"question": "Qual é o principal tipo de célula do tecido ósseo?",
     "options": ["Osteócito", "Condroblasto", "Fibroblasto", "Adipócito"],
     "answer": "Osteócito"},
    {"question": "Qual estrutura protege o axônio em neurônios?",
     "options": ["Bainha de Mielina", "Dendrito", "Corpo Celular", "Sinapse"],
     "answer": "Bainha de Mielina"},
    {"question": "Qual tecido possui matriz rígida devido a sais de cálcio?",
     "options": ["Tecido Ósseo", "Tecido Cartilaginoso", "Tecido Conjuntivo Denso", "Tecido Epitelial"],
     "answer": "Tecido Ósseo"},
    {"question": "Qual tipo de tecido é encontrado no nariz e ouvido externo?",
     "options": ["Tecido Cartilaginoso", "Tecido Muscular", "Tecido Adiposo", "Tecido Ósseo"],
     "answer": "Tecido Cartilaginoso"},
    {"question": "Qual célula no sangue é responsável pelo transporte de oxigênio?",
     "options": ["Hemácia", "Leucócito", "Plaqueta", "Eosinófilo"],
     "answer": "Hemácia"},
    {"question": "Qual célula participa da coagulação sanguínea?",
     "options": ["Plaqueta", "Hemácia", "Neutrófilo", "Monócito"],
     "answer": "Plaqueta"},
    {"question": "Qual tipo de tecido forma a epiderme?",
     "options": ["Epitélio Estratificado Pavimentoso", "Epitélio Simples Cilíndrico", "Epitélio Cuboide Simples", "Epitélio de Transição"],
     "answer": "Epitélio Estratificado Pavimentoso"},
    {"question": "Qual é a função principal do tecido adiposo marrom?",
     "options": ["Produção de calor", "Armazenamento de energia", "Isolamento térmico", "Proteção contra choques"],
     "answer": "Produção de calor"},
    {"question": "Qual tipo de tecido epitelial reveste os alvéolos pulmonares?",
     "options": ["Epitélio Simples Pavimentoso", "Epitélio Estratificado Cuboide", "Epitélio Cilíndrico", "Epitélio de Transição"],
     "answer": "Epitélio Simples Pavimentoso"},
    {"question": "Qual componente do tecido conjuntivo confere resistência ao estiramento?",
     "options": ["Fibras Colágenas", "Fibras Elásticas", "Fibras Reticulares", "Matriz Amorfa"],
     "answer": "Fibras Colágenas"}
]

# Variável para pontuação
score = 0

# Variável para armazenar respostas dos usuários
user_answers = {}

# Loop para exibir as perguntas
for i, q in enumerate(questions):
    # Embaralhar as opções
    options = q["options"].copy()
    random.shuffle(options)
    
    st.write(f"### Pergunta {i+1}: {q['question']}")
    user_answers[i] = st.radio("", options, key=i)

# Finalizar jogo e calcular pontuação
if st.button("Finalizar jogo"):
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    # Exibir a pontuação final
    st.write(f"### Sua pontuação final: {score}/{len(questions)}")
    if score == len(questions):
        st.balloons()
        st.success("Parabéns! Você acertou todas as perguntas!")
    elif score > len(questions) // 2:
        st.info("Bom trabalho! Continue estudando para aprimorar ainda mais.")
    else:
        st.warning("Não se preocupe, pratique mais para melhorar seu desempenho.")
