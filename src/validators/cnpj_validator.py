def validate_cnpj(nfe_data):
    issuer = nfe_data["issuer"]
    recipient = nfe_data["recipient"]
    issuer_cnpj = issuer["cnpj"]
    recipient_cnpj = recipient["cnpj"]
    
    errors = []

    if len(issuer_cnpj) != 14:
        errors.append(f"Emitente: CNPJ inválido ({issuer_cnpj})")

    if len(recipient_cnpj) != 14:
        errors.append(f"Destinatário: CNPJ inválido ({recipient_cnpj})")

    return errors