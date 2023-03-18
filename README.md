# EDIFIER W800BT Plus APP for linux

O objetivo desse projeto é construir um app para controle e monitoramento do Headset para o Linux mais especificamente no Ubuntu. O primeiro será `EDIFIER W800BT Plus`.

Esse projeto é open source e disponível para receber contribuições tanto para outras distros quanto para outros dispositivos.

### Mais sobre o projeto
A ideia é utilizar a ferramenta pacmd como base para obter as informações e controlar o dispositivo.

### Stack do projeto
- Python
- GTK
- Typer
- Pytest
- Poetry

## Andamento do projeto
Etapa atual - 1

### Lista de dispositivos testados e estão funcionando com este aplicativo:

|Dispositivo | Cobertura|
| :---: | :---: |
| EDIFIER W800BT Plus | **40 %** |


## Lista de funções que o aplicativo deverá possuir
- capturar a entrada do dispositivo
- validar o profile que está ativo
- modo para trocar entre os perfis do dispositivo
- mostrar o nome do dispositivo
- apresentar o percentual de bateria

## Projeto divido em etapas
* Etapa 0
    - Setup, configuração do ambiente e suas dependências

* Etapa 1
    - Criar uma API
    - Criar uma interface CLI
    - Criar testes automatizados
    - Documentação

* Etapa 2
    - Criar uma interface gráfica
    - Criar testes automatizados
    - Documentação

* Etapa 3
    - Criar alerta de nível de bateria para realizar recarga
    - Criar atalhos de teclado integrados ao Sistema
    - Criar testes automatizados
    - Documentação

* Etapa 4
    - Criar perfis
    - Criar testes automatizados
    - Documentação

