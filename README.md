# MediasMoveisChoquet

Na sociedade moderna, a infraestrutura de redes de computadores é essencial para o acesso rápido e confiável aos recursos digitais, sendo crucial tanto para negócios quanto para atividades diárias. O crescimento do número de dispositivos interconectados gera um fluxo constante de dados, exigindo monitoramento e gestão eficientes. Este trabalho compara modelos de médias móveis com fraca dependência histórica de dados para prever o tráfego de rede e detectar anomalias, utilizando uma função de agregação baseada na integral de Choquet. A seguir, apresentamos a arquitetura proposta, a implementação, os cenários de testes, os resultados obtidos e as considerações finais.

Como utilizar:
O programa é dividido em três partes principais:

**compilado.csv**: Base de dados composta pela análise de 5 dias fornecida pelo Intrusion Detection Evaluation Dataset (CIC-IDS2017).

**funcoes.py**: Contém as funções matemáticas de atribuição de pesos e cálculo, incluindo as metodologias PMA e Choquet.

**segurança_preditor.py**: Responsável pela execução do programa e pelo cálculo dos ataques.

Para executar o programa, basta iniciar o arquivo segurança_preditor.py junto com todos os arquivos mencionados anteriormente na mesma pasta. Para realizar a alteração da base de dados e testar com outros arquivos, é necessário apenas adicionar um novo arquivo CSV na pasta e atualizar o diretório na linha 7 do arquivo segurança_preditor.py.
