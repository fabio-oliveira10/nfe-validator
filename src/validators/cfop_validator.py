from src.config.fiscal_rules import VALID_CFOPS


def validate_cfop(nfe_data):
    products = nfe_data["products"]
    errors = []

    for product in products:
        cfop = product["product_cfop"]

        if cfop is None:
            errors.append(f"{product['product_name']}: CFOP não informado.")
            continue

        if cfop not in VALID_CFOPS:
            errors.append(f"{product['product_name']}: CFOP {cfop} inválido.")

    return errors
