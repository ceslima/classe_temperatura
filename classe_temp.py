class ConversorTemperatura:
    """
    Classe que converte temperaturas de Celsius para Fahrenheit.
    """

    def celsius_para_fahrenheit(self, celsius: float) -> float:
        """
        Converte uma temperatura de Celsius para Fahrenheit.

        Args:
            celsius: A temperatura em graus Celsius.

        Returns:
            A temperatura convertida em graus Fahrenheit.
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit


# Entrada de dados
celsius = float(input())

# Cria uma instância da classe ConversorTemperatura
conversor = ConversorTemperatura()

# Realiza a conversão e imprime o resultado
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)
