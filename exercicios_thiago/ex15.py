class Mensagem:

    def enviar(self, conteudo=None, destinatario="Desconhecido"):

        if isinstance(conteudo, str):

            print(f"Enviando mensagem de texto para {destinatario}: {conteudo}")

        elif isinstance(conteudo, int):

            print(f"Enviando número para {destinatario}: {conteudo}")

        else:

            print(f"Nada para enviar a {destinatario}")