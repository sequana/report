import sequana_report


def test_import():
    assert sequana_report.__version__ is not None


def test_sequana_base_module_import():
    from sequana_report import SequanaBaseModule

    assert SequanaBaseModule is not None
