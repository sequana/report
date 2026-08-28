import sequana_report


def test_import():
    assert sequana_report.__version__ is not None


def test_sequana_base_module_import():
    from sequana_report import SequanaBaseModule

    assert SequanaBaseModule is not None


def test_datatables_import_without_sequana_dependency():
    import subprocess
    import sys

    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from sequana_report.utils.datatables_js import DataTable, DataTableFunction; print('ok')",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "ok"
