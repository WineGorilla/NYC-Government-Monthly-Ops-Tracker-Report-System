# Global Variables
template_route = "./data/template.xlsx"

# Keywords
packer_features = ['COLLECTION TRUCK - 16 YD', 'COLLECTION TRUCK - 6 YD','COLLECTION TRUCK - 25 YD']
sedans_features = ['SEDAN']
suvs_features = ['SUV']
vans_features = ['VAN - PASSENGER', 'VAN - UTILITY']
pickups_features = ['VAN - PASSENGER', 'VAN - UTILITY']

Division_dict = {'DPAR-BRONX': 'BX',
 'DPAR-BROOKLYN': 'BK',
 'DPAR-MANHATTAN': 'MN',
 'DPAR-QUEENS': 'QN',
 'DPAR-STATEN ISLAND': 'SI',
 'DPAR-OFFICE OF ADMINISTRATION': 'Administration',
 'DPAR-CAPITAL PROJECTS': 'Capital Projects',
 'DPAR - CITYWIDE SERVICES': 'CWS',
 'DPAR-COMMUNICATIONS': 'Communications',
 'DPAR-COMPLIANCE': 'Compliance',
 'DPAR-EXECUTIVE': 'Executive',
 'DPAR-FLEET': 'Fleet',
 'DPAR - ENVIRONMENT AND PLANNING': 'Environment & Planning',
 'DPAR-GENERAL COUNSEL': 'General Counsel',
 'DPAR-IPM': 'IPM',
 'DPAR-LIFEGUARD': 'Lifeguards',
 'DPAR-STRAT COMMUNITY ENGAGMNT': 'Strat Community Engmt',
 'DPAR - BUSINESS & SPECIAL EVENTS': 'Business & Special',
 'DPAR-PUBLIC PROGRAMS': 'Public Programs',
 'DPAR-URBAN PARKS SERVICE': 'Urban Park Service'}

No_dict = ['NOT CAPTURED','NOT DRIVEN','N/A - NEW VEHICLE COMPOUND','N/A - FUEL TRUCK']