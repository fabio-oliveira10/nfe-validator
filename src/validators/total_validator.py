from decimal import Decimal


def validate_nfe_totals(nfe_data):
    products = nfe_data["products"]
    total = nfe_data["total"]
    sum_products = Decimal("0.00")

    for item in products:
        value = Decimal(item["product_value"])
        sum_products += value

    invoice_total = Decimal(total["invoice_total"])
    difference = abs(sum_products - invoice_total)

    return {
        "status": "OK" if difference <= Decimal("0.01") else "ERROR",
        "difference": difference,
        "calculated_total": sum_products,
        "declared_total": invoice_total,
    }
