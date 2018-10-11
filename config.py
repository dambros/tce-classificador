# general
LOG_CONFIG_PATH = './res/configs/logging.ini'
SHARED_FOLDER_PATHS = [
    # '/Users/dambros/Downloads/documentos_classificar/maquina_1',
    # '/Users/dambros/Downloads/documentos_classificar/maquina_2'
    '/Users/dambros/Downloads/documentos_classificar/mario'
]
XML_FOLDER_PATH = '/Users/dambros/Downloads/documentos_classificar/xml/'
SUMMARY_PATH = '/Users/dambros/Downloads/documentos_classificar/xml/summary'
DB_PATH = './res/db'
FIRST_PAGE_PARAGRAPHS = 10
ROOT_CATEGORIES = {
    'Relatório Voto': ['relatório voto', 'é o voto'],
    'Decisão Singular': ['decisão singular', 'é a decisão'],
    'Despacho': ['despacho']
}
SUB_CATEGORIES = {
    'Relatório Voto': {
        'Ata': ['ata'],
        'Contrato': ['contrato administrativo'],
        'Contrato Obra': ['contrato de obra'],
        'Pessoal': ['ato de pessoal', 'atos de pessoal', 'ato', 'atos',
                    'concessão', 'pensão', 'aposentadoria'],
        'Auditoria': ['auditoria']
    },
    'Decisão Singular': {
        'Ata': ['ata'],
        'Contrato': ['contrato administrativo'],
        'Contrato Obra': ['contrato de obra'],
        'Pessoal': ['ato de pessoal', 'atos de pessoal', 'ato', 'atos',
                    'concessão', 'pensão', 'aposentadoria'],
        'Convênio': ['convênio']
    }
}
