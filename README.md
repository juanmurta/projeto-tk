# Sistema de Consulta e Atualização de Cotações de Moedas

## Descrição  
Este projeto é uma aplicação desktop desenvolvida em **Python**, utilizando as bibliotecas **Tkinter** para interface gráfica, **Pandas** para manipulação de dados, **Requests** para consultas de API e **tkcalendar** para seleção de datas. A aplicação permite consultar a cotação de uma moeda específica em um dia escolhido e atualizar cotações de múltiplas moedas dos últimos 15 dias a partir de uma planilha Excel, salvando os resultados em um novo arquivo (`Teste.xlsx`).

## Funcionalidades Principais  
- **Consulta de Cotação Específica**:  
  - Permite selecionar uma moeda e uma data para consultar a cotação do dia via API (`economia.awesomeapi.com.br`).  
  - Exibe o valor da cotação em reais (R$) na interface.  
- **Seleção de Arquivo Excel**:  
  - Permite ao usuário selecionar uma planilha Excel contendo uma lista de moedas.  
- **Atualização de Cotações de Múltiplas Moedas**:  
  - Lê uma planilha Excel e atualiza as cotações dos últimos 15 dias para cada moeda listada.  
  - Adiciona novas colunas com datas e valores de cotações na planilha, salvando os resultados em `Teste.xlsx`.  
- **Interface Gráfica Intuitiva (`Tkinter`)**:  
  - Inclui combobox para seleção de moedas, calendário para escolha de datas, botões para ações e feedback visual sobre o status das operações.  

## Como Contribuir  
1. Faça um fork do repositório.  
2. Crie um branch para suas alterações.  
3. Commit suas mudanças.  
4. Faça push para o branch.  
5. Abra um Pull Request.  

Para mais detalhes sobre como contribuir, veja a [documentação oficial do GitHub sobre Pull Requests](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests).  
