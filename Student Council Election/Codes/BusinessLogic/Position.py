#!/usr/bin/env python

#import modules
from enum import Enum, unique

#definitions for positions in a student council in Mapua University
@unique
class Position(Enum):
    REPRESENTATIVE_CSC = 0
    PRESIDENT = 1
    VICE_PRESIDENT_INT = 2
    VICE_PRESIDENT_EXT = 3
    SECRETARY_EXECUTIVE = 4
    SECRETARY_FINANCE = 5
    SECRETARY_AUDIT = 6
    SECRETARY_LOGISTICS = 7
    SECRETARY_BUDGET_MANAGEMENT = 8
    SECRETARY_SCHOLARSHIP = 9
    SECRETARY_INFO_CORRESPONDENCE = 10
    SECRETARY_AMUSEMENT_RECREATION = 11
    SECRETARY_WELFARE_DEV = 12
    REPRESENTATIVE_4TH_YEAR = 13
    REPRESENTATIVE_3RD_YEAR = 14
    REPRESENTATIVE_2ND_YEAR = 15
    REPRESENTATIVE_GENERAL = 16
    BUSINESS_MANAGER = 17