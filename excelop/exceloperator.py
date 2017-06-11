from openpyxl import load_workbook
from openpyxl.cell import Cell
from openpyxl.workbook import Workbook
from openpyxl.worksheet import Worksheet



class Excel(object):
    def __init__(self, ws: Worksheet):
        self._ws = ws

    def load_value(self, column_name):
        res = []
        tar_column_index = -1
        for row in self._ws:
            for cell in row:
                if cell.value == column_name:
                    tar_column_index = cell.col_idx
                if tar_column_index != -1:
                    if cell.col_idx == tar_column_index:
                        res.append(cell.value)
        return res


def load_excel_by_sheet(f_p, sheet):
    wb = load_workbook(f_p)
    ws = None
    if wb[sheet]:
        ws = wb[sheet]
    return Excel(ws)


if __name__ == "__main__":
    excel = load_excel_by_sheet("/Users/chujiwu/Desktop/test.xlsx", "工作表1")
    excel.load_value("フォーム名")
