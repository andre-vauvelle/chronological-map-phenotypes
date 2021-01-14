import os
import pandas as pd 

secondary_care_files = os.listdir('./secondary_care/')

csv_store = [] 
for f in secondary_care_files:
    df = pd.read_csv(os.path.join('secondary_care', f))
    csv_store.append(df)

secondary_care_df = pd.concat(csv_store)
secondary_care_df.ICD10code = secondary_care_df.ICD10code.str.replace('.','')
secondary_care_df.OPCS4code = secondary_care_df.OPCS4code.str.replace('.','')

secondary_care_df = secondary_care_df.reset_index(drop=True)

secondary_care_df.to_csv('caliber_secondary_care_dict.csv', index=False)

