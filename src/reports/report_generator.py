import csv
from pathlib import Path


def export_to_csv(results, output_path):
    file_path = Path(output_path)

    with file_path.open(mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["file", "status", "errors"])

        for result in results:
            writer.writerow(
                [
                    result["file"],
                    result["status"],
                    "; ".join(result["errors"]),
                ]
            )
