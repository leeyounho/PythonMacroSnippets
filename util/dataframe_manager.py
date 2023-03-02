import pandas as pd
import xlwings as xw

from file.file_manager import FileManager


# TODO xlwings로 바꿔야겠다..
class DataFrameManager:
    def __init__(self):
        self.writer = None

    def write_dataframe_to_excel(self, df, sheet_name):
        # TODO 줄바꿈 없애고, index 살려야함
        # style 정의
        # df = df.style.set_table_styles(
        #     [{
        #         'selector': 'th',
        #         'props': [
        #             ('border', '1.3px solid black'),
        #             ('font-size', '9pt'),
        #             ('background-color', 'black'),
        #             ('color', 'cyan')]
        #     }])
        styled_df = df.style.set_properties(
            **{'border': '1.3px solid black', 'font-size': '9pt', 'text-align': 'center', 'vertical-align': 'middle'})

        # df = df.set_table_styles(
        #     select the table header with th and set it right align
        # [dict(selector="th", props=[("text-align", "right")])]
        # )

        if self.writer is not None:
            styled_df.to_excel(self.writer, sheet_name=sheet_name)

    def make_excel_writer(self, excel_file_name):
        self.writer = pd.ExcelWriter(excel_file_name)

    def close_excel_writer(self):
        if self.writer is not None:
            self.writer.close()


if __name__ == '__main__':
    df = pd.DataFrame(
        {'Data': ['234324325refgergdfgdfgdfgfdgsdfjgearhjkgelrhfkjshdkfjsdlfwsefesfsefsefse', 22, 23, 24]})

    file_manager = FileManager()
    save_file_name = file_manager.ask_save_file_name()

    with xw.App(visible=False) as app:
        wb = xw.Book()

        # create sheet
        wb.sheets.add('temp')

        # write dataframe
        wb.sheets['temp']['A1'].value = df
        wb.sheets['temp'].range('A1').expand('right').font.bold = True # bold header
        wb.sheets['temp'].range('A1').expand('right').color = '#A9A9A9' # color header
        wb.sheets['temp'].range('A1').expand('table').api.Borders.LineStyle = 1  # border
        wb.sheets['temp'].range('A1').expand(
            'table').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignLeft  # left align
        # wb.sheets['temp'].range('A1').expand(
        #     'table').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignCenter  # center align
        wb.sheets['temp'].range('A1').expand('table').font.size = 9  # font 9
        wb.sheets['temp'].autofit(axis="columns")  # autofit

        # delete default sheets
        wb.sheets['sheet1'].delete()
        wb.sheets['sheet2'].delete()
        wb.sheets['sheet3'].delete()

        # excel 저장
        wb.save(save_file_name)
        wb.close()

    # dataframe_manager = DataFrameManager()
    # dataframe_manager.make_excel_writer('test_excel.xlsx')
    # dataframe_manager.write_dataframe_to_excel(df2, sheet_name='df2_test_sheet')
    # dataframe_manager.close_excel_writer()
