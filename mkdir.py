from pathlib import Path

arquivos = [
    "data/input/nfe_ok.xml",
    "data/input/nfe_cnpj_invalido.xml",
    "data/input/nfe_cfop_invalido.xml",
    "data/input/nfe_total_divergente.xml",
    "data/input/nfe_campo_ausente.xml",
    "data/output/inconsistencias.csv",
    "data/output/inconsistencias.xlsx",
    "src/parser/nfe_parser.py",
    "src/validators/xml_validator.py",
    "src/validators/cnpj_validator.py",
    "src/validators/cfop_validator.py",
    "src/validators/ncm_validator.py",
    "src/validators/total_validator.py",
    "src/reports/report_generator.py",
    "src/config/fiscal_rules.py",
    "src/models/nfe_model.py",
    "tests/__init__.py",
    "main.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
]

raiz = Path("nfe-validator")

for arquivo in arquivos:
    caminho = raiz / arquivo
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.touch(exist_ok=True)

print("Estrutura criada com sucesso.")