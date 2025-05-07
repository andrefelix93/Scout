let jogadorSelecionado = '';
let acaoSelecionada = '';

function selecionarJogador(jogador) {
    jogadorSelecionado = jogador;
    document.getElementById('jogador').value = jogador;
}

function selecionarAcao(acao) {
    acaoSelecionada = acao;
    document.getElementById('acao').value = acao;
}

function registrarClique2(event) {
    const campo = document.getElementById('campo');
    const rect = campo.getBoundingClientRect();

    const x = ((event.clientX - rect.left) / campo.width).toFixed(4);
    const y = ((event.clientY - rect.top) / campo.height).toFixed(4);

    document.getElementById('pos_x').value = x;
    document.getElementById('pos_y').value = y;

    if (jogadorSelecionado && acaoSelecionada) {
        document.getElementById('formAcao').submit();
    } else {
        alert('Selecione um jogador e uma ação primeiro2!');
    }
}

function registrarClique3(event) {
    const campo = document.getElementById('campo');
    const rect = campo.getBoundingClientRect();

    const x = ((event.clientX - rect.left) / campo.width).toFixed(4);
    const y = ((event.clientY - rect.top) / campo.height).toFixed(4);

    document.getElementById('pos_x').value = x;
    document.getElementById('pos_y').value = y;

    const acoesSemJogador = [
        'Escanteio OF',
        'Falta Lat OF',
        'Finalização ADV',
        '2ª Bola ADV',
        'Entrada no Último 1/3 ADV',
        'Cruzamento ADV',
        'Escanteio DEF',
        'Falta Lat DEF'
    ];
    const acaoSelecionadaTexto = document.getElementById("escanteio-of").classList.contains("selecionado")
    if (acaoSelecionada && (jogadorSelecionado || acoesSemJogador.includes(acaoSelecionadaTexto))) {
        document.getElementById('formAcao').submit();
    } else {
        alert('Selecione um jogador e uma ação primeiro3!');
    }
}

function registrarClique(event) {
    const campo = document.getElementById('campo');
    const rect = campo.getBoundingClientRect();

    const x = ((event.clientX - rect.left) / campo.width).toFixed(4);
    const y = ((event.clientY - rect.top) / campo.height).toFixed(4);

    document.getElementById('pos_x').value = x;
    document.getElementById('pos_y').value = y;


    document.getElementById('formAcao').submit();

}


let substituicoes = [];

function substituirJogador() {
  const jogadorAntigo = prompt("Digite o nome do jogador que vai sair:");
  if (!jogadorAntigo) {
    alert("Nome do jogador não informado.");
    return;
  }

  const novoJogador = prompt("Digite o nome do novo jogador:");
  if (!novoJogador) {
    alert("Nome do novo jogador não informado.");
    return;
  }

  // Atualiza o botão
  const botaoJogador = document.getElementById('jogador-' + jogadorAntigo);
  if (botaoJogador) {
    botaoJogador.innerText = novoJogador;
    botaoJogador.setAttribute('onclick', "selecionarJogador('" + novoJogador + "')");
    botaoJogador.setAttribute('id', 'jogador-' + novoJogador);
    alert(`Jogador ${jogadorAntigo} substituído por ${novoJogador}.`);

    // Registra a substituição
    substituicoes.push({ 'sai': jogadorAntigo, 'entra': novoJogador });

    // Atualiza o campo escondido
    document.getElementById('substituicoes').value = JSON.stringify(substituicoes);

  } else {
    alert("Jogador não encontrado!");
  }
}


    function selecionarJogador(jogador) {
    document.querySelector('input[name="jogador"]').value = jogador;

}

function abrirTotais() {
    document.getElementById("modalTotais").style.display = "block";
  }

function fecharTotais() {
    document.getElementById("modalTotais").style.display = "none";
  }

  function abrirTotais1T() {
    document.getElementById("modalTotais1T").style.display = "block";
  }

function fecharTotais1T() {
    document.getElementById("modalTotais1T").style.display = "none";
  }

  function abrirTotais2T() {
    document.getElementById("modalTotais2T").style.display = "block";
  }

function fecharTotais2T() {
    document.getElementById("modalTotais2T").style.display = "none";
  }

