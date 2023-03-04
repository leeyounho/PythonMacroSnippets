import pandas as pd
import xlwings as xw

from file.file_manager import FileManager


class DataFrameManager:
    def __init__(self):
        self.writer = None

    # TODO 미완성
    def write_dataframe_to_excel(self, df, sheet_name):
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
            wb.sheets['temp'].range('A1').expand('right').font.bold = True  # bold header
            wb.sheets['temp'].range('A1').expand('right').color = '#A9A9A9'  # color header
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

    # split dataframe to multi dataframe dict. delimiter is key. index will be reset
    def df_split_to_df_dict(self, df_to_split, delimiter_column_name):
        # set the index to be this and don't drop
        if delimiter_column_name not in df_to_split.columns:
            return {}

        df_to_split.set_index(keys=[delimiter_column_name], drop=False, inplace=True)

        # get a list of names
        value_list = df_to_split[delimiter_column_name].unique().tolist()

        # 합치기
        ret_dict = {}
        for value in value_list:
            df_split = df_to_split.loc[df_to_split[delimiter_column_name] == value]
            ret_dict[value] = df_split
        return ret_dict

    def split_and_explode_df_by_delimiter(self, df, column, delimiter):
        df[column] = df[column].str.split(delimiter)  # split str to list
        return df.explode('B', ignore_index=True)  # explode list

    # TODO
    # compare 2 dataframe and return diff dataframe.
    # panastable애 hightlight, export 할 때도 highlight 할거 고려
    # https://stackoverflow.com/questions/71604701/pandas-compare-two-data-frames-and-highlight-the-differences
    def df_compare_to_diff_df(self, df_left, df_right):
        return df_left.compare(df_right)


if __name__ == '__main__':
    dfm = DataFrameManager()
    # df1 = pd.DataFrame({
    #     "A": [1, 2, 3],
    #     "B": ["apple\nfggffg\nfgfgdzdsf\n", "berry", "grapes"],
    #     "C": ["red", "blue", "green"]
    # },
    #     columns=["A", "B", "C"])
    #
    # df2 = pd.DataFrame({
    #     "A": [1, 2, 3],
    #     "B": ["apple", "guava", "banana"],
    #     "C": ["green", "blue", "green"]
    # },
    #     columns=["A", "B", "C"])
    #
    # print(df1)
    # print()
    # print(df2)
    # print()
    #

    # df3 = dfm.df_compare_to_diff_df(df1, df2)
    # print(df3)



