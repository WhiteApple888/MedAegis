import pandas as pd

def get_item(target_item : str, retail_prescribable_list_path : str) -> pd.DataFrame:
    # 1. Load the dataset
    retail_prescribable_list = pd.read_csv(retail_prescribable_list_path)
    
    # 2. Clean dataframe
    retail_prescribable_list = retail_prescribable_list.dropna(subset=['ITEM DESCRIPTION'])
    retail_prescribable_list['ITEM DESCRIPTION'] = retail_prescribable_list['ITEM DESCRIPTION'].astype(str).str.upper()


    # 3. Filter rows where target_item is contained in ITEM DESCRIPTION
    matching_rows = retail_prescribable_list[
        retail_prescribable_list["ITEM DESCRIPTION"].str.contains(
            target_item.upper(), regex=False, na=False
        )
    ]

    # 4. Sort alphabetically by ITEM DESCRIPTION
    matching_rows = matching_rows.sort_values(
        by="ITEM DESCRIPTION", ascending=True
    )

    return matching_rows