## Classificador TCE
Repositório contendo auxiliares para classificações de documentos para o TCE. 

O script em questão possibilita receber múltiplos diretórios de entrada e irá gerar um xml para cada arquivo, respeitando o mesmo path do documento inicial. Além disso, a geração desses xmls são feitas de forma incremental.

Nenhum arquivo original é removido/alterado, e mesmo que seja removido um diretório de indexação após a primeira execução, os xmls anteriormente gerados para aqueles documentos serão mantidos.

Caso não seja possível ler algum arquivo durante a execução, a informação do arquivo com problema é acrescidoa ao log em ```./res/classificador.log```
 
### Requisitos

* Python 3.6+


### Configs


No arquivo ```config.py``` é possível definir todas as infos necessárias para execução do script, sendo eles: 

| Valor        | Definição           |
| ------------- |:-------------:|
| ```SHARED_FOLDER_PATHS```      | Lista de diretórios contendo os documentos a serem classificados |
| ```XML_FOLDER_PATH```     | Caminho do diretório a partir de onde serão salvos os xmls      |
| ```SUMMARY_PATH``` | Caminho onde será salvo o resumo da execução do script. Caso vazio, não será gerado resumo      |
| ```FIRST_PAGE_PARAGRAPHS``` | Quantidade de parágrafos que serão considerados para tentar encontrar hits apenas na primeira página     |

