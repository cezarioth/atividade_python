class Seguranca:

    def __init__(self):

        pass

    def __criptografar_mensagem(self, mensagem: str) -> str:

        return f"Mensagem protegida: {mensagem[::-1]}" 

    def exibir_mensagem(self, mensagem: str):

        return self.__criptografar_mensagem(mensagem)