class Tv:
    def __init__(self, volume):
        self.__volume = volume
        #self.__lista_de_canais = ['nada', 'Globo', 'Rede tv', 'Record', 'Band', 'Tv Jovem', 'Tv Cultura']
        self.__lista_de_canais = [{'canal 0':'nada', 'canal 1':'Globo', 'canal 2':'Rede Tv', 'canal 3':'Record', 'canal 4':'Band', 'canal 5':'Tv Jovem', 'canal 6': 'Tv Cultura'}]

        self.__mudar = 'Canal 0'
        self.__canal_atual = 'Nada'

    def Mudar_de_canal(self):
        print('-' * 66)
        for i in self.__lista_de_canais:
            for c in i.keys():
                print(c)
        temp = str(input('Deseja qual canal: ')).strip().lower()
        print('-' * 66)
        for i in self.__lista_de_canais:
            for c, tv in i.items():
                if c == temp:
                    self.__mudar = c
                    self.__canal_atual = tv
            print(f'Mudança feita, agora você está no canal {self.__mudar}')

    def get_info(self):
        print('-' * 66)
        print(f'Tv: {self.__canal_atual}\nVolume: {self.__volume}')
        print('-' * 66)

pessoa1 = Tv(20)
pessoa1.get_info()
pessoa1.Mudar_de_canal()
pessoa1.get_info()






