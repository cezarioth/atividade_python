class Matematica:
    @staticmethod
    def e_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

print(Matematica.e_primo(2))
print(Matematica.e_primo(7))
print(Matematica.e_primo(10))
print(Matematica.e_primo(17))
print(Matematica.e_primo(1))