from src.config.fiscal_rules import VALID_CFOPS


def validate_cfop(nfe_data):
    products = nfe_data["products"]
    errors = []

    for product in products:
        cfop = product["product_cfop"]

        if cfop is None:
            errors.append(
                {
                    "rule": "CFOP",
                    "field": "CFOP",
                    "target": product["product_name"],
                    "message": "CFOP não informado.",
                }
            )
            continue

        if cfop not in VALID_CFOPS:
            errors.append(
                {
                    "rule": "CFOP",
                    "field": "CFOP",
                    "target": product["product_name"],
                    "message": f"CFOP {cfop} inválido.",
                }
            )

    return errors
