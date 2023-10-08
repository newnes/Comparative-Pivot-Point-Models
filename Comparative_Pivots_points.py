####################
# Title: Comparative Evaluation: Public Models Pivot Points vs Proprietary Model - Proximity & Pivot Point in Highs Peaks and Lows Valleys of Session over 482 Days - (Time Series ETF-SPY - Frame 1 min)
# Author: Nestor Mendez
# Propietary Model: Jump Inside the Fractal Spread" Model (JiFS) /Nestor Mendez 
# Year 2023, October, 7
# For testing purposes only

###################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_pivot_points(candlex, lst_day):
    # Obtain the necessary values from the previous day
    high = lst_day['high'].max()
    low = lst_day['low'].min()
    close = lst_day['close'].iloc[-1]
    open = lst_day['open'].iloc[0]

    ####################################

    # The Pivot
    PP = (high + low + close) / 3

    # The Diference prev_day bett high & low
    dif = round(high - low, 2)

    # SOURCE PIVOTS FIBONACCI
    # https://www.interactivebrokers.com/en/software/tws/usersguidebook/technicalanalytics/fibonaccipivotpoints.htm

    ### FIBONACCI ###
    R1 = 2*PP - low
    S1 = 2*PP - high
    R2 = PP + (high - low)
    S2 = PP - (high - low)
    R3 = high + 2*(PP - low)
    S3 = low - 2*(high - PP)

    # SOURCE PIVOTS CAMARILLA
    # https://www.interactivebrokers.com/en/software/tws/usersguidebook/technicalanalytics/camarillapivotpoints.htm

    ### CAMARILLA ##
    R1_Cam = round(close + dif * 1.1 / 12, 2)
    R2_Cam = round(close + dif * 1.1 / 6, 2)
    R3_Cam = round(close + dif * 1.1 / 4, 2)
    R4_Cam = round(close + dif * 1.1 / 2, 2)
    R5_Cam = round(0.82 * dif + close, 2)
    S1_Cam = round(close - dif * 1.1 / 12, 2)
    S2_Cam = round(close - dif * 1.1 / 6, 2)
    S3_Cam = round(close - dif * 1.1 / 4, 2)
    S4_Cam = round(close - dif * 1.1 / 2, 2)
    S5_Cam = round(close - 0.82 * dif, 2)

    # SOURCE PIVOTS FLOOR
    # https://www.interactivebrokers.com/en/software/tws/usersguidebook/technicalanalytics/floorpivotpoints.htm
    ### PIVOTS FLOOR ###
    floor = round(2 * PP, 2)
    FL_S1 = round(floor - high, 2)
    FL_S2 = round(PP - dif, 2)
    FL_S3 = round(FL_S1 - dif, 2)
    FL_R1 = round(floor - low, 2)
    FL_R2 = round(PP + dif, 2)
    FL_R3 = round(FL_R1 + dif, 2)

    # SOURCE PIVOTS WOODIE´S
    # #https://www.interactivebrokers.com/en/software/tws/usersguidebook/technicalanalytics/woodiepivotpoints.htm
    ### PIVOTS WOODIE´S ###

    PPW = round((high + low + 2 * close) / 4, 2)
    W_R1 = round((2 * PPW) - low, 2)
    W_R2 = round(PPW + high - low, 2)
    W_S1 = round((2 * PPW) - high, 2)
    W_S2 = round(PPW - high + low, 2)

    # SOURCE PIVOTS DEMARK
    # https://www.interactivebrokers.com/en/software/tws/usersguidebook/technicalanalytics/demarkpivotpoints.htm
    ### PIVOTS DEMARK ###

    men = high + 2 * low + close
    mas = 2 * high + low + close
    eq = high + low + 2 * close
    alto = round(men / 2 - low, 2)
    bajo = round(men / 2 - high, 2)
    alto1 = round(mas / 2 - low, 2)
    bajo1 = round(mas / 2 - high, 2)
    alto2 = round(eq / 2 - low, 2)
    bajo2 = round(eq / 2 - high, 2)

    def up():
        if close < open:
            return alto
        elif close > open:
            return alto1
        else:
            return alto2

    def dw():
        if close < open:
            return bajo
        elif close > open:
            return bajo1
        else:
            return bajo2

    ##################---PIVOTS -GANN ANGLE ####################

    gann1l = 86.25  ##degrees
    gann2l = 82.50  ##degrees
    gann3l = 75.00  ##degrees
    gann4l = 71.25  ##degrees
    gann5l = 63.75  ##degrees
    gann1k = 45.00  ##degrees
    gann2k = 26.25  ##degrees
    gann3k = 18.75  ##degrees
    gann4k = 15.00  ##degrees
    gann5k = 7.50  ##degrees
    gann6k = 3.75  ##degrees

    gann2 = (1 / 180) * gann1k  ## 45.00 degrees
    gann2a = (1 / 180) * gann2k  ## 26.25 degrees
    gann3a = (1 / 180) * gann3k  ## 18.75 degrees
    gann4a = (1 / 180) * gann4k  ## 15.00 degrees
    gann5a = (1 / 180) * gann5k  ## 7.5 degrees
    gann6a = (1 / 180) * gann6k  ## 3.5 degrees
    gann7a = (1 / 180) * gann1l  ## 86.25 degrees
    gann8a = (1 / 180) * gann2l  ## 82.50 degrees
    gann9a = (1 / 180) * gann3l  ## 75.00 degrees
    gann10a = (1 / 180) * gann4l  ## 71.25 degrees
    gann11a = (1 / 180) * gann5l  ## 63.75 degrees

    FH = np.sqrt(high)  #####################################

    gann4 = FH - gann2  ## 45.00 degrees
    gann4_a = FH - gann2a  ## 26.25 degrees
    gann4_b = FH - gann3a  ## 18.75 degrees
    gann4_c = FH - gann4a  ## 15.00 degrees
    gann4_d = FH - gann5a  ## 7.5 degrees
    gann4_e = FH - gann6a  ## 3.5 degrees
    gann4_f = FH - gann7a  ## 86.25 degrees
    gann4_g = FH - gann8a  ## 82.50 degrees
    gann4_h = FH - gann9a  ## 75.00 degrees
    gann4_i = FH - gann10a  ## 71.25 degrees
    gann4_j = FH - gann11a  ## 63.75 degrees

    a45du = round(np.power(gann4, 2), 2)  ## 45.00 degrees
    a26du = round(np.power(gann4_a, 2), 2)  ## 26.25 degrees
    a18du = round(np.power(gann4_b, 2), 2)  ## 18.75 degrees
    a15du = round(np.power(gann4_c, 2), 2)  ## 15.00 degrees
    a7du = round(np.power(gann4_d, 2), 2)  ## 7.5 degrees
    a3du = round(np.power(gann4_e, 2), 2)  ## 3.5 degrees
    a86du = round(np.power(gann4_f, 2), 2)  ## 86.25 degrees
    a82du = round(np.power(gann4_g, 2), 2)  ## 82.50 degrees
    a75du = round(np.power(gann4_h, 2), 2)  ## 75.00 degrees
    a71du = round(np.power(gann4_i, 2), 2)  ## 71.25 degrees
    a63du = round(np.power(gann4_j, 2), 2)  ## 63.75 degrees

    FL = np.sqrt(low)  #########################################

    gann7 = FL + gann2  ## 45.00 degrees
    gann7_a = FL + gann2a  ## 26.25 degrees
    gann7_b = FL + gann3a  ## 18.75 degrees
    gann7_c = FL + gann4a  ## 15.00 degrees
    gann7_d = FL + gann5a  ## 7.5 degrees
    gann7_e = FL + gann6a  ## 3.5 degrees
    gann7_f = FL + gann7a  ## 86.25 degrees
    gann7_g = FL + gann8a  ## 82.50 degrees
    gann7_h = FL + gann9a  ## 75.00 degrees
    gann7_i = FL + gann10a  ## 71.25 degrees
    gann7_j = FL + gann11a  ## 63.75 degrees

    a45dd = round(np.power(gann7, 2), 2)  ## 45.00 degrees
    a26dd = round(np.power(gann7_a, 2), 2)  ## 26.25 degrees
    a18dd = round(np.power(gann7_b, 2), 2)  ## 18.75 degrees
    a15dd = round(np.power(gann7_c, 2), 2)  ## 15.00 degrees
    a7dd = round(np.power(gann7_d, 2), 2)  ## 7.5 degrees
    a3dd = round(np.power(gann7_e, 2), 2)  ## 3.5 degrees
    a86dd = round(np.power(gann7_f, 2), 2)  ## 86.25 degrees
    a82dd = round(np.power(gann7_g, 2), 2)  ## 82.50 degrees
    a75dd = round(np.power(gann7_h, 2), 2)  ## 75.00 degrees
    a71dd = round(np.power(gann7_i, 2), 2)  ## 71.25 degrees
    a63dd = round(np.power(gann7_j, 2), 2)  ## 63.75 degrees

    ############################ PIVOTS --MURREY MATH LINES  ##############################

    murr8 = round(high, 2)  # 8/8
    murr7 = round(high - ((high - low)) / 8, 2) # 7/8
    murr6 = round(murr7 - ((high - low)) / 8, 2) # 6/8
    murr5 = round(murr6 - ((high - low)) / 8, 2) # 5/8
    murr4 = round(murr5 - ((high - low)) / 8, 2) # 4/8
    murr3 = round(murr4 - ((high - low)) / 8, 2)  # 3/8
    murr2 = round(murr3 - ((high - low)) / 8, 2) # 2/8
    murr1 = round(murr2 - ((high - low)) / 8, 2) # 1/8
    murr0 = round(low, 2)  # 0/8

    ############################ PIVOTS "JiFS" / MENDEZ  ##############################

    # Obtain values of the highest and lowest price
    high_nes = candlex.high.max()
    low_nes = candlex.low.min()

    dispersion = candlex.dispersion.iloc[-1]
    hypothetical_average = candlex.sma_total1.iloc[-1]

    N1_UP = low_nes + dispersion
    N2_UP = low_nes + dispersion*2
    N3_UP = low_nes + dispersion*3
    N4_UP = low_nes + dispersion*4
    N5_UP = low_nes + dispersion*5
    N6_UP = low_nes + dispersion*6

    N1_DW = high_nes - dispersion
    N2_DW = high_nes - dispersion * 2
    N3_DW = high_nes - dispersion * 3
    N4_DW = high_nes - dispersion * 4
    N5_DW = high_nes - dispersion * 5
    N6_DW = high_nes - dispersion * 6


    ha_1up = hypothetical_average + dispersion
    ha_2up = hypothetical_average + dispersion* 2
    ha_3up = hypothetical_average + dispersion* 3
    ha_4up = hypothetical_average + dispersion* 4
    ha_5up = hypothetical_average + dispersion* 5
    ha_6up = hypothetical_average + dispersion* 6

    ha_1dw = hypothetical_average - dispersion
    ha_2dw = hypothetical_average - dispersion * 2
    ha_3dw = hypothetical_average - dispersion * 3
    ha_4dw = hypothetical_average - dispersion * 4
    ha_5dw = hypothetical_average - dispersion * 5
    ha_6dw = hypothetical_average - dispersion * 6


    diccionario =  {
        'Fibonacci': {
            'PP': PP,
            'S1': S1,
            'S2': S2,
            'S3': S3,
            'R1': R1,
            'R2': R2,
            'R3': R3
        },
        'Camarilla': {
            'PP': PP,
            'S1': S1_Cam,
            'S2': S2_Cam,
            'S3': S3_Cam,
            'S4': S4_Cam,
            'S5': S5_Cam,
            'R1': R1_Cam,
            'R2': R2_Cam,
            'R3': R3_Cam,
            'R4': R4_Cam,
            'R5': R5_Cam
        },
        'Floor': {
            'PP': PP,
            'S1': FL_S1,
            'S2': FL_S2,
            'S3': FL_S3,
            'R1': FL_R1,
            'R2': FL_R2,
            'R3': FL_R3
        },
        'Woodies': {
            'PP': PPW,
            'S1': W_S1,
            'S2': W_S2,
            'R1': W_R1,
            'R2': W_R2,
        },
        'Demark': {
            'Up': up(),
            'Down': dw()
        },
        'Gann Angle': {
            'DU_86.25': a86du, 'DU_82.50': a82du, 'DU_75.00': a75du, 'DU_71.25': a71du,
            'DU_63.75':a63du, 'DU_45.00': a45du, 'DU_26.25': a26du, 'DU_18.75': a18du,
            'DU_15.00': a15du,'DU_7.5': a7du, 'DU_3.5': a3du,

            'DD_86.25': a86dd, 'DD_82.50': a82dd, 'DD_75.00': a75dd, 'DD_71.25': a71dd,
            'DD_63.75': a63dd, 'DD_45.00': a45dd, 'DD_26.25': a26dd, 'DD_18.75': a18dd,
            'DD_15.00': a15dd, 'DD_7.5': a7dd, 'DD_3.5': a3dd
        },
        'Murrey Math Lines': {
            'L_8/8': murr8,
            'L_7/8': murr7,
            'L_6/8': murr6,
            'L_5/8': murr5,
            'L_4/8': murr4,
            'L_3/8': murr3,
            'L_2/8': murr2,
            'L_1/8': murr1,
            'L_0/8': murr0
        }

    }
    # ha_1up
    diccionario_alto = {
        'Mendez_up': {
            'R1': N1_UP,
            'R2': N2_UP,
            'R3': N3_UP,
            'R4': N4_UP,
            'R5': N5_UP,
            'R6': N6_UP,
            'HA_R1': ha_1up,
            'HA_R2': ha_2up,
            'HA_R3': ha_3up,
            'HA_R4': ha_4up,
            'HA_R5': ha_5up,
            'HA_R6': ha_6up

        }
    }
    diccionario_bajo = {
        'Mendez_dw': {
            'S1': N1_DW,
            'S2': N2_DW,
            'S3': N3_DW,
            'S4': N4_DW,
            'S5': N5_DW,
            'S6': N6_DW,
            'HA_S1': ha_1dw,
            'HA_S2': ha_2dw,
            'HA_S3': ha_3dw,
            'HA_S4': ha_4dw,
            'HA_S5': ha_5dw,
            'HA_S6': ha_6dw
        }
    }

    # Reset the index
    candlex = candlex.reset_index(drop=True)

    # Get values of the highest price and the lowest price
    max_high = candlex.high.max()
    min_low = candlex.low.min()

    # Find the index of the highest price
    index_high_prev = candlex["high"].idxmax()

    # Find the index of the lowest price
    index_low_prev = candlex["low"].idxmin()

    # Open, high, low, and close values at max_high
    max_open_candle = candlex.loc[index_high_prev, "open"]
    max_high_candle = candlex.loc[index_high_prev, "high"]
    max_low_candle = candlex.loc[index_high_prev, "low"]
    max_close_candle = candlex.loc[index_high_prev, "close"]

    # Open, high, low, and close values at min_low
    min_open_candle = candlex.loc[index_low_prev, "open"]
    min_high_candle = candlex.loc[index_low_prev, "high"]
    min_low_candle = candlex.loc[index_low_prev, "low"]
    min_close_candle = candlex.loc[index_low_prev, "close"]


    resultados = []
    resultados_up = []
    resultados_dw = []

    # Get all the pivot values
    all_pivot_values = []
    for _, pivotes in diccionario.items():
        for _, valor_pivot in pivotes.items():
            all_pivot_values.append(valor_pivot)

    # Identify the values closest to max_high and min_low to avoid false positives when an immensely large candlestick covers the entire chart
    nearest_high_value = min(all_pivot_values, key=lambda x: abs(x - max_high))
    nearest_low_value = min(all_pivot_values, key=lambda x: abs(x - min_low))


    for metodo, pivotes in diccionario.items():
        for nombre_pivot, valor_pivot in pivotes.items():
            # Condition for pivot at max_high
            condicion_max = (max_low_candle <= max_open_candle <= max_close_candle < valor_pivot <= max_high_candle or
                    max_high_candle >= valor_pivot > max_open_candle >= max_close_candle > max_low_candle)

            # Condition for pivot in min_low
            condicion_min = (min_high_candle >= min_open_candle >= min_close_candle > valor_pivot >= min_low_candle or
                    min_low_candle <= valor_pivot < min_open_candle <= min_close_candle < min_high_candle)

            if condicion_max and valor_pivot == nearest_high_value:
                resultados.append((metodo, nombre_pivot, valor_pivot))

            if condicion_min and valor_pivot == nearest_low_value:
                resultados.append((metodo, nombre_pivot, valor_pivot))

    # Get all the pivot values
    all_pivot_values_up = []
    for _, pivotes in diccionario_alto.items():
        for _, valor_pivot in pivotes.items():
            all_pivot_values_up.append(valor_pivot)

        # Identify the values closest to max_high and min_low to avoid false positives when an immensely large candlestick covers the entire chart
    near_high_up = min(all_pivot_values_up, key=lambda x: abs(x - max_high))

    for metodo, pivotes in diccionario_alto.items():
        for nombre_pivot, valor_pivot in pivotes.items():
            # Condition for pivot at max_high
            condicion_max = (max_low_candle <= max_open_candle <= max_close_candle < valor_pivot <= max_high_candle or
                    max_high_candle >= valor_pivot > max_open_candle >= max_close_candle > max_low_candle)

            if condicion_max and valor_pivot == near_high_up:
                resultados_up.append((metodo, nombre_pivot, valor_pivot))


    # Get all the pivot values
    all_pivot_values_dw = []
    for _, pivotes in diccionario_bajo.items():
        for _, valor_pivot in pivotes.items():
            all_pivot_values_dw.append(valor_pivot)

    # Identify the values closest to max_high and min_low to avoid false positives when an immensely large candlestick covers the entire chart
    near_low_dw = min(all_pivot_values_dw, key=lambda x: abs(x - min_low))

    for metodo, pivotes in diccionario_bajo.items():
        for nombre_pivot, valor_pivot in pivotes.items():
            # Condition for pivot in min_low
            condicion_min = (min_high_candle >= min_open_candle >= min_close_candle > valor_pivot >= min_low_candle or
                             min_low_candle <= valor_pivot < min_open_candle <= min_close_candle < min_high_candle)

            if condicion_min and valor_pivot == near_low_dw:
                resultados_dw.append((metodo, nombre_pivot, valor_pivot))


    return diccionario, resultados,resultados_up,resultados_dw, candlex


all_weeks = pd.read_csv("ALL.csv", low_memory=False)
unique_days = all_weeks["date"].apply( lambda x: x.split()[0] )
all_days = unique_days.unique()

print(len(all_days),"----------")

# Create a list to store all results
all_results = []
all_results_up = []
all_results_dw = []

total_days = len(all_days) - 1

# Initialize counters
count_res_up = 0
count_res_dw = 0
count_by_type = {
    'Fibonacci': 0,
    'Camarilla': 0,
    'Floor': 0,
    'Woodies': 0,
    'Demark': 0,
    'Gann Angle': 0,
    'Murrey Math Lines': 0
}

# Iterate from date 1 to the end since we use the previous date as a reference

for i in range(1, len(all_days)):
    # Get data for the previous day
    dia_prev = all_days[i-1]

    # Get data for the current day
    dia = all_days[i]

    data_by_day_prev = [str(dia_prev) in value for value in all_weeks['date']]
    data_prev = all_weeks[data_by_day_prev]

    data_by_day = [str(dia) in value for value in all_weeks['date']]
    data = all_weeks[data_by_day]


    pivot_points, resultados,resultados_up,resultados_dw, candlex = calculate_pivot_points(data, data_prev)

    # Add the results to the general list
    all_results.append(resultados)
    all_results_up.append(resultados_up)
    all_results_dw.append(resultados_dw)

    # Calculate and display the progress percentage
    progress_percentage = (i / total_days) * 100
    print(f"Progress: {progress_percentage:.2f}%")

    # Add to the general counter and by type
    for tupla in resultados:
        tipo = tupla[0]
        count_by_type[tipo] += 1
    count_res_up += len(resultados_up)
    count_res_dw += len(resultados_dw)


# averages open Dic
averages = {}

# Print the results by type and Mendez study
for tipo, count in count_by_type.items():
    avg_per_day = count / len(all_days)
    averages[tipo] = avg_per_day
    print(f"Total results of type '{tipo}': {count}")
    print(f"Average results of type '{tipo}' by day: {avg_per_day:.2f}")


total_mendez = count_res_up+count_res_dw
print(f"Total results for 'Mendez': {total_mendez}")

avg_mendez_per_day = total_mendez / len(all_days)
print(f"Average results for 'Mendez' per day: {avg_mendez_per_day:.2f}")

averages['Mendez'] = avg_mendez_per_day

# Sort the averages
sorted_averages = dict(sorted(averages.items(), key=lambda item: item[1], reverse=True))

# Sort the counts
sorted_counts = dict(sorted(count_by_type.items(), key=lambda item: item[1], reverse=True))


# Data for visualization
names = list(sorted_averages.keys())
values = list(sorted_averages.values())

# Create bar chart
plt.figure(figsize=(12, 7))
colors = ['green' if val == max(values) else 'blue' if val in values[:3] else 'grey' for val in values]

bars = plt.bar(names, values, color=colors)
plt.ylabel('Average Results - Sample 482 days')
plt.xlabel('Study Type')
plt.title('Comparative Evaluation: Public Models Pivot Points vs Proprietary Model - Proximity & Pivot Point in Highs Peaks and Lows Valleys of Session over 482 Days - (Time Series ETF-SPY - Frame 1 min)')
plt.xticks(rotation=45)
plt.tight_layout()

# Añadir descripción de los tres modelos más frecuentes
top3 = "\n".join([f"{names[i]}: {values[i]:.2f}" for i in range(3)])
plt.annotate(f"Top 3 Models (by average):\n{top3}", xy=(0.90, 0.95), xycoords='axes fraction', fontsize=10, ha="right", va="top", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="aliceblue"))

# Añadir información total
totals_info = "\n".join([f"{tipo}: {count} times" for tipo, count in sorted_counts.items()] + [f"Mendez: {total_mendez} times"])
plt.annotate("All Models Frequency:\n" +totals_info, xy=(0.90, 0.70), xycoords='axes fraction', fontsize=10, ha="right", va="top", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="aliceblue"))

plt.show()

for res, res_up, res_dw in zip(all_results, all_results_up, all_results_dw):
    print(res)
    print(res_up)
    print(res_dw)













