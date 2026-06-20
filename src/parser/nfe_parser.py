from itertools import product
import xml.etree.ElementTree as ET


def get_xml_root(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


root = get_xml_root("data/input/nfe_ok.xml")


def get_issuer_data(inf_nfe):
    emit = inf_nfe.find("emit")
    cnpj = emit.find("CNPJ").text
    nome = emit.find("xNome").text
    ie = emit.find("IE").text

    return {
        "cnpj": cnpj,
        "company_name": nome,
        "state_registration": ie,
    }


def get_recipient_data(inf_nfe):
    dest = inf_nfe.find("dest")
    cnpj = dest.find("CNPJ").text
    nome = dest.find("xNome").text

    return {
        "cnpj": cnpj,
        "company_name": nome,
    }


def get_products_data(inf_nfe):
    products = inf_nfe.findall("det")
    products_data = []

    for item in products:
        prod = item.find("prod")
        product_code = prod.find("cProd").text
        product_name = prod.find("xProd").text
        product_ncm = prod.find("NCM").text
        product_cfop = prod.find("CFOP").text
        product_quantity = prod.find("qCom").text
        product_value = prod.find("vProd").text
        product_data = {
            "product_code": product_code,
            "product_name": product_name,
            "product_ncm": product_ncm,
            "product_cfop": product_cfop,
            "product_quantity": product_quantity,
            "product_value": product_value,
        }
        products_data.append(product_data)
    return products_data


def get_total_data(inf_nfe):
    total = inf_nfe.find("total")
    icms = total.find("ICMSTot")
    products_total = icms.find("vProd").text
    invoice_total = icms.find("vNF").text

    return {
        "products_total": products_total,
        "invoice_total": invoice_total,
    }


def parse_nfe(root):
    inf_nfe = root.find("infNFe")
    issuer_data = get_issuer_data(inf_nfe)
    recipient_data = get_recipient_data(inf_nfe)
    products_data = get_products_data(inf_nfe)
    total_data = get_total_data(inf_nfe)

    return {
        "issuer": issuer_data,
        "recipient": recipient_data,
        "products": products_data,
        "total": total_data,
    }

nfe_data = parse_nfe(root)

