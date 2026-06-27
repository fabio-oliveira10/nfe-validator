from src.config.fiscal_rules import VALID_NCM_PREFIXES


def validate_ncm(nfe_data):
    products = nfe_data["products"]
    errors = []

    for product in products:
        ncm = product["product_ncm"]

        if ncm is None:
            errors.append(
                {
                    "rule": "NCM",
                    "field": "NCM",
                    "target": product["product_name"],
                    "message": "NCM não informado.",
                }
            )
            continue

        if not any(ncm.startswith(prefix) for prefix in VALID_NCM_PREFIXES):
            errors.append(
                {
                    "rule": "NCM",
                    "field": "NCM",
                    "target": product["product_name"],
                    "message": f"NCM {ncm} inválido.",
                }
            )

    return errors
