import pandas as pd


class DataFrameManager:
    def __init__(self):
        self.writer = None

    def write_dataframe_to_excel(self, df, sheet_name):
        if self.writer is not None:
            df.to_excel(self.writer, sheet_name=sheet_name)

    def make_excel_writer(self, excel_file_name, engine='xlsxwriter'):
        self.writer = pd.ExcelWriter(excel_file_name, engine=engine)

    def close_excel_writer(self):
        if self.writer is not None:
            self.writer.close()


if __name__ == '__main__':
    df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
    df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
    df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})

    dataframe_manager = DataFrameManager()
    dataframe_manager.make_excel_writer('test_excel.xlsx')
    dataframe_manager.write_dataframe_to_excel(df1, sheet_name='df1_test_sheet')
    dataframe_manager.write_dataframe_to_excel(df2, sheet_name='df2_test_sheet')
    dataframe_manager.close_excel_writer()
