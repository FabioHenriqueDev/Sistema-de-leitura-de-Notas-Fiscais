# Sistema-de-leitura-de-Notas-Fiscais

# 📄 Sistema de Leitura de Notas Fiscais em XML (Danfe)

Este projeto é uma aplicação web interativa desenvolvida com **Streamlit** para leitura e análise de **notas fiscais eletrônicas (NF-e)** no formato **XML do padrão Danfe**.

---

## 🚀 Funcionalidades

✅ Interface gráfica simples e intuitiva  
✅ Upload de arquivos XML de notas fiscais  
✅ Geração de tabela com os dados da nota  
✅ Download automático da tabela em **formato CSV**  
✅ Envio automático da tabela por **e-mail** para o usuário  

---

## 🖼️ Interface do sistema

- O usuário faz upload do arquivo XML da nota fiscal
- Os dados da nota (CNPJ, CPF, produtos, valores etc.) são extraídos e exibidos em uma tabela
- É possível baixar essa tabela como `.csv` para celular ou computador
- Um campo permite informar o e-mail para o envio automático do arquivo CSV

---

## 📬 Envio de e-mail automático

- Após o upload e visualização da nota, o usuário pode inserir seu e-mail
- Ao clicar no botão **"Enviar e-mail"**, o sistema envia automaticamente o CSV como anexo com os dados extraídos da nota fiscal

---

## 🛠️ Tecnologias utilizadas

- [Python 3.13](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [xmltodict](https://github.com/martinblech/xmltodict)
- `smtplib` + `email.mime` (para envio de e-mails)

---

## 📦 Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-projeto.git
