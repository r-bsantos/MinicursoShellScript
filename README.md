# Minicurso de Shell Script — Do Básico à Automação Avançada

Material de estudo completo e **formatado** (com explicações, exemplos, exercícios e scripts de produção), focado em administração de sistemas e automação.

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

```
#!/bin/bash
# O jogo da velha (#) serve para fazer comentários ignorados pelo sistema.
clear
echo "Olá! Este é meu primeiro script."


```

### 1.3. Permissões de Execução

Sistemas Linux nascem seguros. Um arquivo de texto recém-criado não pode ser executado.

```
# Dando permissão de execução
chmod +x meu_script.sh

# Executando
./meu_script.sh


```

## Módulo 2 — Variáveis, Argumentos e Aritmética

### 2.1. Variáveis

Diferente de outras linguagens, em Shell não se usa espaços ao lado do sinal de igual.

```
# CORRETO
usuario="Robson"
# Chamando a variável (sempre use $ para ler o conteúdo)
echo "Bem-vindo, $usuario"


```

### 2.2. Recebendo Argumentos do Terminal

Quando você roda um script passando informações logo à frente dele no terminal (ex: `./script.sh arg1 arg2`), o Shell automaticamente guarda esses valores em variáveis especiais para você usar lá dentro.

* `$1`, `$2`, `$3`... = Representam o primeiro, segundo, terceiro argumento, etc.

* `$@` = Todos os argumentos passados, em formato de lista.

* `$#` = A quantidade total de argumentos passados.

**Exemplo prático (`saudacao.sh`):**

```
#!/bin/bash

# Exibindo os dados recebidos pelo terminal
echo "Total de informações recebidas: $#"
echo "A primeira palavra foi: $1"
echo "A segunda palavra foi: $2"
echo "Lista completa de tudo que foi digitado: $@"


```

*Se você rodar o comando: `./saudacao.sh Linux Automação`, a saída na tela será "Linux" na variável `$1` e "Automação" na variável `$2`.*

### 2.3. Operações Aritméticas (com `expr` ou duplo parênteses)

```
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

```
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

Em Shell Script, os operadores mudam dependendo do tipo de dado que você está avaliando. É muito importante não confundir operadores numéricos com os de texto!

* **Comparação de Números:**

  * `-eq` (equal / igual a)

  * `-ne` (not equal / diferente de)

  * `-gt` (greater than / maior que)

  * `-lt` (less than / menor que)

  * `-ge` (greater or equal / maior ou igual a)

  * `-le` (less or equal / menor ou igual a)

* **Comparação de Strings (Textos):**

  * `=` (igual)

  * `!=` (diferente)

  * `-z` (string está vazia / tamanho zero)

  * `-n` (string NÃO está vazia)

* **Verificação de Arquivos e Diretórios:**

  * `-e` (arquivo ou diretório existe)

  * `-d` (existe e é um diretório)

  * `-f` (existe e é um arquivo comum)

**Exemplos Práticos com os Operadores:**

```
#!/bin/bash

# ==========================================
# 1. Testando Números: Igualdade e Diferença (-eq, -ne)
# ==========================================
qtd_erros=0
if [ "$qtd_erros" -eq 0 ]; then
    echo "Sucesso: Nenhum erro encontrado (-eq 0)."
fi

codigo_saida=1
if [ "$codigo_saida" -ne 0 ]; then
    echo "Alerta: Ocorreu um problema, código de saída não é zero (-ne 0)."
fi

# ==========================================
# 2. Testando Números: Maior e Menor (-gt, -lt, -ge, -le)
# ==========================================
uso_disco=85
if [ "$uso_disco" -gt 90 ]; then
    echo "Crítico: Uso de disco MAIOR QUE 90% (-gt)."
elif [ "$uso_disco" -ge 80 ]; then
    echo "Atenção: Uso de disco MAIOR OU IGUAL a 80% (-ge)."
fi

tempo_espera=15
if [ "$tempo_espera" -lt 10 ]; then
    echo "Rápido: Tempo MENOR QUE 10 segundos (-lt)."
elif [ "$tempo_espera" -le 20 ]; then
    echo "Aceitável: Tempo MENOR OU IGUAL a 20 segundos (-le)."
fi

# ==========================================
# 3. Testando Strings (Textos) e Valores do Sistema
# ==========================================
# O Shell pega automaticamente o usuário logado usando a variável nativa $USER
# (ou executando o comando 'whoami')
usuario_logado=$USER

if [ "$usuario_logado" = "root" ]; then
    echo "Acesso total liberado. Olá, Administrador!"
else
    echo "Acesso comum. Bem-vindo(a), $usuario_logado!"
fi

nome=""
if [ -z "$nome" ]; then
    echo "Erro: O nome não foi preenchido (-z detecta vazio)!"
fi

# ==========================================
# 4. Testando Arquivos
# ==========================================
caminho="/etc/passwd"
if [ -f "$caminho" ]; then
    echo "O arquivo foi encontrado no sistema (-f)!"
else
    echo "Arquivo não existe."
fi


```

## Módulo 4 — Repetição (Loops)

### 4.1. Laço `for`

Para iterar sobre listas ou arquivos:

```
#!/bin/bash
for arquivo in /var/log/*.log; do
  echo "Encontrado o log: $arquivo"
done


```

### 4.2. Laço `while` (Menus Interativos)

```
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

O Shell orquestra muito bem outras ferramentas. Você não precisa fazer tudo em Bash! Você pode usar um laço Bash para processar arquivos em lote, alimentando um script Python (que é melhor com dados complexos) de forma automatizada.

Abaixo, o nosso Shell Script vai procurar todos os arquivos `.txt` na pasta e enviar um a um para um script Python processar:

**Script Shell (`orquestrador.sh`):**

```
#!/bin/bash
echo "Iniciando orquestração com Python..."

# Procura todos os arquivos .txt na pasta atual
for arquivo in *.txt; do
  # Se não encontrar nada, ignora e segue a vida
  [ -e "$arquivo" ] || continue
  
  echo "Enviando arquivo '$arquivo' para análise..."
  # Chama o python enviando o nome do arquivo como o "Argumento 1"
  python3 processador.py "$arquivo"
done

echo "Processamento em lote concluído!"


```

*(Nota para o Laboratório: Certifique-se de criar os arquivos de exemplo `processador.py` e `entrada.txt` no mesmo diretório antes de rodar o `orquestrador.sh`).*

### 5.2. Rodando scripts em "Backstage"

Se você fechar o terminal conectado ao servidor, seu script morre. O comando `nohup` junto com o `&` previnem isso.

```
nohup ./script_demorado.sh > relatorio.out 2> erros.log &


```

*Isto garante que a saída padrão vai para relatorio, os erros para um log específico e roda em segundo plano.*

## Módulo 6 — Automação Avançada (Cenários Reais)

Nesta etapa, vamos aplicar os conceitos estudados em cenários práticos de administração de sistemas.

### 6.1. Relatório de Saúde e Diagnóstico de Gargalos (RAM e Disco)

Este script faz uma radiografia do sistema e identifica possíveis gargalos de infraestrutura. Pode ser rodado por usuários comuns.

```
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

```
#!/bin/bash
# backup_rotativo.sh

DATA=$(date +%Y%m%d_%H%M)
ORIGEM="$HOME/Documentos" # Pasta que queremos salvar
DESTINO="$HOME/backup_seguro"
ARQUIVO="$DESTINO/backup_$DATA.tar.gz"
RETENCAO=7 # Manter backups por apenas 7 dias
LOG="$DESTINO/backup.log"

# Verifica se a pasta de destino NÃO existe (! -d)
if [ ! -d "$DESTINO" ]; then
    echo "Pasta de destino não encontrada. Criando $DESTINO..."
    mkdir -p "$DESTINO"
fi

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

```
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

```
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

```
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

```
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

```
#!/bin/bash
# organiza_arquivos.sh

# Definindo variáveis
ORIGEM="$HOME/Downloads"
DEST_IMG="$HOME/Imagens/Salvas"
DEST_DOC="$HOME/Documentos/Organizados"

# Garantindo que as pastas de destino existem
# Aqui também podemos aplicar a verificação com 'if' explicada anteriormente
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

Ao final do curso você deve ser capaz de:

* \[ \] Navegar no Linux compreendendo como os pipes (`|`) e redirecionamentos (`>`, `>>`) orquestram o sistema.

* \[ \] Criar scripts com variáveis, cálculos e receber argumentos de fora (`$1`).

* \[ \] Construir lógicas de decisão robustas usando `if` e laços de repetição (`for`, `while`).

* \[ \] Tratar arquivos em lote (como leitura de `.csv` e movimentação automática).

* \[ \] Orquestrar ferramentas de outras linguagens (como Python) usando Shell.

* \[ \] Construir ferramentas que rodem de forma contínua, agendadas via `crontab` e realizem manutenção preventiva.
