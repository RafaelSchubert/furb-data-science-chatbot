import sys

INFO_MODELOS = {
    'Ford Bronco Sport 2021': {
        'descricao': 'Um SUV construído para o caçador de emoções, o turista e o viajante diurno. Para possibilitar sua jornada ao inexplorado, este veículo robusto coloca a utilidade em primeiro plano com um design que inclui superfícies fáceis de limpar e uma tonelada de espaço interior, graças à arquitetura espaçosa do telhado em estilo safári.',
        'tags': 'SUV, Off-Road, Viagem',
        'preco': 'USD$ 26.820'
    },
    'Ford Ecosport 2021': {
        'descricao': 'O Ford EcoSport 2021 oferece 4WD Inteligente e um desempenho esportivo que o torna ideal para uma direção diária tranquila. Onde quer que você vá, o EcoSport oferece um interior elegante e tecnologia inteligente projetada para ajudá-lo a se manter conectado.',
        'tags': 'SUV, Dia a dia',
        'preco': 'USD$ 19.995'
    },
    'Ford Escape Hybrid 2021': {
        'descricao': 'O Ford Escape 2021 foi feito para um estilo de vida ativo e oferece muitas opções para você pegar a estrada em seu próprio estilo. Um veículo com uma reputação sólida por oferecer espaço flexível para carga e passageiros, reboque impressionante e tecnologia padrão e confiável de conectividade e segurança, tudo isso perfeitamente integrado com uma aparência esportiva.',
        'tags': 'Elétrico, SUV, Dia a dia, Viagem',
        'preco': 'USD$ 27.605'
    },
    'Ford Explorer Hybrid 2021': {
        'descricao': 'O Ford Explorer 2021 está preparado para a exploração nos tempos modernos. Seu interior ajustável oferece espaço e conforto para toda a família. E ajuda você a aproveitar ao máximo cada experiência com tecnologia conectada e uma forma atlética que está pronta para o que está por vir.',
        'tags': 'Elétrico, SUV, Viagem',
        'preco': 'USD$ 45.005'
    },
    'Ford F-150 Raptor 2020': {
        'descricao': 'Fornecendo a base para a melhor capacidade de carga útil disponível em sua categoria, o Ford F-150 oferece a capacidade de transportar o que você precisa para trabalhar ou se divertir. Com o único corpo de liga de alumínio de alta resistência e grau militar e estrutura de aço de alta resistência em sua categoria, o Ford F-150 faz com que tarefas difíceis pareçam fáceis, esteja você no trabalho ou de saída para o final de semana.',
        'tags': 'Camionete, Esportivo, Lazer, Off-Road',
        'preco': 'USD$ 53.455'
    },
    'Ford Fusion Hybrid 2021': {
        'descricao': 'Com opções de trem de força a gasolina, híbrido e híbrido plug-in, o Fusion 2021 é onde tecnologia, estilo e direção responsável se encontram. As opções híbrido e híbrido plug-in podem ajudar a melhorar a eficiência e a autonomia totais de seu veículo. No modo totalmente elétrico, o híbrido plug-in pode até mesmo reduzir as emissões de CO2, ajudando a deixar uma pegada menor.',
        'tags': 'Elétrico, Passeio, Dia a dia',
        'preco': 'USD$ 28.000'
    },
    'Ford Mustang Mach 1 2021': {
        'descricao': 'Ouça o rugido de um Mustang enquanto o chão balança e suas pernas tremem. Como sempre, o Mustang apela às suas raízes de performance com recursos para direção aprimorada, opções de motor de alta potência e design clássico do Mustang. O Mach 1, completamente personalizável, continua seu legado, projetado para voltas rápidas e direção vigorosa.',
        'tags': 'Esportivo, Lazer',
        'preco': 'USD$ 54.315'
    },
    'Ford Mustang Mach-E 2021': {
        'descricao': 'O Mustang Mach-E revigora o prazer de dirigir. Este modelo traz um design verdadeiramente icônico, combinado com materiais luxuosos e tecnologias padrão de assistência ao motorista, como o Ford Co-Pilot360™ 2.0. Além disso, toda a emoção das rodovias que você pode suportar, com acesso à maior rede pública de recarga da América do Norte oferecida por fabricantes automotivos.',
        'tags': 'Elétrico, Esportivo, SUV, Dia a dia, Viagem',
        'preco': 'USD$ 42.895'
    },
    'Ford Mustang Shelby GT500 2021': {
        'descricao': 'A combinação de um motor V8 de 5,2 litros superpotente e uma transmissão TREMEC de 7 marchas de dupla embreagem confere a este Shelby potência e desempenho inspiradores. Projetado com caças em mente, o exterior aerodinâmico permite atingir uma velocidade máxima de 300 Km/h. Com sua construção precisa e motorização superior, o Shelby GT500 leva o desempenho a novos patamares como o Mustang de rua legal mais rápido de todos os tempos.',
        'tags': 'Esportivo, Lazer',
        'preco': 'USD$ 72.900'
    },
    'Ford Super Duty 2021': {
        'descricao': 'A Super Duty nunca para de seguir em frente. As impressionantes classificações de potência a gás e diesel da Super Duty combinam-se com uma estrutura robusta e engenharia de chassi para atingir números fortes em todas as categorias de capacidades de transporte e reboque, incluindo as melhores potência, GVWR, capacidade de carga útil e reboque da sua categoria.',
        'tags': 'Camionete, Comercial, Off-Road, Trabalho',
        'preco': 'USD$ 34.230'
    },
    'Ford Transit 2021': {
        'descricao': 'O Ford Transit 2021 está pronto para trabalhar. Desde a transmissão automática de 10 marchas e uma escolha de motores disponíveis até a tecnologia inteligente que lhe ajuda a dirigir com confiança, o Transit foi construído pensando na sua produtividade, seu conforto e seus resultados financeiros.',
        'tags': 'Comercial, Trabalho',
        'preco': 'USD$ 35.020'
    },
    'Ford Transit Connect 2021': {
        'descricao': 'Carregue e dirija. O Ford Transit Connect 2021 oferece espaços de carga e assentos grandes e flexíveis, assentos dobráveis nas segunda e terceira fileiras e portas laterais deslizantes duplas por padrão. Além disso, você descobrirá que sua fácil manobrabilidade é mais do que capaz de colocá-lo dentro, fora e em todos os lugares.',
        'tags': 'Passeio, Dia a dia, Viagem',
        'preco': 'USD$ 27.400'
    }
}

def get_info_modelo(modelo: str):
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json'},
        'body': INFO_MODELOS[modelo]
    }

def main(params: dict):
    operacao = params['operacao']
    if operacao == 'consultar_modelo':
        return get_info_modelo(params['modelo'])
