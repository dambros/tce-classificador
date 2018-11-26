# general
SHARED_FOLDER_PATHS = [
    # '/Users/dambros/Downloads/documentos_classificar/maquina_1',
    # '/Users/dambros/Downloads/documentos_classificar/maquina_2',
    # '/Users/dambros/Downloads/documentos_classificar/mario',
    # '/Users/dambros/Downloads/documentos_classificar/odt'
    '/Users/dambros/Downloads/documentos_classificar/geanlucas'
]
XML_FOLDER_PATH = '/Users/dambros/Downloads/documentos_classificar/xml/'
SUMMARY_PATH = '/Users/dambros/Downloads/documentos_classificar/xml/summary.csv'
FIRST_PAGE_PARAGRAPHS = 20

# não alterar
LOG_CONFIG_PATH = './res/configs/logging.ini'
DB_PATH = './res/db'
ROOT_CATEGORIES = {
    'Relatório Voto': ['relatório voto', 'relatório e voto', 'é o voto',
                       'é como voto'],
    'Decisão Singular': ['decisão singular', 'é a decisão'],
    'Cautelar': ['cautelar', 'liminar'],
    'Despacho': ['despacho']
}
SUB_CATEGORIES = {
    'Relatório Voto': {
        'Ata': ['ata'],
        'Auditoria': ['auditoria'],
        'Contrato': ['contrato administrativo'],
        'Contrato Obra': ['contrato de obra'],
        'Pessoal': ['ato de pessoal', 'atos de pessoal', 'ato', 'atos',
                    'concessão', 'pensão', 'aposentadoria'],
        'Recursos': ['recurso ordinário', 'embargos de declaração', 'agravo'],
        'Denúncia': ['denúncia'],
        'Representação': ['representação'],
        'Contábil': ['apuração de responsabilidade', 'orçamento programa',
                     'prestação de contas'],
        'Consulta': ['consulta'],
        'Pedido de Revisão': ['pedido de revisão']
    },
    'Decisão Singular': {
        'Ata': ['ata'],
        'Convênio': ['convênio'],
        'Contrato': ['contrato administrativo'],
        'Contrato Obra': ['contrato de obra'],
        'Pessoal': ['ato de pessoal', 'atos de pessoal', 'ato', 'atos',
                    'concessão', 'pensão', 'aposentadoria']
    }
}
