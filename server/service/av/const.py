from enum import Enum, auto

class AV_Function(Enum):
    INTRADAY            = auto()
    DAILY               = auto()
    DAILY_ADJUSTED      = auto()
    WEEKLY              = auto()
    WEEKLY_ADJUSTED     = auto()
    MONTHLY             = auto()
    MONTHLY_ADJUSTED    = auto()
    LATEST              = auto()
    SEARCH              = auto()

AV_Function_param_map = {
    AV_Function.INTRADAY:           'TIME_SERIES_INTRADAY',
    AV_Function.DAILY:              'TIME_SERIES_DAILY',
    AV_Function.DAILY_ADJUSTED:     'TIME_SERIES_DAILY_ADJUSTED',
    AV_Function.WEEKLY:             'TIME_SERIES_WEEKLY',
    AV_Function.WEEKLY_ADJUSTED:    'TIME_SERIES_WEEKLY_ADJUSTED',
    AV_Function.MONTHLY:            'TIME_SERIES_MONTHLY',
    AV_Function.MONTHLY_ADJUSTED:   'TIME_SERIES_MONTHLY_ADJUSTED',
    AV_Function.LATEST:             'GLOBAL_QUOTE',
    AV_Function.SEARCH:             'SYMBOL_SEARCH',
}
