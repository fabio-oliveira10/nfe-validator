from pathlib import Path

from src.parser.nfe_parser import get_xml_root, parse_nfe
from src.validators.total_validator import validate_nfe_totals
from src.validators.cfop_validator import validate_cfop
from src.reports.report_generator import export_to_csv
from src.validators.cnpj_validator import validate_cnpj
from src.validators.ncm_validator import validate_ncm


input_folder = Path("data/input")
xml_files = list(input_folder.glob("*.xml"))

results = []

for file in xml_files:
    root = get_xml_root(str(file))
    nfe_data = parse_nfe(root)

    total_validation = validate_nfe_totals(nfe_data)
    cfop_errors = validate_cfop(nfe_data)
    cnpj_errors = validate_cnpj(nfe_data)
    ncm_errors = validate_ncm(nfe_data)
    errors = []

    # transforma validação de total em erro (se necessário)
    if total_validation["status"] == "ERROR":
        errors.append(
            f"Divergência de total: diferença {total_validation['difference']}"
        )

    # adiciona erros de CFOP
    errors.extend(cfop_errors)
    # adiciona erros de CNPJ
    errors.extend(cnpj_errors)
    # adiciona erros de NCM
    errors.extend(ncm_errors)

    results.append(
        {
            "file": file.name,
            "status": "OK" if len(errors) == 0 else "ERROR",
            "errors": errors,
        }
    )

total_files = len(results)
ok_files = sum(1 for r in results if r["status"] == "OK")
error_files = sum(1 for r in results if r["status"] == "ERROR")
success_rate = (ok_files / total_files) * 100 if total_files > 0 else 0

export_to_csv(results, "data/output/inconsistencias.csv")

print("\nRESUMO FINAL")
print(f"Total de arquivos: {total_files}")
print(f"OK: {ok_files}")
print(f"ERROR: {error_files}")
print(f"Taxa de aprovação: {success_rate:.2f}%")
