import pandas as pd


default_df = pd.read_csv('dashboard/nyiso_rt.csv')

test_df = pd.DataFrame({
    'date': ['2020-05-05', '2020-05-04', '2020-05-03', '2020-05-02', '2020-05-01', '2020-04-30', '2020-04-29',
             '2020-05-05', '2020-05-04', '2020-05-03', '2020-05-02', '2020-05-01', '2020-04-30', '2020-04-29',
             '2020-05-05', '2020-05-04', '2020-05-03', '2020-05-02', '2020-05-01', '2020-04-30', '2020-04-29'],
    'iso': ['NYISO', 'NYISO', 'NYISO', 'NYISO', 'NYISO', 'NYISO', 'NYISO',
            'NYISO', 'NYISO', 'NYISO', 'NYISO', 'NYISO', 'NYISO', 'NYISO',
            'NEPOOL', 'NEPOOL', 'NEPOOL', 'NEPOOL', 'NEPOOL', 'NEPOOL', 'NEPOOL'],
    'zone': ['CAPITL', 'CAPITL', 'CAPITL', 'CAPITL', 'CAPITL', 'CAPITL', 'CAPITL',
             'HUD_VL', 'HUD_VL', 'HUD_VL', 'HUD_VL', 'HUD_VL', 'HUD_VL', 'HUD_VL',
             'MASS_HUB', 'MASS_HUB', 'MASS_HUB', 'MASS_HUB', 'MASS_HUB', 'MASS_HUB', 'MASS_HUB'],
    'he01': [14.21, 14.07, 13.5, 14.66, 13.77, 15.11, 14.9,
             13.31, 15.73, 16.73, 13.18, 14.11, 15.83, 16.06,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he02': [12.94, 15.36, 16.36, 12.81, 13.74, 15.46, 15.69,
             14.48, 14.0, 15.44, 12.59, 13.83, 13.64, 13.13,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he03': [14.11, 13.63, 15.07, 12.22, 13.46, 13.27, 12.76,
             12.45, 12.34, 16.44, 12.52, 11.87, 13.16, 12.22,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he04': [12.08, 11.97, 16.07, 12.15, 11.5, 12.79, 11.85,
             12.08, 11.48, 16.25, 12.47, 11.65, 12.92, 12.11,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he05': [11.71, 11.11, 15.88, 12.1, 11.28, 12.55, 11.74,
             12.21, 11.9, 16.47, 12.35, 11.96, 13.45, 12.83,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he06': [11.84, 11.53, 16.1, 11.98, 11.59, 13.08, 12.46,
             12.79, 13.3, 15.44, 14.09, 12.82, 13.74, 13.68,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he07': [12.42, 12.93, 15.07, 13.72, 12.45, 13.37, 13.31,
             15.27, 12.02, 14.33, 13.7, 14.89, 14.99, 15.99,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
    'he08':  [14.9, 11.65, 13.96, 13.33, 14.52, 14.62, 15.62,
              16.67, 13.0, 14.27, 15.03, 15.1, 16.84, 17.64,
              15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75 ],
    'he09': [16.3, 12.63, 13.9, 14.66, 14.73, 16.47, 17.27,
             18.66, 13.44, 13.25, 16.64, 16.72, 17.8, 18.15,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75 ],
    'he10': [18.29, 13.07, 12.88, 16.27, 16.35, 17.43, 17.78,
             19.42, 14.08, 13.64, 17.2, 15.92, 17.29, 18.04,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he11': [19.05, 13.71, 13.27, 16.83, 15.55, 16.92, 17.67,
             19.23, 14.01, 13.61, 16.52, 15.61, 16.46, 17.74,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he12': [18.86, 13.64, 13.24, 16.15, 15.24, 16.09, 17.37,
             19.22, 14.01, 14.62, 16.73, 15.37, 16.05, 17.36,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75 ],
    'he13': [18.85, 13.64, 14.25, 16.36, 15.0, 15.68, 16.99,
             18.43, 13.94, 14.67, 16.55, 14.85, 16.21, 16.74,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he14': [18.06, 13.57, 14.3, 16.18, 14.48, 15.84, 16.37,
             17.06, 13.19, 15.39, 16.18, 14.54, 15.48, 16.53,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75 ],
    'he15': [16.69, 12.82, 15.02, 15.81, 14.17, 15.11, 16.16,
             16.43, 12.55, 14.11, 15.57, 13.85, 14.54, 15.94,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he16': [16.06, 12.18, 13.74, 15.2, 13.48, 14.17, 15.57,
             15.8, 12.54, 14.02, 15.06, 13.74, 14.42, 15.8,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75 ] ,
    'he17': [15.43, 12.17, 13.65, 14.69, 13.37, 14.05, 15.43,
             16.64, 13.51, 14.88, 16.68, 15.14, 16.08, 16.77,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he18': [16.27, 13.14, 14.51, 16.31, 14.77, 15.71, 16.4,
             19.03, 15.59, 17.39, 18.49, 16.42, 18.18, 19.29,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75 ],
    'he19': [18.66, 15.22, 17.02, 18.12, 16.05, 17.81, 18.92,
             17.98, 19.12, 18.79, 18.95, 17.71, 18.98, 18.96,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he20': [17.61, 18.75, 18.42, 18.58, 17.34, 18.61, 18.59,
             18.74, 20.6, 19.9, 20.4, 19.83, 20.36, 20.48,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he21': [18.37, 20.23, 19.53, 20.03, 19.46, 19.99, 20.11,
             18.89, 21.71, 23.12, 21.84, 21.77, 22.72, 22.93,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he22': [18.52, 21.34, 22.75, 21.47, 21.4, 22.35, 22.56,
             16.93, 17.46, 17.0, 18.76, 17.77, 19.04, 18.69,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he23': [16.56, 17.09, 16.63, 18.39, 17.4, 18.67, 18.32,
             14.96, 14.26, 14.6, 15.55, 15.79, 16.06, 16.71,
             15.75, 15.75, 15.75, 15.75, 15.75, 15.75, 15.75],
    'he24': [14.59, 13.89, 14.23, 15.18, 15.42, 15.69, 16.34,
             14.96, 14.26, 14.6, 15.55, 15.79, 16.06, 16.71,
             7.55, 7.55, 7.55, 7.55, 7.55, 7.55, 7.55],
})
