from utils import rupiah


def test_rupiah_format_kecil():
    assert rupiah(15000) == "Rp15.000"

def test_rupiah_format_besar():
    assert rupiah(1250000) == "Rp1.250.000"