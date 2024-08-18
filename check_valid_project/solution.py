import pandas as pd


def check_valid_project(cadena: str):
    try:
        if cadena.startswith("FONDOS") or cadena.startswith("FONDO") or cadena.startswith("Fondo") or cadena.startswith(
                "Rendición") or cadena.startswith("Preciado") or cadena.startswith("COMISIONES") or cadena.startswith(
            "Comisiones") or cadena.startswith("REGI"):
            return cadena
        if cadena.startswith("PROYECTO "):
            cadena = cadena.replace("PROYECTO ", "")
        if cadena.startswith("PROY "):
            cadena = cadena.replace("PROY ", "")

        if "," in cadena:
            cadena = cadena.replace(",", " ")
        parts = cadena.split('-')
        if ' ' in parts[0]:
            project_code = parts[0].replace(' ', '-') + '-' + parts[1]
        else:
            project_code = '-'.join(parts[:3])

        project_code = project_code.split(' ')[0]

        return project_code.strip()
    except Exception as e:
        pass


def clean_xlsx(chain: str):
    if isinstance(chain, float):
        return chain
    if chain.startswith("Rendición"):
        chain = chain.split(" ")

        chain = chain[-2:]

        chain = "".join(chain)

    return chain.strip().replace(".", "")


def read_xlsx(file):
    df = pd.read_excel(file, sheet_name='CONSOLIDADO', engine='openpyxl')

    print("Columnas en la hoja 'CONSOLIDADO':", df.columns)
    df['CODIGO PROYECTO'] = df['CODIGO PROYECTO'].apply(check_valid_project)

    df.to_excel(file, index=False)


def update_excel_sheet(file_path, sheet_name: str):
    with pd.ExcelFile(file_path, engine='openpyxl') as xls:

        sheets = xls.sheet_names
        print("Sheets in the file:", sheets)
        df_dict = pd.read_excel(xls, sheet_name=None)

    if sheet_name in df_dict:
        df = df_dict[sheet_name]
        print("Columns in the sheet:", df.columns)
        if 'CODIGO PROYECTO' in df.columns:
            df['CODIGO PROYECTO'] = df['CODIGO PROYECTO'].apply(clean_xlsx)

        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            for sheet in sheets:
                if sheet == sheet_name:
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                else:
                    df_dict[sheet].to_excel(writer, sheet_name=sheet, index=False)

    else:
        print(f"Sheet '{sheet_name}' not found in the file.")


file = "file path"
update_excel_sheet(file, "CONSOLIDADO")
