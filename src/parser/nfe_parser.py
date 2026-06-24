import xml.etree.ElementTree as ET


def get_tag_text(parent, tag):
    element = parent.find(tag)
    return element.text if element is not None else None


def get_xml_root(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()


def get_issuer_data(inf_nfe):
    emit = inf_nfe.find("emit")

    cnpj = get_tag_text(emit, "CNPJ")
    nome = get_tag_text(emit, "xNome")
    ie = get_tag_text(emit, "IE")

    return {
        "cnpj": cnpj,
        "company_name": nome,
        "state_registration": ie,
    }


def get_recipient_data(inf_nfe):
    dest = inf_nfe.find("dest")

    cnpj = get_tag_text(dest, "CNPJ")
    nome = get_tag_text(dest, "xNome")

    return {
        "cnpj": cnpj,
        "company_name": nome,
    }


def get_products_data(inf_nfe):
    products = inf_nfe.findall("det")
    products_data = []

    for item in products:
        prod = item.find("prod")

        product_code = get_tag_text(prod, "cProd")
        product_name = get_tag_text(prod, "xProd")
        product_ncm = get_tag_text(prod, "NCM")
        product_cfop = get_tag_text(prod, "CFOP")
        product_quantity = get_tag_text(prod, "qCom")
        product_value = get_tag_text(prod, "vProd")

        products_data.append(
            {
                "product_code": product_code,
                "product_name": product_name,
                "product_ncm": product_ncm,
                "product_cfop": product_cfop,
                "product_quantity": product_quantity,
                "product_value": product_value,
            }
        )

    return products_data


def get_total_data(inf_nfe):
    total = inf_nfe.find("total")
    icms = total.find("ICMSTot") if total is not None else None

    products_total = get_tag_text(icms, "vProd") if icms is not None else None
    invoice_total = get_tag_text(icms, "vNF") if icms is not None else None

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
