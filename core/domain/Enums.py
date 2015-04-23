__author__ = 'Dzianis_Shender'

def enum(**enums):
    return type('Enum', (), enums)

errorLayers = enum(SERVER_SIDE='SERVER_SIDE', RWI='RWI')
reportInitiators = enum(USER='USER', SUPPRESSED_ERROR='SUPPRESSED_ERROR')

