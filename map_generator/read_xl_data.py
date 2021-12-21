import pandas as pd
from openpyxl import load_workbook
import os
from .utils import find_files_recursive, gen_col_range
from .config import (COL_INICIO,
                    COL_FIM,
                    HEADER_ROW,
                    DATA_ROW_RANGE,
                    DATA_SOURCE_DIR,
                    SAVE_CSV_DIR)

class XlDataReader:
    
    COL_INICIO = COL_INICIO
    COL_FIM = COL_FIM
    HEADER_ROW = HEADER_ROW
    DATA_ROW_RANGE = DATA_ROW_RANGE
    
    def __init__(self, lazy=True, file=None):

        if lazy and not file:
            raise ValueError(f'Se inicializar sem ser lazy, tem que passar o file')
        
        if not lazy:
            self.initialize(file=file)
            
    def list_data_sheets(self):
        
        data_sheets = [
            sheet
            for sheet in self.wb.sheetnames
            if sheet.lower().strip().endswith('indicador')
        ]
        
        return data_sheets
    
    
    def parse_sheet_name(self, name):
        
        new_name = name.lower().strip()
        
        splited = new_name.split(' ')
        
        secretaria = splited[0]
        meta = splited[1]
        meta = meta.replace('.', '_')
        
        return f'{secretaria}_{meta}'
    
    
    def parse_all_sheet_names(self, sheets):
        
        parsed = {self.parse_sheet_name(name) : name
                  for name in sheets}
        
        return parsed
    
    def get_sheet_names(self):
        
        data_sheets = self.list_data_sheets()
        
        return self.parse_all_sheet_names(data_sheets)
    
    def get_sheet(self, key):
        
        if key not in self.sheets:
            raise ValueError(f'Sheet {key} não encontrada no arquivo')
        
        return self.wb[self.sheets[key]]
    
    def get_cell_value(self, sheet, col, row):
        
        cell = f'{col}{row}'
        
        return sheet[cell].value
        
    def check_for_geo_data(self, sheet):
        
        #celula com o nome da primeira subprefeitura
        val = self.get_cell_value(
            sheet,
            self.COL_INICIO, 
            self.HEADER_ROW
        )
        
        if pd.isnull(val):
            return False
        elif val == '':
            return False
        val = val.lower().strip()
        
        if 'aricanduva' in val:
            return True
        return False
    
    
    def get_sub_name(self, sheet, col):
        
        
        val = self.get_cell_value(sheet,
                                   col, 
                                   self.HEADER_ROW)
        
        return val
    
    
    def parse_geo_data(self, sheet):
        
        
        col_range = self.gen_col_range(self.COL_INICIO, 
                                       self.COL_FIM)
        
        data = {}
        for col in col_range:
            sub_name = self.get_sub_name(sheet, col)
            data[sub_name] = []
            
            for row in range(*self.DATA_ROW_RANGE):
                
                val = self.get_cell_value(sheet, col, row)
                data[sub_name].append(val)
                
        return data
    
    def clean_geo_val(self, val):
        
        if pd.isnull(val):
            return float(0)
        if val == '':
            return float(0)
        
        val = str(val)
        val = val.replace('.', '')
        val = val.replace(',', '.')
        
        return float(val)
            
    
    def clean_geo_data(self, data):
        
        cleaned = {}
        
        for subs, vals in data.items():
            cleaned[subs] = []
            for val in vals:
                val = self.clean_geo_val(val)
                cleaned[subs].append(val)
                
        return cleaned
        
    
    def parse_all_geodata(self):
        
        all_data = {}
        for sheet_name in self.sheets.keys():
            sheet = self.get_sheet(sheet_name)
            if self.check_for_geo_data(sheet):
                data = self.parse_geo_data(sheet)
                clean_data = self.clean_geo_data(data)
                
                all_data[sheet_name] = clean_data
        
        return all_data

    def initialize(self, file):

        self.file = file
        self.gen_col_range = gen_col_range
        self.wb = load_workbook(file)
        self.sheets = self.get_sheet_names()

        self.initialized = True

    def __call__(self, file=None):

        file = file or getattr(self,'file', None)
        if file is None:
            raise ValueError('Lazy load: precisa passar o parametro file')
        
        if not self.initialized:
            self.initialize(file)

        return self.parse_all_geodata()

