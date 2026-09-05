import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def rupiah(amount: int) -> str:
    """Format angka int menjadi string Rupiah contoh 15000 -> Rp15.000"""
    return f"Rp{amount:,.0f}".replace(",", ".")