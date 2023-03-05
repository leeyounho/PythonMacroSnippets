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
        temp_df = df_to_split.copy()

        # set the index to be this and don't drop
        if delimiter_column_name not in temp_df.columns:
            return {}

        temp_df.set_index(keys=[delimiter_column_name], drop=False, inplace=True)

        # get a list of names
        value_list = temp_df[delimiter_column_name].unique().tolist()

        # 합치기
        ret_dict = {}
        for value in value_list:
            df_split = temp_df.loc[temp_df[delimiter_column_name] == value]
            ret_dict[value] = df_split
        return ret_dict

    def split_and_explode_df_by_delimiter(self, df, column, delimiter):
        df[column] = df[column].str.split(delimiter)  # split str to list
        return df.explode(column, ignore_index=True)  # explode list

    def df_compare_by_merge(self, df_left, df_right, except_column_name_list=[]):
        df_left_copied = df_left.copy()
        df_right_copied = df_right.copy()
        return df_left_copied.merge(df_right_copied,
                                    on=self.get_column_list_without(df_left_copied, except_column_name_list),
                                    indicator='diff', how='outer')

    def df_compare_by_drop_and_merge(self, df_left, df_right, except_column_name_list=[]):
        df_left_drop = df_left.drop(columns=except_column_name_list)
        df_right_drop = df_right.drop(columns=except_column_name_list)
        return df_left_drop.merge(df_right_drop, on=df_left_drop.columns.to_list(), indicator='diff', how='outer')

    def get_column_list_without(self, df, column_name_list):
        return df.columns.difference(column_name_list).tolist()


if __name__ == '__main__':
    dfm = DataFrameManager()
    df1 = pd.DataFrame({
        "A": [1, 2, 3],
        "B": ["apple\nfggffg\nfgfgdzdsf\n", "berry", "grapes"],
        "C": ["red", "blue", "green"]
    },
        columns=["A", "B", "C"])

    df2 = pd.DataFrame({
        "A": [1, 2, 3],
        "B": ["apple", "berry", "banana"],
        "C": ["green", "blue", "green"]
    },
        columns=["A", "B", "C"])

    print(df1)
    print()

    print(df2)
    print()

    df_diff_1 = dfm.df_compare_by_merge(df1, df2, ['A'])
    print(df_diff_1)
    print()

    df_diff_2 = dfm.df_compare_by_drop_and_merge(df1, df2, ['A'])
    print(df_diff_2)
    print()
    # df_diff = df_diff.style.highlight_null()
