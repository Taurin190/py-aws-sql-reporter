import openpyxl


class StoreExcel:
    @staticmethod
    def create_sheet(name):
        wb = openpyxl.Workbook()
        if not name.endsWith(".xlsx"):
            name += ".xlsx"
        wb.save('tmp/' + name)
