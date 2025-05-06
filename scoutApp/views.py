from django.shortcuts import render

# Create your views here.
# scouts/views.py

from django.shortcuts import render, redirect
from .models import Acao,Partida
from django.contrib import messages

def registrar_acao(request):
    if request.method == 'POST':
        partida_id = request.session.get('partida_id')
        partida = Partida.objects.get(id=partida_id)
        jogador = request.POST.get('jogador')
        tipo_acao = request.POST.get('acao')
        pos_x = request.POST.get('pos_x')
        pos_y = request.POST.get('pos_y')
        tempo = int(request.POST['tempo'])
        # Cria e salva a ação
        Acao.objects.create(
            jogador=jogador,
            tipo_acao=tipo_acao,
            pos_x=pos_x,
            pos_y=pos_y,
            tempo=tempo,
            partida=partida
        )

    return render(request, 'scouts/forms3.html')


def formulario(request):
    jogadores = request.session.get('jogadores_america', [])
    time1 = request.session.get('time_casa', [])
    time2 = request.session.get('time_fora', [])
    tempo_selecionado = request.session.get('tempo_selecionado', 1)  # valor padrão = 1
    if request.method == 'POST':
        partida_id = request.session.get('partida_id')
        partida = Partida.objects.get(id=partida_id)
        jogador = request.POST.get('jogador')
        tipo_acao = request.POST.get('acao')
        pos_x = request.POST.get('pos_x')
        pos_y = request.POST.get('pos_y')
        tempo = request.POST.get('tempo')
        acoes_sem_jogador = [
            'Escanteio OF',
            'Falta Lat OF',
            'Finalização ADV',
            '2ª Bola ADV',
            'Entrada no Último 1/3 ADV',
            'Cruzamento ADV',
            'Escanteio DEF',
            'Falta Lat DEF'
        ]
        if tipo_acao not in acoes_sem_jogador:
            if jogador and tipo_acao and pos_x and pos_y:
                Acao.objects.create(
                    jogador=jogador,
                    tipo_acao=tipo_acao,
                    pos_x=pos_x,
                    pos_y=pos_y,
                    tempo=tempo,
                    partida=partida
                )
            return redirect('formulario')
        else:
            Acao.objects.create(
                jogador='Adversário',
                tipo_acao=tipo_acao,
                pos_x=pos_x,
                pos_y=pos_y,
                tempo=tempo,
                partida=partida
            )
            return redirect('formulario')

    # Calcula totais do banco
    scouts = Acao.objects.all()

    totais = {
        'Finalizacao_AMERICA': scouts.filter(tipo_acao='Finalização AMÉRICA').count(),
        'Desarme': scouts.filter(tipo_acao='Desarme').count(),
        'Interceptacao': scouts.filter(tipo_acao='Interceptação').count(),
        'Seg_Bola_Ganha': scouts.filter(tipo_acao='2ª Bola Ganha').count(),
        'Entrada_no_Ultimo_1_3_AMERICA': scouts.filter(tipo_acao='Entrada no Último 1/3 AMÉRICA').count(),
        'Cruzamento_AMERICA': scouts.filter(tipo_acao='Cruzamento AMÉRICA').count(),
        'Escanteio_OF': scouts.filter(tipo_acao='Escanteio OF').count(),
        'Falta_Lat_OF': scouts.filter(tipo_acao='Falta Lat OF').count(),
        'Falta_Sofrida': scouts.filter(tipo_acao='Falta Sofrida').count(),
        'Falta_Cometida': scouts.filter(tipo_acao='Falta Cometida').count(),
        'Finalizacao_ADV': scouts.filter(tipo_acao='Finalização ADV').count(),
        'Passe_Errado': scouts.filter(tipo_acao='Passe Errado').count(),
        'Perda_de_Posse': scouts.filter(tipo_acao='Perda de Posse').count(),
        'Seg_Bola_ADV': scouts.filter(tipo_acao='2ª Bola ADV').count(),
        'Entrada_no_Ultimo_1_3_ADV': scouts.filter(tipo_acao='Entrada no Último 1/3 ADV').count(),
        'Cruzamento_ADV': scouts.filter(tipo_acao='Cruzamento ADV').count(),
        'Escanteio_DEF': scouts.filter(tipo_acao='Escanteio DEF').count(),
        'Falta_Lat_DEF': scouts.filter(tipo_acao='Falta Lat DEF').count(),
    }

    return render(request, 'scouts/forms5.html', {'totais': totais, 'jogadores': jogadores, 'time1': time1, 'time2':time2, 'tempo_selecionado':tempo_selecionado})


def desfazer_ultima_acao(request):
    if request.method == 'POST':
        ultima_acao = Acao.objects.last()
        if ultima_acao:
            ultima_acao.delete()
    return redirect('formulario')

def criar_partida2(request):
    if request.method == 'POST':
        time_casa = request.POST.get('time_casa')
        time_fora = request.POST.get('time_fora')

        jogadores_america = []
        for i in range(1, 24):  # até 12 jogadores
            nome = request.POST.get(f'jogador_{i}')
            if nome:
                jogadores_america.append(nome)

        # Armazena na sessão
        request.session['time_casa'] = time_casa
        request.session['time_fora'] = time_fora
        request.session['jogadores_america'] = jogadores_america

        return redirect('formulario')  # nome da URL da tela de scout
    context = {
        'range_11': range(1, 12)
        }
    return render(request, 'prejogo/criar_partida.html', context)

def criar_partida(request):
    if request.method == 'POST':
        time_casa = request.POST.get('time_casa') or request.session.get('time_casa')
        time_fora = request.POST.get('time_fora') or request.session.get('time_fora')

        jogadores_america = []
        for i in range(1, 24):
            nome = request.POST.get(f'jogador_{i}')
            if nome:
                jogadores_america.append(nome)

        # Atualiza a sessão com os novos jogadores
        request.session['time_casa'] = time_casa
        request.session['time_fora'] = time_fora
        request.session['jogadores_america'] = jogadores_america
        # Cria a partida
        partida = Partida.objects.create(time_casa=time_casa, time_fora=time_fora)

        # Armazena o ID da partida na sessão
        request.session['partida_id'] = partida.id
        return redirect('formulario')  # volta para o scout

    # Se for GET, pega os jogadores já existentes
    jogadores_america = request.session.get('jogadores_america', [])
    time1 = request.session.get('time_casa', '')
    time2 = request.session.get('time_fora', '')
    context = {
        'jogadores_america': jogadores_america,
        'range_11': range(1, 12),
        'time1': time1,
        'time2': time2
    }
    return render(request, 'prejogo/criar_partida.html', context)
