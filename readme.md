# Minicurso de Shell Script — Do Básico à Automação Avançada

Material de estudo completo e **formatado** (com explicações, exemplos, exercícios e scripts de produção), focado em administração de sistemas e automação.

## Como utilizar este material (Escolha sua Trilha)

Este minicurso foi desenhado para se adaptar ao nível da turma. Antes de começar, defina com os alunos qual vertente seguir:

* **Opção 1 (Trilha Completa - Iniciantes):** Foco em ensinar os fundamentos do Linux, estrutura do sistema, conceitos de lógica em Shell (Módulos 0 a 5) e finalização com 1 ou 2 automações do Módulo 6.

* **Opção 2 (Trilha Fast-Track - Foco em Automação):** Pula-se a sintaxe básica. Faz-se uma revisão relâmpago do Módulo 0 (para nivelamento de pipes e redirecionamentos) e mergulha-se diretamente no **Módulo 6**, estudando, rodando e adaptando os scripts avançados para o mundo real.

## Módulo 0 — Sobrevivência no Linux (Conceitos Essenciais)

Antes de programar, é fundamental entender onde estamos pisando. O Shell Script interage intimamente com o sistema operacional.

### 0.1. A Estrutura de Diretórios do Linux

No Linux, tudo é arquivo e a estrutura de pastas é uma árvore única que nasce na raiz (`/`).

* `/` **(Root):** A raiz do sistema.

* `/bin` e `/sbin`: Onde ficam os binários (comandos executáveis) do sistema (ex: `ls`, `cp`, `ping`).

* `/etc`: Guarda os arquivos de configuração do sistema e dos serviços.

* `/home`: Diretórios pessoais dos usuários comuns (suas pastas, downloads, scripts).

* `/var`: Dados variáveis, como logs do sistema (`/var/log`) e bancos de dados.

* `/tmp`: Arquivos temporários (apagados ao reiniciar).

* `/dev`: Dispositivos de hardware mapeados como arquivos (ex: discos `/dev/sda`).

### 0.2. Operadores Lógicos e de Fluxo no Terminal

Para criar automações reais, precisamos conectar comandos.

* `>` **(Redirecionamento de Saída - Sobrescreve):** Joga a saída de um comando para um arquivo, apagando o que havia antes.

  * *Exemplo:* `echo "Olá" > arquivo.txt`

* `>>` **(Redirecionamento de Saída - Anexa):** Adiciona a saída ao final do arquivo, sem apagar o conteúdo existente (muito usado para Logs).

  * *Exemplo:* `echo "Nova linha" >> arquivo.txt`

* `|` **(Pipe):** "Encanamento". Pega o resultado (saída) do comando da esquerda e injeta como entrada no comando da direita.

  * *Exemplo:* `ls -l /etc | grep "network"` (Lista o /etc e filtra apenas linhas com "network").

* `&` **(Background):** Executa um processo em segundo plano, liberando o terminal.

  * *Exemplo:* `meu_script.sh &`

* `&&` **(AND Lógico):** Executa o segundo comando **APENAS SE** o primeiro der certo (código de saída 0).

  * *Exemplo:* `mkdir nova_pasta && cd nova_pasta`

* `||` **(OR Lógico):** Executa o segundo comando **APENAS SE** o primeiro falhar.

  * *Exemplo:* `ping -c 1 google.com || echo "Estamos sem internet!"`

### 0.3. O Arquivo e Serviço `cron`

O `cron` é o "despertador" do Linux. Ele lê o arquivo `crontab` e executa scripts em horários programados automaticamente.

* Para editar seus agendamentos: `crontab -e`

* **Sintaxe (5 estrelas):** `Minuto Hora Dia_do_mês Mês Dia_da_semana Comando`

  * `* * * * * /meu_script.sh` (Roda a cada minuto).

  * `0 2 * * * /meu_script.sh` (Roda todo dia às 02:00 da manhã).

## Módulo 1 — Introdução e Primeiros Passos

### 1.1. O que é Shell Script?

É um arquivo de texto com uma sequência de comandos que o shell (interpretador) executa de cima para baixo. Serve para evitar repetição manual e garantir padronização em rotinas de TI.

### 1.2. Estrutura de um arquivo `.sh`

A primeira linha sempre define qual interpretador executará o script (Shebang):

```bash
#!/bin/bash
# O jogo da velha (#) serve para fazer comentários ignorados pelo sistema.
clear
echo "Olá! Este é meu primeiro script."
```

### 1.3. Permissões de Execução

Sistemas Linux nascem seguros. Um arquivo de texto recém-criado não pode ser executado.

```bash
# Dando permissão de execução
chmod +x meu_script.sh

# Executando
./meu_script.sh
```

## Módulo 2 — Variáveis, Argumentos e Aritmética

### 2.1. Variáveis

Diferente de outras linguagens, em Shell não se usa espaços ao lado do sinal de igual.

```bash
# CORRETO
usuario="Robson"
# Chamando a variável (sempre use $ para ler o conteúdo)
echo "Bem-vindo, $usuario"
```

### 2.2. Recebendo Argumentos do Terminal

Quando você roda `./script.sh arg1 arg2`:

* `$1` = Primeiro argumento.
* `$2` = Segundo argumento.
* `$@` = Todos os argumentos.
* `$#` = Quantidade de argumentos.

### 2.3. Operações Aritméticas (com `expr` ou duplo parênteses)

```bash
#!/bin/bash
x=10
y=3
# Usando a sintaxe nativa do bash:
soma=$((x + y))
resto=$((x % y))
echo "Soma: $soma | Resto: $resto"
```

## Módulo 3 — Condicionais (`if` / `else`)

### 3.1. Estrutura Base

```bash
if [ condição ]; then
  # Comandos se verdadeiro
elif [ outra_condição ]; then
  # Comandos se a segunda for verdadeira
else
  # Comandos se tudo falhar
fi
```

*(Nota: O espaço dentro dos colchetes `[ ]` é obrigatório!).*

### 3.2. Operadores de Comparação

* **Números:** `-eq` (igual), `-ne` (diferente), `-gt` (maior que), `-lt` (menor que), `-ge` (maior ou igual), `-le` (menor ou igual).

* **Strings:** `=` (igual), `!=` (diferente), `-z` (vazia).

* **Arquivos:** `-e` (existe), `-d` (é diretório), `-f` (é arquivo).

```bash
# Exemplo Prático: Checar se o usuário é root
if [ "$USER" = "root" ]; then
    echo "Você é o administrador."
else
    echo "Acesso restrito!"
fi
```

## Módulo 4 — Repetição (Loops)

### 4.1. Laço `for`

Para iterar sobre listas ou arquivos:

```bash
#!/bin/bash
for arquivo in /var/log/*.log; do
  echo "Encontrado o log: $arquivo"
done
```

### 4.2. Laço `while` (Menus Interativos)

```bash
#!/bin/bash
while true; do
  echo "1) Mostrar Data"
  echo "0) Sair"
  read -p "Escolha: " op

  if [ "$op" -eq 1 ]; then
    date
  elif [ "$op" -eq 0 ]; then
    echo "Saindo..."; break
  else
    echo "Opção inválida"
  fi
done
```

## Módulo 5 — Integração e Background

### 5.1. Chamando Python via Shell

O Shell orquestra muito bem outras ferramentas. Você pode usar um loop Bash para alimentar um script Python pesado.

```bash
#!/bin/bash
for arquivo in *.txt; do
  [ -e "$arquivo" ] || continue
  python3 processador.py "$arquivo"
done
```

### 5.2. Rodando scripts em "Backstage"

Se você fechar o terminal conectado ao servidor, seu script morre. O comando `nohup` junto com o `&` previnem isso.

```bash
nohup ./script_demorado.sh > relatorio.out 2> erros.log &
```

*Isto garante que a saída padrão vai para relatorio, os erros para um log específico e roda em segundo plano.*

## Módulo 6 — Automação Avançada (Cenários Reais)

*Se você escolheu a Trilha 2, o curso engrena de verdade aqui!*

### 6.1. Relatório de Saúde e Diagnóstico de Gargalos (RAM e Disco)

Este script faz uma radiografia do sistema e identifica possíveis gargalos de infraestrutura. Pode ser rodado por usuários comuns.

```bash
#!/bin/bash
# relatorio_saude.sh

echo "========================================"
echo "    RELATÓRIO DE SAÚDE DO SISTEMA"
echo "    Data: $(date '+%d/%m/%Y %H:%M:%S')"
echo "========================================"

# Uptime e Carga (Gargalo de CPU)
echo -e "\n[+] Uptime e Carga de CPU:"
uptime

# Memória RAM (Gargalo de Memória)
echo -e "\n[+] Consumo de Memória RAM:"
free -h

# Disco (Gargalo de Armazenamento)
echo -e "\n[+] Uso de Disco (Partições > 80% requerem atenção):"
df -h | grep -E '^/dev/|Filesystem'

# Processos Comilões
echo -e "\n[+] Top 3 Processos consumindo mais CPU:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 4

echo "========================================"
echo "Relatório gerado com sucesso."
```

### 6.2. Rotina de Backup com Rotação (Retenção)

Fazer backup é fácil. Difícil é gerenciar o disco cheio. Este script compacta dados e exclui backups com mais de 7 dias.

```bash
#!/bin/bash
# backup_rotativo.sh

DATA=$(date +%Y%m%d_%H%M)
ORIGEM="$HOME/Documentos" # Pasta que queremos salvar
DESTINO="$HOME/backup_seguro"
ARQUIVO="$DESTINO/backup_$DATA.tar.gz"
RETENCAO=7 # Manter backups por apenas 7 dias
LOG="$DESTINO/backup.log"

mkdir -p "$DESTINO"

echo "[$(date)] Iniciando backup de $ORIGEM..." >> "$LOG"
tar -czf "$ARQUIVO" "$ORIGEM" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "[$(date)] Sucesso! Arquivo criado: $ARQUIVO" >> "$LOG"
else
    echo "[$(date)] ERRO ao criar backup." >> "$LOG"
fi

# Rotação (Limpeza de arquivos antigos)
echo "[$(date)] Limpando backups com mais de $RETENCAO dias..." >> "$LOG"
find "$DESTINO" -type f -name "*.tar.gz" -mtime +$RETENCAO -exec rm {} \; >> "$LOG" 2>&1
```

### 6.3. Processamento de Dados em Lote (Leitura de CSV)

Perfeito para laboratórios! Em vez de alterar o sistema, vamos automatizar a leitura de um relatório (arquivo `dados_alunos.csv`), calcular quem foi aprovado e gerar um novo log.

```bash
#!/bin/bash
# processa_notas.sh

ARQUIVO="dados_alunos.csv"
RELATORIO="aprovados.txt"

# Verifica se o arquivo existe
if [ ! -f "$ARQUIVO" ]; then
    echo "Erro: Arquivo $ARQUIVO não encontrado!"
    exit 1
fi

echo "Processando notas dos alunos..."
> "$RELATORIO" # Limpa o arquivo de relatório antes de começar

# Lê o CSV separando pelas vírgulas (IFS=',')
while IFS=',' read -r matricula nome curso nota; do
    # Ignora o cabeçalho
    if [ "$matricula" = "Matricula" ]; then continue; fi
    
    # Compara a nota (usando bc para lidar com decimais ou lógica simples)
    # Aqui multiplicamos por 10 para usar aritmética simples do Bash
    nota_int=$(echo "$nota * 10" | bc | cut -d'.' -f1)
    
    if [ "$nota_int" -ge 60 ]; then
        echo "$nome (Matrícula: $matricula) - APROVADO ($nota)" >> "$RELATORIO"
    fi
done < "$ARQUIVO"

echo "Processamento concluído. Verifique o arquivo $RELATORIO."
```

### 6.4. Monitor de Serviços com Auto-Recuperação

Se um serviço vital cair, o Shell Script pode reerguê-lo. *(Nota: Iniciar/parar serviços geralmente exige privilégios de root).*

```bash
#!/bin/bash
# monitor_servico.sh

SERVICO="cron" # No lab, teste monitorar o próprio cron ou ssh
LOG="/tmp/monitor_$SERVICO.log"

if systemctl is-active --quiet "$SERVICO"; then
    echo "[$(date)] Tudo OK. O serviço $SERVICO está rodando."
else
    echo "[$(date)] ALERTA: $SERVICO parado! Tentando reiniciar..." >> "$LOG"
    sudo systemctl restart "$SERVICO"
    
    if systemctl is-active --quiet "$SERVICO"; then
        echo "[$(date)] RECOVERY: $SERVICO reiniciado com sucesso." >> "$LOG"
    else
        echo "[$(date)] CRÍTICO: Intervenção humana necessária." >> "$LOG"
    fi
fi
```

### 6.5. Sentinela de Conectividade (Redes)

Verifica se links de internet ou equipamentos da rede interna estão respondendo.

```bash
#!/bin/bash
# sentinela_rede.sh

ALVOS=("8.8.8.8" "1.1.1.1" "site_falso.com")

echo "Verificando conectividade..."

for host in "${ALVOS[@]}"; do
    # Dispara 1 ping, aguarda no máximo 2 segundos
    if ping -c 1 -W 2 "$host" &> /dev/null; then
        echo -e "[\033[32m ONLINE \033[0m] $host"
    else
        echo -e "[\033[31m OFFLINE\033[0m] $host"
    fi
done
```

### 6.6. Faxina no Sistema (Limpeza de RAM, Caches e Temp)

Script utilitário para liberar espaço em disco e memória. Dividido em tarefas de usuário comum (seguro) e tarefas administrativas (`sudo`).

```bash
#!/bin/bash
# faxina_sistema.sh

echo "Iniciando Faxina no Sistema..."

# 1. Limpeza Segura (Usuário Comum)
echo "[1/3] Limpando arquivos temporários do usuário..."
rm -rf /tmp/* 2>/dev/null
rm -rf "$HOME/.cache/thumbnails/*" 2>/dev/null
echo "Temporários limpos."

# 2. Limpeza de Cache de Atualizações (Requer Sudo)
echo "[2/3] Limpando cache do gerenciador de pacotes (requer senha)..."
sudo apt-get clean -y 2>/dev/null || echo "Aviso: Comando 'apt-get' não disponível nesta distro."

# 3. Limpeza de RAM/Swap (Requer Sudo)
# Muito útil em laboratórios de TI que rodam VMs ou compilações pesadas
echo "[3/3] Desfragmentando Memória RAM (drop caches)..."
sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null

echo "Faxina concluída! O sistema deve estar respirando melhor agora."
```

### 6.7. Organizador Automático de Arquivos (Downloads)

Excelente script para rodar no `cron` a cada hora. Ele pega sua pasta bagunçada e joga cada arquivo no diretório correto com base na extensão. 100% seguro para usuários comuns!

```bash
#!/bin/bash
# organiza_arquivos.sh

# Definindo variáveis
ORIGEM="$HOME/Downloads"
DEST_IMG="$HOME/Imagens/Salvas"
DEST_DOC="$HOME/Documentos/Organizados"

# Garantindo que as pastas de destino existem
mkdir -p "$DEST_IMG" "$DEST_DOC"

echo "Analisando a pasta: $ORIGEM"

# Movendo Imagens (.jpg, .png, .jpeg)
# Usamos 2>/dev/null para esconder erros caso não haja arquivos daquela extensão
mv "$ORIGEM"/*.jpg "$ORIGEM"/*.jpeg "$ORIGEM"/*.png "$DEST_IMG" 2>/dev/null
if [ $? -eq 0 ]; then echo "Imagens movidas com sucesso."; fi

# Movendo Documentos (.pdf, .docx, .txt)
mv "$ORIGEM"/*.pdf "$ORIGEM"/*.docx "$ORIGEM"/*.txt "$DEST_DOC" 2>/dev/null
if [ $? -eq 0 ]; then echo "Documentos movidos com sucesso."; fi

echo "Organização concluída!"
```

## Checklist Final de Domínio Técnico

Seja qual for a trilha escolhida, ao final do curso você deve ser capaz de:

* [ ] Navegar no Linux compreendendo como os pipes (`|`) e redirecionamentos (`>`, `>>`) orquestram o sistema.
* [ ] Criar scripts com variáveis, cálculos e receber argumentos de fora (`$1`).
* [ ] Construir lógicas de decisão robustas usando `if` e laços de repetição (`for`, `while`).
* [ ] Tratar arquivos em lote (como leitura de `.csv` e movimentação automática).
* [ ] Construir ferramentas que rodem de forma contínua, agendadas via `crontab` e realizem manutenção preventiva.
