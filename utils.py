
def rupiah(amount):
    """
    Format angka int menjadi string Rupiah
    contoh 15000 -> Rp15.000
    """
    return f"Rp{amount:,.0f}".replace(",", ".")