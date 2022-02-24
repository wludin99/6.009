junctions = {'D0', 'D1', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D2', 'D20', 'D21', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'U0', 'U1', 'U10', 'U11', 'U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U19', 'U2', 'U20', 'U21', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9'}

wires = {('D0', 'D1'): ('D0', 'D1'), ('D1', 'D2'): ('D1', 'D2'), ('D10', 'D11'): ('D10', 'D11'), ('D11', 'D12'): ('D11', 'D12'), ('D12', 'D13'): ('D12', 'D13'), ('D13', 'D14'): ('D13', 'D14'), ('D14', 'D15'): ('D14', 'D15'), ('D15', 'D16'): ('D15', 'D16'), ('D16', 'D17'): ('D16', 'D17'), ('D17', 'D18'): ('D17', 'D18'), ('D18', 'D19'): ('D18', 'D19'), ('D19', 'D20'): ('D19', 'D20'), ('D2', 'D3'): ('D2', 'D3'), ('D20', 'D21'): ('D20', 'D21'), ('D3', 'D4'): ('D3', 'D4'), ('D4', 'D5'): ('D4', 'D5'), ('D5', 'D6'): ('D5', 'D6'), ('D6', 'D7'): ('D6', 'D7'), ('D7', 'D8'): ('D7', 'D8'), ('D8', 'D9'): ('D8', 'D9'), ('D9', 'D10'): ('D9', 'D10'), ('U0', 'D0'): ('U0', 'D0'), ('U0', 'U1'): ('U0', 'U1'), ('U1', 'D1'): ('U1', 'D1'), ('U1', 'U2'): ('U1', 'U2'), ('U10', 'D10'): ('U10', 'D10'), ('U10', 'U11'): ('U10', 'U11'), ('U11', 'D11'): ('U11', 'D11'), ('U11', 'U12'): ('U11', 'U12'), ('U12', 'D12'): ('U12', 'D12'), ('U12', 'U13'): ('U12', 'U13'), ('U13', 'D13'): ('U13', 'D13'), ('U13', 'U14'): ('U13', 'U14'), ('U14', 'D14'): ('U14', 'D14'), ('U14', 'U15'): ('U14', 'U15'), ('U15', 'D15'): ('U15', 'D15'), ('U15', 'U16'): ('U15', 'U16'), ('U16', 'D16'): ('U16', 'D16'), ('U16', 'U17'): ('U16', 'U17'), ('U17', 'D17'): ('U17', 'D17'), ('U17', 'U18'): ('U17', 'U18'), ('U18', 'D18'): ('U18', 'D18'), ('U18', 'U19'): ('U18', 'U19'), ('U19', 'D19'): ('U19', 'D19'), ('U19', 'U20'): ('U19', 'U20'), ('U2', 'D2'): ('U2', 'D2'), ('U2', 'U3'): ('U2', 'U3'), ('U20', 'D20'): ('U20', 'D20'), ('U20', 'U21'): ('U20', 'U21'), ('U21', 'D21'): ('U21', 'D21'), ('U3', 'D3'): ('U3', 'D3'), ('U3', 'U4'): ('U3', 'U4'), ('U4', 'D4'): ('U4', 'D4'), ('U4', 'U5'): ('U4', 'U5'), ('U5', 'D5'): ('U5', 'D5'), ('U5', 'U6'): ('U5', 'U6'), ('U6', 'D6'): ('U6', 'D6'), ('U6', 'U7'): ('U6', 'U7'), ('U7', 'D7'): ('U7', 'D7'), ('U7', 'U8'): ('U7', 'U8'), ('U8', 'D8'): ('U8', 'D8'), ('U8', 'U9'): ('U8', 'U9'), ('U9', 'D9'): ('U9', 'D9'), ('U9', 'U10'): ('U9', 'U10')}

resistances = {('D0', 'D1'): 0.5, ('D1', 'D2'): 0.5, ('D10', 'D11'): 0.5, ('D11', 'D12'): 0.5, ('D12', 'D13'): 0.5, ('D13', 'D14'): 0.5, ('D14', 'D15'): 0.5, ('D15', 'D16'): 0.5, ('D16', 'D17'): 0.5, ('D17', 'D18'): 0.5, ('D18', 'D19'): 0.5, ('D19', 'D20'): 0.5, ('D2', 'D3'): 0.5, ('D20', 'D21'): 0.5, ('D3', 'D4'): 0.5, ('D4', 'D5'): 0.5, ('D5', 'D6'): 0.5, ('D6', 'D7'): 0.5, ('D7', 'D8'): 0.5, ('D8', 'D9'): 0.5, ('D9', 'D10'): 0.5, ('U0', 'D0'): 1, ('U0', 'U1'): 0.5, ('U1', 'D1'): 1, ('U1', 'U2'): 0.5, ('U10', 'D10'): 1, ('U10', 'U11'): 0.5, ('U11', 'D11'): 1, ('U11', 'U12'): 0.5, ('U12', 'D12'): 1, ('U12', 'U13'): 0.5, ('U13', 'D13'): 1, ('U13', 'U14'): 0.5, ('U14', 'D14'): 1, ('U14', 'U15'): 0.5, ('U15', 'D15'): 1, ('U15', 'U16'): 0.5, ('U16', 'D16'): 1, ('U16', 'U17'): 0.5, ('U17', 'D17'): 1, ('U17', 'U18'): 0.5, ('U18', 'D18'): 1, ('U18', 'U19'): 0.5, ('U19', 'D19'): 1, ('U19', 'U20'): 0.5, ('U2', 'D2'): 1, ('U2', 'U3'): 0.5, ('U20', 'D20'): 1, ('U20', 'U21'): 0.5, ('U21', 'D21'): 1, ('U3', 'D3'): 1, ('U3', 'U4'): 0.5, ('U4', 'D4'): 1, ('U4', 'U5'): 0.5, ('U5', 'D5'): 1, ('U5', 'U6'): 0.5, ('U6', 'D6'): 1, ('U6', 'U7'): 0.5, ('U7', 'D7'): 1, ('U7', 'U8'): 0.5, ('U8', 'D8'): 1, ('U8', 'U9'): 0.5, ('U9', 'D9'): 1, ('U9', 'U10'): 0.5}

voltages = {('D0', 'D1'): 0, ('D1', 'D2'): 0, ('D10', 'D11'): 0, ('D11', 'D12'): 0, ('D12', 'D13'): 0, ('D13', 'D14'): 0, ('D14', 'D15'): 0, ('D15', 'D16'): 0, ('D16', 'D17'): 0, ('D17', 'D18'): 0, ('D18', 'D19'): 0, ('D19', 'D20'): 0, ('D2', 'D3'): 0, ('D20', 'D21'): 0, ('D3', 'D4'): 0, ('D4', 'D5'): 0, ('D5', 'D6'): 0, ('D6', 'D7'): 0, ('D7', 'D8'): 0, ('D8', 'D9'): 0, ('D9', 'D10'): 0, ('U0', 'D0'): 1000000000, ('U0', 'U1'): 0, ('U1', 'D1'): 0, ('U1', 'U2'): 0, ('U10', 'D10'): 0, ('U10', 'U11'): 0, ('U11', 'D11'): 0, ('U11', 'U12'): 0, ('U12', 'D12'): 0, ('U12', 'U13'): 0, ('U13', 'D13'): 0, ('U13', 'U14'): 0, ('U14', 'D14'): 0, ('U14', 'U15'): 0, ('U15', 'D15'): 0, ('U15', 'U16'): 0, ('U16', 'D16'): 0, ('U16', 'U17'): 0, ('U17', 'D17'): 0, ('U17', 'U18'): 0, ('U18', 'D18'): 0, ('U18', 'U19'): 0, ('U19', 'D19'): 0, ('U19', 'U20'): 0, ('U2', 'D2'): 0, ('U2', 'U3'): 0, ('U20', 'D20'): 0, ('U20', 'U21'): 0, ('U21', 'D21'): 0, ('U3', 'D3'): 0, ('U3', 'U4'): 0, ('U4', 'D4'): 0, ('U4', 'U5'): 0, ('U5', 'D5'): 0, ('U5', 'U6'): 0, ('U6', 'D6'): 0, ('U6', 'U7'): 0, ('U7', 'D7'): 0, ('U7', 'U8'): 0, ('U8', 'D8'): 0, ('U8', 'U9'): 0, ('U9', 'D9'): 0, ('U9', 'U10'): 0}

currents = {('D0', 'D1'): 381966011.2561051, ('D1', 'D2'): 145898033.75331545, ('D10', 'D11'): 25250.61732734896, ('D11', 'D12'): 9644.885636300414, ('D12', 'D13'): 3684.0125815521337, ('D13', 'D14'): 1407.168108355988, ('D14', 'D15'): 537.4937435159145, ('D15', 'D16'): 205.29312219171132, ('D16', 'D17'): 78.4076230593628, ('D17', 'D18'): 29.94774698630216, ('D18', 'D19'): 11.411617899543636, ('D19', 'D20'): 4.286106712294761, ('D2', 'D3'): 55728090.009841226, ('D20', 'D21'): 1.425702237446482, ('D3', 'D4'): 21286236.260208167, ('D4', 'D5'): 8130618.759783301, ('D5', 'D6'): 3105620.009141728, ('D6', 'D7'): 1186241.2956418844, ('D7', 'D8'): 453103.85778392496, ('D8', 'D9'): 173070.26270989052, ('D9', 'D10'): 66106.96534574647, ('U0', 'D0'): 381966011.25810516, ('U0', 'U1'): -381966011.24910516, ('U1', 'D1'): -236067977.5057897, ('U1', 'U2'): -145898033.76031545, ('U10', 'D10'): -40856.349018397515, ('U10', 'U11'): -25250.610327348957, ('U11', 'D11'): -15605.733691048543, ('U11', 'U12'): -9644.868636300414, ('U12', 'D12'): -5960.87005474828, ('U12', 'U13'): -3684.009581552134, ('U13', 'D13'): -2276.8364731961456, ('U13', 'U14'): -1407.1771083559884, ('U14', 'D14'): -869.6713648400739, ('U14', 'U15'): -537.4867435159144, ('U15', 'D15'): -332.18362132420316, ('U15', 'U16'): -205.30412219171131, ('U16', 'D16'): -126.88749913234852, ('U16', 'U17'): -78.4156230593628, ('U17', 'D17'): -48.47787607306064, ('U17', 'U18'): -29.931746986302162, ('U18', 'D18'): -18.524129086758524, ('U18', 'U19'): -11.399617899543633, ('U19', 'D19'): -7.1325111872488725, ('U19', 'U20'): -4.283106712294761, ('U2', 'D2'): -90169943.74147423, ('U2', 'U3'): -55728090.009841226, ('U20', 'D20'): -2.8564044748482784, ('U20', 'U21'): -1.430702237446482, ('U21', 'D21'): -1.4187022374464822, ('U3', 'D3'): -34441853.758633055, ('U3', 'U4'): -21286236.25420817, ('U4', 'D4'): -13155617.506424868, ('U4', 'U5'): -8130618.7597833, ('U5', 'D5'): -5024998.741641572, ('U5', 'U6'): -3105620.0201417278, ('U6', 'D6'): -1919378.7234998434, ('U6', 'U7'): -1186241.2996418844, ('U7', 'D7'): -733137.4268579595, ('U7', 'U8'): -453103.852783925, ('U8', 'D8'): -280033.5740740345, ('U8', 'U9'): -173070.26770989053, ('U9', 'D9'): -106963.30736414404, ('U9', 'U10'): -66106.96934574647}

deviations = {('D0', 'D1'): -190983005.62805256, ('D1', 'D2'): -72949016.87665772, ('D10', 'D11'): -12625.30866367448, ('D11', 'D12'): -4822.442818150207, ('D12', 'D13'): -1842.0062907760669, ('D13', 'D14'): -703.584054177994, ('D14', 'D15'): -268.74687175795725, ('D15', 'D16'): -102.64656109585566, ('D16', 'D17'): -39.2038115296814, ('D17', 'D18'): -14.97387349315108, ('D18', 'D19'): -5.705808949771818, ('D19', 'D20'): -2.1430533561473806, ('D2', 'D3'): -27864045.004920613, ('D20', 'D21'): -0.712851118723241, ('D3', 'D4'): -10643118.130104084, ('D4', 'D5'): -4065309.3798916503, ('D5', 'D6'): -1552810.004570864, ('D6', 'D7'): -593120.6478209422, ('D7', 'D8'): -226551.92889196248, ('D8', 'D9'): -86535.13135494526, ('D9', 'D10'): -33053.48267287324, ('U0', 'D0'): 618033988.7418948, ('U0', 'U1'): 190983005.62455258, ('U1', 'D1'): 236067977.5057897, ('U1', 'U2'): 72949016.88015772, ('U10', 'D10'): 40856.349018397515, ('U10', 'U11'): 12625.305163674479, ('U11', 'D11'): 15605.733691048543, ('U11', 'U12'): 4822.434318150207, ('U12', 'D12'): 5960.87005474828, ('U12', 'U13'): 1842.004790776067, ('U13', 'D13'): 2276.8364731961456, ('U13', 'U14'): 703.5885541779942, ('U14', 'D14'): 869.6713648400739, ('U14', 'U15'): 268.7433717579572, ('U15', 'D15'): 332.18362132420316, ('U15', 'U16'): 102.65206109585566, ('U16', 'D16'): 126.88749913234852, ('U16', 'U17'): 39.2078115296814, ('U17', 'D17'): 48.47787607306064, ('U17', 'U18'): 14.965873493151081, ('U18', 'D18'): 18.524129086758524, ('U18', 'U19'): 5.699808949771817, ('U19', 'D19'): 7.1325111872488725, ('U19', 'U20'): 2.1415533561473805, ('U2', 'D2'): 90169943.74147423, ('U2', 'U3'): 27864045.004920613, ('U20', 'D20'): 2.8564044748482784, ('U20', 'U21'): 0.715351118723241, ('U21', 'D21'): 1.4187022374464822, ('U3', 'D3'): 34441853.758633055, ('U3', 'U4'): 10643118.127104085, ('U4', 'D4'): 13155617.506424868, ('U4', 'U5'): 4065309.37989165, ('U5', 'D5'): 5024998.741641572, ('U5', 'U6'): 1552810.0100708639, ('U6', 'D6'): 1919378.7234998434, ('U6', 'U7'): 593120.6498209422, ('U7', 'D7'): 733137.4268579595, ('U7', 'U8'): 226551.9263919625, ('U8', 'D8'): 280033.5740740345, ('U8', 'U9'): 86535.13385494526, ('U9', 'D9'): 106963.30736414404, ('U9', 'U10'): 33053.48467287324}

soln = 0.05600000964477658
