import pandas as pd


# sort the dataframe
# df.sort_values(by='target_database', axis=1, inplace=True)

# split dataframe to multi dataframe dict. delimiter is key. index will be reset
def df_split_to_df_dict(df_to_split, delimiter_column_name):
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


df2 = pd.DataFrame({'target_database': ['S3', '17', 'P1', 'U1'],
                    'value1': ['fdgdfg', 'dfgfdghdfhsdfhsdfgsdfgsdfgksjldfhgslkjer5hgljekrgjlsergsergsregsreg', 0, 0],
                    'value2': ['788\njkgukg\nhhjhjjh\n', 'fdgdfg', 1, 0]},
                   index=['falcon', 'dog', 'spider', 'fish'])

print(type(df_split_to_df_dict(df2, 'temp')))
