import streamlit as st
from leitor_xml import ler_xml_danfe
import pandas as pd
import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def app():
    load_dotenv()
    st.header('Sistema de Leitura XML', divider=True)
    st.markdown('#### Adicione Notas Fiscais do padrão Danfe')
    arquivo = st.file_uploader("Selecione Notas Fiscais do padrão XML da Danfe", type=['xml'])

    try:
        if arquivo:
            dicionario = ler_xml_danfe(arquivo)
            df = pd.DataFrame.from_dict(dicionario)
            st.write('Tabela gerada com sucesso:')
            st.dataframe(df)
            enviar_email = st.text_input('Escreva seu email para enviar as informações da nota fiscal')
            
            if st.button('Clique aqui para receber o email'):
                html_df = df.to_html()
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                sender_email = os.environ["email"]
                sender_password = os.environ["senha_app"]

                # Compondo o e-mail
                msg = MIMEMultipart()
                msg['Subject'] = 'Parabéns! Você foi aprovado na nossa escola!'
                msg['From'] = sender_email
                msg['To'] = enviar_email

                html = f"""
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <style>
                            table {{
                                width: 100%;
                                border-collapse: collapse;
                                font-size: 14px;
                            }}
                            th, td {{
                                border: 1px solid #dddddd;
                                text-align: left;
                                padding: 8px;
                            }}
                            th {{
                                background-color: #f2f2f2;
                            }}
                            @media only screen and (max-width: 600px) {{
                                body {{
                                font-size: 16px;
                                }}
                                table {{
                                font-size: 16px;
                                }}
                                h3 {{
                                font-size: 20px;
                                }}
                            }}
                        </style>
                    </head>
                    <body style="font-family: Arial, sans-serif; margin: 0; padding: 20px;">
                        <h3 style="color: #333;">Segue o relatório da Nota Fiscal:</h3>
                        {html_df}
                    </body>
                    </html>
                """

                msg.attach(MIMEText(html, 'html'))

                try:
                    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
                        smtp.starttls()
                        smtp.login(sender_email, sender_password)
                        smtp.send_message(msg)
                        st.success('Email enviado com sucesso!')
                except:
                    st.warning('Erro ao envio do email.')
    except:
        st.error("Não foi possível ler sua Nota Fiscal.")
        st.error("Verifique se sua nota tem o padrão da Danfe.")


if __name__ == '__main__':
    app()