# -*- coding: utf-8 -*-
import glob
import json
import logging.config
import os
import re
from datetime import datetime
from itertools import islice
from xml.dom.minidom import parseString

import dicttoxml
from dateutil.parser import parse
from docx import Document

import config


def cli():
    """

    Script responsável por classificar documentos do tipo docx baseado nas regras
    fornecidas pelo TCE e escrever tais categorias em um XML respeitando o mesmo
    path do arquivo original.

           classifier.py classify

       For detailed help, try this:

           classifier.py classify --help
       """
    pass


def classify():
    doc_lists = []
    for doc_path in config.SHARED_FOLDER_PATHS:
        path = get_path(doc_path, 'docx')
        doc_lists.append(glob.glob(path, recursive=True))

    last_index_date = get_last_index_date()

    result = {}
    for doc_list in doc_lists:
        if last_index_date:
            filter_files_after(doc_list, last_index_date)

        if doc_list:
            for doc in doc_list:
                root_category = get_root_category(doc)
                result[doc] = {'parent': root_category}
                if root_category not in ['Geral', 'Despacho']:
                    sub_category = get_sub_category(doc, root_category)
                    if sub_category:
                        result[doc]['child'] = sub_category

            write_xml(result)
            write_file(config.SUMMARY_PATH,
                       json.dumps(result, indent=1, ensure_ascii=False))
            save_current_modification_date()


def write_xml(result):
    for name, value in result.items():
        xml_path = re.sub(r'^/', '', re.sub(r'docx$', 'xml', name))
        xml_path = os.path.join(config.XML_FOLDER_PATH, xml_path)
        categories = {'categories': value}
        xml = dicttoxml.dicttoxml(categories, attr_type=False)
        dom = parseString(xml)
        write_file(xml_path, dom.toprettyxml())


def write_file(filename, content):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'w') as file:
        file.write(content)
        file.close()


def get_root_category(doc_path):
    document = Document(doc_path)
    paragraphs = document.paragraphs

    start_paragraphs = islice(paragraphs, config.FIRST_PAGE_PARAGRAPHS)
    for p in start_paragraphs:
        text = p.text.lower()
        if text:
            for name, values_list in config.ROOT_CATEGORIES.items():
                if values_list[0].lower() in text:
                    return name

    reversed_paragraphs = reversed(paragraphs)
    last_paragraphs = islice(reversed_paragraphs, 20)
    for p in last_paragraphs:
        text = p.text.lower()
        if text:
            for name, values_list in config.ROOT_CATEGORIES.items():
                if values_list[-1].lower() in text:
                    return name

    return 'Geral'


def get_sub_category(doc_path, root_category):
    document = Document(doc_path)
    paragraphs = document.paragraphs

    start_paragraphs = islice(paragraphs, config.FIRST_PAGE_PARAGRAPHS)
    for p in start_paragraphs:
        text = p.text.lower()
        if text:
            for root, subs in config.SUB_CATEGORIES[root_category].items():
                if any(sub_category in text for sub_category in subs):
                    return root


def get_last_index_date():
    if os.path.isfile(config.DB_PATH):
        with open(config.DB_PATH, 'r') as f:
            last_date = f.read()
            return parse(last_date)

    return None


def save_current_modification_date():
    with open(config.DB_PATH, 'w+') as f:
        curr_time = datetime.now().isoformat()
        f.write(curr_time)


def filter_files_after(files, last_modified_date):
    for file in files[:]:
        file_modified_date = datetime.fromtimestamp(os.path.getmtime(file))
        if last_modified_date > file_modified_date:
            files.remove(file)


def get_path(folder, extension):
    path = f'{folder}/**/*.{extension}'
    return path


if __name__ == "__main__":
    logging.config.fileConfig(config.LOG_CONFIG_PATH)
    logger = logging.getLogger(os.path.basename(__file__))
    classify()
