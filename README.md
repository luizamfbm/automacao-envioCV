1: 
importação de módulos 
smtplib: Biblioteca para enviar e-mails usando o protocolo SMTP (Simple Mail Transfer Protocol).
MIMEMultipart: Classe para criar mensagens de e-mail que podem conter várias partes, como texto e anexos.
MIMEText: Classe para criar a parte de texto de uma mensagem de e-mail.
MIMEBase: Classe base para criar partes de mensagens com conteúdo binário, como anexos.
encoders: Módulo para codificar partes de uma mensagem em base64, necessário para anexos.
 
2:
Definir a função enviar_email que configura e envia o e-mail.

3: 
Definir o corpo do e-mail em formato HTML. O conteúdo HTML será renderizado quando o e-mail for visualizado em um cliente de e-mail.

4: 
msg = MIMEMultipart(): Cria um objeto de mensagem que pode conter múltiplas partes (texto e anexos).
Define os cabeçalhos do e-mail: From, To, e Subject.
password: É a senha do seu e-mail (ou uma senha de aplicativo se estiver usando autenticação de dois fatores).

5: 
Adicionar o corpo do e-mail à mensagem. MIMEText é usado para especificar que o conteúdo é HTML.

6:
filename: Define o caminho do arquivo PDF que você deseja anexar.
attachment = open(filename, "rb"): Abre o arquivo PDF em modo de leitura binária.
part = MIMEBase('application', 'octet-stream'): Cria uma parte da mensagem para o arquivo anexo.
part.set_payload(attachment.read()): Define o conteúdo da parte como o conteúdo do arquivo PDF.
encoders.encode_base64(part): Codifica o conteúdo do arquivo em base64 para envio.
part.add_header('Content-Disposition', f'attachment; filename={filename}'): Adiciona um cabeçalho que indica que esta parte é um anexo e define o nome do arquivo.
msg.attach(part): Anexa a parte ao e-mail.

7: 
s = smtplib.SMTP('smtp.gmail.com', 587): Conecta-se ao servidor SMTP do Gmail na porta 587.
s.starttls(): Inicia a comunicação segura com o servidor SMTP.
s.login(msg['From'], password): Faz login no servidor SMTP usando o e-mail e a senha fornecidos.
s.sendmail(msg['From'], msg['To'], msg.as_string()): Envia o e-mail. msg.as_string() converte o objeto de mensagem para uma string formatada.
s.quit(): Encerra a conexão com o servidor SMTP.

8:  
Imprime uma mensagem de confirmação no console indicando que o e-mail foi enviado com sucesso.

9:
Chama a função enviar_email para executar o código de envio de e-mail.

Essa estrutura garante que seu e-mail será enviado com um corpo HTML e um anexo PDF, utilizando o servidor SMTP do Gmail.
