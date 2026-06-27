import csv
from pathlib import Path

from openpyxl import Workbook


def export_to_csv(results, output_path):
    file_path = Path(output_path)

    with file_path.open(mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["file", "status", "rule", "field", "target", "message"])

        for result in results:
            if len(result["errors"]) == 0:
                writer.writerow(
                    [
                        result["file"],
                        result["status"],
                        "",
                        "",
                        "",
                        "",
                    ]
                )
            else:
                for error in result["errors"]:
                    writer.writerow(
                        [
                            result["file"],
                            result["status"],
                            error["rule"],
                            error["field"],
                            error["target"],
                            error["message"],
                        ]
                    )


def export_to_excel(results, output_path):
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["file", "status", "rule", "field", "target", "message"])

    for result in results:
        if len(result["errors"]) == 0:
            sheet.append(
                [
                    result["file"],
                    result["status"],
                    "",
                    "",
                    "",
                    "",
                ]
            )
        else:
            for error in result["errors"]:
                sheet.append(
                    [
                        result["file"],
                        result["status"],
                        error["rule"],
                        error["field"],
                        error["target"],
                        error["message"],
                    ]
                )

    workbook.save(output_path)
