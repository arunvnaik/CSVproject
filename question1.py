import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1FXmmFDS0r6SNE1ZPizrwYjNRC4ZgnCC_M4WcNCVGp0U/export?format=csv' , on_bad_lines='skip')

print("print df data----->",df.to_string())
