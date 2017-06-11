from openpyxl import load_workbook
from openpyxl.worksheet import Worksheet


class ExcelSheet(object):
    def __init__(self, ws: Worksheet):
        self._ws = ws

    def load_value(self, column_name):
        res = []
        tar_column_index = -1
        combine_value = None
        for row in self._ws:
            for cell in row:
                if cell.value == column_name:
                    tar_column_index = cell.col_idx
                    continue
                if tar_column_index != -1:
                    if cell.col_idx == tar_column_index:
                        if cell.value is not None:
                            res.append(cell.value)
                            combine_value = cell.value
                        elif cell.value is None and combine_value is not None:
                            res.append(combine_value)
                            combine_value == None
                        else:
                            pass
        return res

    def locate(self, column_name, row_search_value, column_search_value):
        res = []
        column_index = -1
        column_search_index = -1
        head_row_founded = False
        for row in self._ws:
            for cell in row:
                if cell.value == column_name:
                    column_index = cell.col_idx
                if cell.value == column_search_value:
                    column_search_index = cell.col_idx
                if column_index != -1 and column_search_index != -1:
                    head_row_founded = True
                    continue
                if head_row_founded:
                    if cell.col_idx == column_index:
                        if cell.value == row_search_value:
                            res.append((cell.row, cell.col_index))
        return res


def load_excel_by_sheet(f_p, sheet):
    wb = load_workbook(f_p)
    ws = None
    if wb[sheet]:
        ws = wb[sheet]
    return ExcelSheet(ws)


if __name__ == "__main__":
    excel_sheet = load_excel_by_sheet("/Users/chujiwu/Desktop/test.xlsx", "工作表1")
    excel_sheet.load_value("フォーム名")
