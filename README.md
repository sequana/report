# sequana_report

Shared HTML report generation infrastructure for Sequana.

This package provides the base classes, templates, and utilities used by the Sequana ecosystem to generate consistent, professional HTML reports.

## Features

- **SequanaBaseModule**: Base class for all report generators
- **Jinja2 Templates**: Standard and customizable HTML report templates
- **CSS/JS Assets**: Bootstrap, jQuery, DataTables, Plotly integration
- **Utilities**: DataTable, CanvasJS line graphs for interactive visualizations

## Installation

```bash
pip install sequana_report
```

## Usage

```python
from sequana_report import SequanaBaseModule

class MyReport(SequanaBaseModule):
    def __init__(self, data):
        super().__init__()
        self.title = "My Report"
        self.sections = [
            {"name": "Overview", "anchor": "overview", "content": "<p>Hello</p>"}
        ]
        self.create_html("my_report.html")
```

## Dependencies

- Jinja2 >= 3.0
- pandas >= 1.0
- colorlog >= 6.0

## License

BSD-3-Clause
