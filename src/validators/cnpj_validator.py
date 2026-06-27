def validate_cnpj(nfe_data):
    issuer = nfe_data["issuer"]
    recipient = nfe_data["recipient"]

    issuer_cnpj = issuer["cnpj"]
    recipient_cnpj = recipient["cnpj"]

    errors = []

    if len(issuer_cnpj) != 14:
        errors.append(
            {
                "rule": "CNPJ",
                "field": "CNPJ",
                "target": "Emitente",
                "message": f"CNPJ {issuer_cnpj} inválido.",
            }
        )

    if len(recipient_cnpj) != 14:
        errors.append(
            {
                "rule": "CNPJ",
                "field": "CNPJ",
                "target": "Destinatário",
                "message": f"CNPJ {recipient_cnpj} inválido.",
            }
        )

    return errors
