# Funções do dia a dia
#exercicio 1
def formatar_saudacao(nome:str, cidade:str):
    return f"ola {nome},seja bem vindo(a)a{cidade}"

# Exercicio 2


# exercicio 3  
def fahrenheit_para_celsius(temp_f:float):
    temp_celsius=(temp_f-32)*(5/9) 
    return temp_celsius

# exercicios 4
def calcular_gorjeta_por_pessoa(conta:float,porcentagem_gorjeta:float,pessoas:int):
    gorjeta = conta * (porcentagem_gorjeta/100) / pessoas 
    return gorjeta
                                      
# exercicio 5
def resusmo_circulo(raio:float):
    pi=3.14159
    area=pi*(raio**2)
    return f" um circulo de raio{raio}tem area de {area:.2f}"

#exercicios 6 
def resumo_juros_basicos(capital:float,taxa:float):
    pass

if __name__ == "__main__":
    saudacao = formatar_saudacao("alice","porto alegre")
    print(saudacao)

    temperatura = fahrenheit_para_celsius(30)
    print(temperatura)

def # exercicios 7
metricas_cilindro (2.0,5.0)




                                                            