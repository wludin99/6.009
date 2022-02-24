junctions = {'D0', 'D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D2', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D3', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'U0', 'U1', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U19', 'U2', 'U20', 'U21', 'U22', 'U23', 'U24', 'U25', 'U26', 'U27', 'U28', 'U29', 'U3', 'U30', 'U31', 'U32', 'U33', 'U34', 'U35', 'U36', 'U37', 'U38', 'U39', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9'}

wires = {('D0', 'D1'): ('D0', 'D1'), ('D1', 'D2'): ('D1', 'D2'), ('D10', 'D11'): ('D10', 'D11'), ('D11', 'D12'): ('D11', 'D12'), ('D12', 'D13'): ('D12', 'D13'), ('D13', 'D14'): ('D13', 'D14'), ('D14', 'D15'): ('D14', 'D15'), ('D15', 'D16'): ('D15', 'D16'), ('D16', 'D17'): ('D16', 'D17'), ('D17', 'D18'): ('D17', 'D18'), ('D18', 'D19'): ('D18', 'D19'), ('D19', 'D20'): ('D19', 'D20'), ('D2', 'D3'): ('D2', 'D3'), ('D20', 'D21'): ('D20', 'D21'), ('D21', 'D22'): ('D21', 'D22'), ('D22', 'D23'): ('D22', 'D23'), ('D23', 'D24'): ('D23', 'D24'), ('D24', 'D25'): ('D24', 'D25'), ('D25', 'D26'): ('D25', 'D26'), ('D26', 'D27'): ('D26', 'D27'), ('D27', 'D28'): ('D27', 'D28'), ('D28', 'D29'): ('D28', 'D29'), ('D29', 'D30'): ('D29', 'D30'), ('D3', 'D4'): ('D3', 'D4'), ('D30', 'D31'): ('D30', 'D31'), ('D31', 'D32'): ('D31', 'D32'), ('D32', 'D33'): ('D32', 'D33'), ('D33', 'D34'): ('D33', 'D34'), ('D34', 'D35'): ('D34', 'D35'), ('D35', 'D36'): ('D35', 'D36'), ('D36', 'D37'): ('D36', 'D37'), ('D37', 'D38'): ('D37', 'D38'), ('D38', 'D39'): ('D38', 'D39'), ('D4', 'D5'): ('D4', 'D5'), ('D5', 'D6'): ('D5', 'D6'), ('D6', 'D7'): ('D6', 'D7'), ('D7', 'D8'): ('D7', 'D8'), ('D8', 'D9'): ('D8', 'D9'), ('D9', 'D10'): ('D9', 'D10'), ('U0', 'D0'): ('U0', 'D0'), ('U0', 'U1'): ('U0', 'U1'), ('U1', 'D1'): ('U1', 'D1'), ('U1', 'U2'): ('U1', 'U2'), ('U10', 'D10'): ('U10', 'D10'), ('U10', 'U11'): ('U10', 'U11'), ('U11', 'D11'): ('U11', 'D11'), ('U11', 'U12'): ('U11', 'U12'), ('U12', 'D12'): ('U12', 'D12'), ('U12', 'U13'): ('U12', 'U13'), ('U13', 'D13'): ('U13', 'D13'), ('U13', 'U14'): ('U13', 'U14'), ('U14', 'D14'): ('U14', 'D14'), ('U14', 'U15'): ('U14', 'U15'), ('U15', 'D15'): ('U15', 'D15'), ('U15', 'U16'): ('U15', 'U16'), ('U16', 'D16'): ('U16', 'D16'), ('U16', 'U17'): ('U16', 'U17'), ('U17', 'D17'): ('U17', 'D17'), ('U17', 'U18'): ('U17', 'U18'), ('U18', 'D18'): ('U18', 'D18'), ('U18', 'U19'): ('U18', 'U19'), ('U19', 'D19'): ('U19', 'D19'), ('U19', 'U20'): ('U19', 'U20'), ('U2', 'D2'): ('U2', 'D2'), ('U2', 'U3'): ('U2', 'U3'), ('U20', 'D20'): ('U20', 'D20'), ('U20', 'U21'): ('U20', 'U21'), ('U21', 'D21'): ('U21', 'D21'), ('U21', 'U22'): ('U21', 'U22'), ('U22', 'D22'): ('U22', 'D22'), ('U22', 'U23'): ('U22', 'U23'), ('U23', 'D23'): ('U23', 'D23'), ('U23', 'U24'): ('U23', 'U24'), ('U24', 'D24'): ('U24', 'D24'), ('U24', 'U25'): ('U24', 'U25'), ('U25', 'D25'): ('U25', 'D25'), ('U25', 'U26'): ('U25', 'U26'), ('U26', 'D26'): ('U26', 'D26'), ('U26', 'U27'): ('U26', 'U27'), ('U27', 'D27'): ('U27', 'D27'), ('U27', 'U28'): ('U27', 'U28'), ('U28', 'D28'): ('U28', 'D28'), ('U28', 'U29'): ('U28', 'U29'), ('U29', 'D29'): ('U29', 'D29'), ('U29', 'U30'): ('U29', 'U30'), ('U3', 'D3'): ('U3', 'D3'), ('U3', 'U4'): ('U3', 'U4'), ('U30', 'D30'): ('U30', 'D30'), ('U30', 'U31'): ('U30', 'U31'), ('U31', 'D31'): ('U31', 'D31'), ('U31', 'U32'): ('U31', 'U32'), ('U32', 'D32'): ('U32', 'D32'), ('U32', 'U33'): ('U32', 'U33'), ('U33', 'D33'): ('U33', 'D33'), ('U33', 'U34'): ('U33', 'U34'), ('U34', 'D34'): ('U34', 'D34'), ('U34', 'U35'): ('U34', 'U35'), ('U35', 'D35'): ('U35', 'D35'), ('U35', 'U36'): ('U35', 'U36'), ('U36', 'D36'): ('U36', 'D36'), ('U36', 'U37'): ('U36', 'U37'), ('U37', 'D37'): ('U37', 'D37'), ('U37', 'U38'): ('U37', 'U38'), ('U38', 'D38'): ('U38', 'D38'), ('U38', 'U39'): ('U38', 'U39'), ('U39', 'D39'): ('U39', 'D39'), ('U4', 'D4'): ('U4', 'D4'), ('U4', 'U5'): ('U4', 'U5'), ('U5', 'D5'): ('U5', 'D5'), ('U5', 'U6'): ('U5', 'U6'), ('U6', 'D6'): ('U6', 'D6'), ('U6', 'U7'): ('U6', 'U7'), ('U7', 'D7'): ('U7', 'D7'), ('U7', 'U8'): ('U7', 'U8'), ('U8', 'D8'): ('U8', 'D8'), ('U8', 'U9'): ('U8', 'U9'), ('U9', 'D9'): ('U9', 'D9'), ('U9', 'U10'): ('U9', 'U10')}

resistances = {('D0', 'D1'): 0.5, ('D1', 'D2'): 0.5, ('D10', 'D11'): 0.5, ('D11', 'D12'): 0.5, ('D12', 'D13'): 0.5, ('D13', 'D14'): 0.5, ('D14', 'D15'): 0.5, ('D15', 'D16'): 0.5, ('D16', 'D17'): 0.5, ('D17', 'D18'): 0.5, ('D18', 'D19'): 0.5, ('D19', 'D20'): 0.5, ('D2', 'D3'): 0.5, ('D20', 'D21'): 0.5, ('D21', 'D22'): 0.5, ('D22', 'D23'): 0.5, ('D23', 'D24'): 0.5, ('D24', 'D25'): 0.5, ('D25', 'D26'): 0.5, ('D26', 'D27'): 0.5, ('D27', 'D28'): 0.5, ('D28', 'D29'): 0.5, ('D29', 'D30'): 0.5, ('D3', 'D4'): 0.5, ('D30', 'D31'): 0.5, ('D31', 'D32'): 0.5, ('D32', 'D33'): 0.5, ('D33', 'D34'): 0.5, ('D34', 'D35'): 0.5, ('D35', 'D36'): 0.5, ('D36', 'D37'): 0.5, ('D37', 'D38'): 0.5, ('D38', 'D39'): 0.5, ('D4', 'D5'): 0.5, ('D5', 'D6'): 0.5, ('D6', 'D7'): 0.5, ('D7', 'D8'): 0.5, ('D8', 'D9'): 0.5, ('D9', 'D10'): 0.5, ('U0', 'D0'): 1, ('U0', 'U1'): 0, ('U1', 'D1'): 1, ('U1', 'U2'): 0, ('U10', 'D10'): 1, ('U10', 'U11'): 0, ('U11', 'D11'): 1, ('U11', 'U12'): 0, ('U12', 'D12'): 1, ('U12', 'U13'): 0, ('U13', 'D13'): 1, ('U13', 'U14'): 0, ('U14', 'D14'): 1, ('U14', 'U15'): 0, ('U15', 'D15'): 1, ('U15', 'U16'): 0, ('U16', 'D16'): 1, ('U16', 'U17'): 0, ('U17', 'D17'): 1, ('U17', 'U18'): 0, ('U18', 'D18'): 1, ('U18', 'U19'): 0, ('U19', 'D19'): 1, ('U19', 'U20'): 0, ('U2', 'D2'): 1, ('U2', 'U3'): 0, ('U20', 'D20'): 1, ('U20', 'U21'): 0, ('U21', 'D21'): 1, ('U21', 'U22'): 0, ('U22', 'D22'): 1, ('U22', 'U23'): 0, ('U23', 'D23'): 1, ('U23', 'U24'): 0, ('U24', 'D24'): 1, ('U24', 'U25'): 0, ('U25', 'D25'): 1, ('U25', 'U26'): 0, ('U26', 'D26'): 1, ('U26', 'U27'): 0, ('U27', 'D27'): 1, ('U27', 'U28'): 0, ('U28', 'D28'): 1, ('U28', 'U29'): 0, ('U29', 'D29'): 1, ('U29', 'U30'): 0, ('U3', 'D3'): 1, ('U3', 'U4'): 0, ('U30', 'D30'): 1, ('U30', 'U31'): 0, ('U31', 'D31'): 1, ('U31', 'U32'): 0, ('U32', 'D32'): 1, ('U32', 'U33'): 0, ('U33', 'D33'): 1, ('U33', 'U34'): 0, ('U34', 'D34'): 1, ('U34', 'U35'): 0, ('U35', 'D35'): 1, ('U35', 'U36'): 0, ('U36', 'D36'): 1, ('U36', 'U37'): 0, ('U37', 'D37'): 1, ('U37', 'U38'): 0, ('U38', 'D38'): 1, ('U38', 'U39'): 0, ('U39', 'D39'): 0.5, ('U4', 'D4'): 1, ('U4', 'U5'): 0, ('U5', 'D5'): 1, ('U5', 'U6'): 0, ('U6', 'D6'): 1, ('U6', 'U7'): 0, ('U7', 'D7'): 1, ('U7', 'U8'): 0, ('U8', 'D8'): 1, ('U8', 'U9'): 0, ('U9', 'D9'): 1, ('U9', 'U10'): 0}

voltages = {('D0', 'D1'): 0.0, ('D1', 'D2'): 0.0, ('D10', 'D11'): 0.0, ('D11', 'D12'): 0.11499999997613486, ('D12', 'D13'): 0.0, ('D13', 'D14'): 0.0, ('D14', 'D15'): 0.0, ('D15', 'D16'): 0.09500000000207365, ('D16', 'D17'): 0.0, ('D17', 'D18'): 0.004999999999881766, ('D18', 'D19'): 0.0, ('D19', 'D20'): 0.0, ('D2', 'D3'): 0.005000010132789612, ('D20', 'D21'): 0.0, ('D21', 'D22'): 0.0, ('D22', 'D23'): 0.0, ('D23', 'D24'): 0.0, ('D24', 'D25'): 0.10499999999999865, ('D25', 'D26'): -8.881784197001252e-16, ('D26', 'D27'): 4.440892098500626e-16, ('D27', 'D28'): 0.0, ('D28', 'D29'): 1.1102230246251565e-16, ('D29', 'D30'): 0.15500000000000003, ('D3', 'D4'): 0.0, ('D30', 'D31'): -5.551115123125783e-17, ('D31', 'D32'): 0.0, ('D32', 'D33'): 5.551115123125783e-17, ('D33', 'D34'): 1.3877787807814457e-17, ('D34', 'D35'): -1.5612511283791264e-17, ('D35', 'D36'): -1.3877787807814457e-17, ('D36', 'D37'): -1.0408340855860843e-17, ('D37', 'D38'): -1.734723475976807e-17, ('D38', 'D39'): -1.3877787807814457e-17, ('D4', 'D5'): -0.050000013783574104, ('D5', 'D6'): 9.313225746154785e-10, ('D6', 'D7'): 0.0, ('D7', 'D8'): 0.0, ('D8', 'D9'): 0.0, ('D9', 'D10'): -0.14999999979045242, ('U0', 'D0'): 1000000000.0, ('U0', 'U1'): 0.015000015497207642, ('U1', 'D1'): 0.0949999988079071, ('U1', 'U2'): 0.0, ('U10', 'D10'): 0.0, ('U10', 'U11'): -0.05000000004656613, ('U11', 'D11'): 0.0, ('U11', 'U12'): 0.0, ('U12', 'D12'): 0.0, ('U12', 'U13'): 0.08500000006642949, ('U13', 'D13'): -0.16500000002997695, ('U13', 'U14'): 0.0, ('U14', 'D14'): -0.03499999999985448, ('U14', 'U15'): 0.0, ('U15', 'D15'): 0.0, ('U15', 'U16'): 0.0, ('U16', 'D16'): 0.0, ('U16', 'U17'): -0.03999999999950887, ('U17', 'D17'): 0.0, ('U17', 'U18'): 0.0, ('U18', 'D18'): 0.0, ('U18', 'U19'): 0.19999999999982876, ('U19', 'D19'): -0.13999999999987267, ('U19', 'U20'): 0.0, ('U2', 'D2'): 0.0, ('U2', 'U3'): 0.0, ('U20', 'D20'): -0.03999999999979309, ('U20', 'U21'): 0.0, ('U21', 'D21'): -0.005000000000052296, ('U21', 'U22'): 0.0, ('U22', 'D22'): -0.025000000000005684, ('U22', 'U23'): 0.0, ('U23', 'D23'): -0.025000000000005684, ('U23', 'U24'): 0.0, ('U24', 'D24'): 0.0, ('U24', 'U25'): 0.0, ('U25', 'D25'): -0.03500000000000192, ('U25', 'U26'): 0.0, ('U26', 'D26'): 0.06499999999999861, ('U26', 'U27'): 0.0, ('U27', 'D27'): 0.0, ('U27', 'U28'): 0.19499999999999995, ('U28', 'D28'): -0.2250000000000001, ('U28', 'U29'): 0.0, ('U29', 'D29'): 0.0, ('U29', 'U30'): 0.0, ('U3', 'D3'): 0.0, ('U3', 'U4'): 0.1600000038743019, ('U30', 'D30'): 0.16000000000000014, ('U30', 'U31'): 0.0, ('U31', 'D31'): 0.07000000000000006, ('U31', 'U32'): 0.0, ('U32', 'D32'): 0.1, ('U32', 'U33'): 0.0, ('U33', 'D33'): 0.07500000000000001, ('U33', 'U34'): 0.0, ('U34', 'D34'): 0.025000000000000026, ('U34', 'U35'): 0.0, ('U35', 'D35'): -0.03, ('U35', 'U36'): 0.0, ('U36', 'D36'): 0.10999999999999999, ('U36', 'U37'): 0.0, ('U37', 'D37'): -2.0816681711721685e-17, ('U37', 'U38'): -0.00500000000000006, ('U38', 'D38'): 0.13000000000000003, ('U38', 'U39'): 0.0, ('U39', 'D39'): 1.3877787807814457e-17, ('U4', 'D4'): 0.0, ('U4', 'U5'): 0.0, ('U5', 'D5'): -0.03000001423060894, ('U5', 'U6'): 0.0, ('U6', 'D6'): 0.0, ('U6', 'U7'): -0.23499999975319952, ('U7', 'D7'): 0.0750000006519258, ('U7', 'U8'): 0.0, ('U8', 'D8'): 0.1250000004656613, ('U8', 'U9'): 0.0, ('U9', 'D9'): 0.0, ('U9', 'U10'): 0.0}

currents = {('D0', 'D1'): 500000000.0, ('D1', 'D2'): 250000000.03, ('D10', 'D11'): 488281.35000000056, ('D11', 'D12'): 244140.61500000025, ('D12', 'D13'): 122070.35250000008, ('D13', 'D14'): 61035.076250000064, ('D14', 'D15'): 30517.668125000033, ('D15', 'D16'): 15258.71906250002, ('D16', 'D17'): 7629.4145312500095, ('D17', 'D18'): 3814.7272656250043, ('D18', 'D19'): 1907.2686328125028, ('D19', 'D20'): 953.5943164062513, ('D2', 'D3'): 124999999.91, ('D20', 'D21'): 476.7671582031258, ('D21', 'D22'): 238.43857910156288, ('D22', 'D23'): 119.22928955078143, ('D23', 'D24'): 59.614644775390715, ('D24', 'D25'): 29.842322387695358, ('D25', 'D26'): 14.921161193847679, ('D26', 'D27'): 7.3805805969238385, ('D27', 'D28'): 3.7652902984619203, ('D28', 'D29'): 1.77264514923096, ('D29', 'D30'): 0.90132257461548, ('D3', 'D4'): 62499999.980000004, ('D30', 'D31'): 0.46566128730774003, ('D31', 'D32'): 0.23283064365387007, ('D32', 'D33'): 0.10641532182693503, ('D33', 'D34'): 0.15820766091346752, ('D34', 'D35'): -0.0008961695432662432, ('D35', 'D36'): -0.04544808477163312, ('D36', 'D37'): 0.04727595761418344, ('D37', 'D38'): 0.05363797880709172, ('D38', 'D39'): 0.031818989403545855, ('D4', 'D5'): 31249999.919999998, ('D5', 'D6'): 15624999.999999983, ('D6', 'D7'): 7812500.020000007, ('D7', 'D8'): 3906250.0400000038, ('D8', 'D9'): 1953125.0700000024, ('D9', 'D10'): 976562.5200000013, ('U0', 'D0'): 499999999.96, ('U0', 'U1'): -499999999.92, ('U1', 'D1'): -249999999.93, ('U1', 'U2'): -249999999.96, ('U10', 'D10'): -488281.16000000056, ('U10', 'U11'): -488281.20000000094, ('U11', 'D11'): -244140.53500000032, ('U11', 'U12'): -244140.61500000034, ('U12', 'D12'): -122070.34250000017, ('U12', 'U13'): -122070.40250000011, ('U13', 'D13'): -61035.2462500001, ('U13', 'U14'): -61035.08625000006, ('U14', 'D14'): -30517.578125000033, ('U14', 'U15'): -30517.558125000025, ('U15', 'D15'): -15258.709062500018, ('U15', 'U16'): -15258.79906250002, ('U16', 'D16'): -7629.44453125001, ('U16', 'U17'): -7629.44453125001, ('U17', 'D17'): -3814.777265625005, ('U17', 'U18'): -3814.637265625005, ('U18', 'D18'): -1907.4186328125027, ('U18', 'U19'): -1907.3386328125027, ('U19', 'D19'): -953.7243164062513, ('U19', 'U20'): -953.7643164062514, ('U2', 'D2'): -125000000.01, ('U2', 'U3'): -124999999.92000003, ('U20', 'D20'): -476.8271582031256, ('U20', 'U21'): -476.9371582031258, ('U21', 'D21'): -238.40857910156294, ('U21', 'U22'): -238.32857910156287, ('U22', 'D22'): -119.20928955078143, ('U22', 'U23'): -119.17928955078143, ('U23', 'D23'): -59.59464477539072, ('U23', 'U24'): -59.56464477539072, ('U24', 'D24'): -29.76232238769536, ('U24', 'U25'): -29.72232238769536, ('U25', 'D25'): -14.981161193847681, ('U25', 'U26'): -14.911161193847677, ('U26', 'D26'): -7.42058059692384, ('U26', 'U27'): -7.54058059692384, ('U27', 'D27'): -3.79529029846192, ('U27', 'U28'): -3.7452902984619203, ('U28', 'D28'): -1.9426451492309602, ('U28', 'U29'): -1.9626451492309602, ('U29', 'D29'): -0.8313225746154801, ('U29', 'U30'): -0.9613225746154801, ('U3', 'D3'): -62500000.06000002, ('U3', 'U4'): -62500000.030000016, ('U30', 'D30'): -0.37566128730773996, ('U30', 'U31'): -0.40566128730774004, ('U31', 'D31'): -0.23283064365386996, ('U31', 'U32'): -0.16283064365387007, ('U32', 'D32'): -0.08641532182693498, ('U32', 'U33'): -0.1464153218269351, ('U33', 'D33'): -0.05820766091346751, ('U33', 'U34'): -0.028207660913467512, ('U34', 'D34'): -0.029103830456733756, ('U34', 'U35'): -0.08910383045673376, ('U35', 'D35'): -0.08455191522836689, ('U35', 'U36'): -0.04455191522836688, ('U36', 'D36'): 0.03272404238581656, ('U36', 'U37'): 0.09272404238581657, ('U37', 'D37'): -0.05363797880709172, ('U37', 'U38'): 0.02636202119290828, ('U38', 'D38'): 0.09818101059645415, ('U38', 'U39'): -0.07181898940354586, ('U39', 'D39'): -0.031818989403545855, ('U4', 'D4'): -31249999.91000001, ('U4', 'U5'): -31249999.90000003, ('U5', 'D5'): -15624999.930000013, ('U5', 'U6'): -15625000.020000016, ('U6', 'D6'): -7812499.900000008, ('U6', 'U7'): -7812499.90000001, ('U7', 'D7'): -3906250.0500000035, ('U7', 'U8'): -3906250.0300000045, ('U8', 'D8'): -1953124.9800000018, ('U8', 'U9'): -1953124.9600000028, ('U9', 'D9'): -976562.570000001, ('U9', 'U10'): -976562.4600000015}

soln = {'D0', 'D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D2', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D3', 'D30', 'D31', 'D32', 'D33', 'D34', 'D35', 'D36', 'D37', 'D38', 'D39', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'U0', 'U1', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U19', 'U2', 'U20', 'U21', 'U22', 'U23', 'U24', 'U25', 'U26', 'U27', 'U28', 'U29', 'U3', 'U30', 'U31', 'U32', 'U33', 'U34', 'U35', 'U36', 'U37', 'U38', 'U39', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9'}

