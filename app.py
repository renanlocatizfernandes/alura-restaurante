from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','Gourmet')
restaurante_praca.receber_avaliacao('Renan', 10)
restaurante_praca.receber_avaliacao('Caio', 8)
restaurante_praca.receber_avaliacao('Gui', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()