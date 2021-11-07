
class ExcelHandler:
    def __init__(self, file_path: str):
        self.path = file_path

    def value_from_sheets(self):
        ...

    def value_by_column(self, sheet_name: str, col_name: str):
        ...

