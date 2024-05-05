import heapq

class Carro:
    def __init__(self, id_carro, desgaste_pneus, nivel_combustivel, posicao_corrida, tipo_acidente=None):
        self.id_carro = id_carro
        self.desgaste_pneus = desgaste_pneus
        self.nivel_combustivel = nivel_combustivel
        self.posicao_corrida = posicao_corrida
        self.tipo_acidente = tipo_acidente

    def __lt__(self, outra):
        return self.prioridade() < outra.prioridade()

    def prioridade(self):
        w1, w2, w3 = 0.5, 0.5, 0.1
        return w1 * self.desgaste_pneus + w2 * (1 - self.nivel_combustivel / 100) + w3 * (1 / self.posicao_corrida)

def pit_stop_schedule(carros):
    heap = []
    acidentes_graves = []
    for carro in carros:
        if carro.tipo_acidente == "F":
            acidentes_graves.append(carro)
            continue
        elif carro.tipo_acidente == "P":
            carro.desgaste_pneus += 0.4
            carro.nivel_combustivel *= 0.8
        elif carro.tipo_acidente == "L":
            carro.desgaste_pneus += 0.2
        heapq.heappush(heap, carro)
    schedule = []
    while heap:
        carro = heapq.heappop(heap)
        schedule.append(carro.id_carro)
    return schedule, acidentes_graves

dados_carros_usuario = []

for i in range(3):
    id_carro = input(f"Digite o nome do {i+1}º carro: ")
    desgaste_pneus = float(input(f"Digite o nível de desgaste dos pneus (entre 0 e 1) do {i+1}º carro: ").replace(",", "."))
    nivel_combustivel = int(input("Digite o nível de combustível (entre 0 e 100): "))
    posicao_corrida = int(input(f"Digite a posição na corrida  do {i+1}º (entre 1 a 20): "))
    tipo_acidente_input = input(f"Digite o tipo de acidente do {i+1}º carro (F, P, L ou deixe em branco): ").upper()
    tipo_acidente = None
    if tipo_acidente_input in ["F", "P", "L"]:
        tipo_acidente = tipo_acidente_input
    car = Carro(id_carro, desgaste_pneus, nivel_combustivel, posicao_corrida, tipo_acidente)
    dados_carros_usuario.append(car)

dados_carros_constantes = [
    ("Hamilton", 0, 100, 20),
    ("Bottas", 0.7, 45, 2),
    ("Jimmy", 0.5, 60, 3),
    ("Button", 0.8, 30, 4),
    ("Jay", 0.4, 70, 5),
    ("Ramirez", 0.1, 10, 6),
    ("Rice", 0.3, 0, 7),
    ("Dimitry", 0.5, 30, 8),
    ("Jonh", 0.2, 40, 9),
    ("Shev", 0.4, 50, 10),
    ("Richard", 0.6,45, 11),
    ("Manny", 0.7, 68, 12),
    ("Pedry", 0.9, 63, 13),
    ("Prons", 0, 32, 14),
    ("Miles", 0.8, 98, 15),
    ("Mike", 1, 100, 16),
    ("Filipe", 1, 92, 17),
]


carros_constantes = [Carro(*data) for data in dados_carros_constantes]

for carro in carros_constantes:
    carro.posicao_reversa = 21 - carro.posicao_corrida

dados_carros = dados_carros_usuario + carros_constantes

schedule, acidentes_graves = pit_stop_schedule(dados_carros)

print("\nCronograma de paradas nos boxes:")
for id_carro in schedule:
    print(id_carro)

print("\nCarros com acidentes graves:")
for carro in acidentes_graves:
    print(f"{carro.id_carro} teve um acidente grave e precisa parar imediatamente!")