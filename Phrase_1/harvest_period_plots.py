import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def harvest_period(country_region, country):
    regions = country_region[country] 
    num_regions = len(regions)
    ncols = 6
    nrows = math.ceil(num_regions/ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(18, 3 * nrows))
    fig.suptitle(f"Harvest Seasons: {country.upper()}", fontsize=12, fontweight="bold", y=0.98)

    if num_regions == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for i, region in enumerate(regions):
        working_df = pd.read_csv(f"./{country}/raw_{region}.csv")
            
        # 1. Cleaner line with step-style transitions
        axes[i].plot(working_df['date_on'], working_df['categorical_harvest_period'], 
                    color='#1b5e20', linewidth=2, drawstyle='steps-post')

        # 2. X-Axis: Show a label every 2 years to stop the 'black bar' effect
        axes[i].xaxis.set_major_locator(mdates.YearLocator(2)) 
        axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        
        # 3. Y-Axis: Lock to integers 0-4
        axes[i].set_yticks([0, 1, 2, 3, 4])
        
        # 4. Styling and Padding
        axes[i].set_title(f"Region: {region}", fontsize=9, pad=15)
        axes[i].set_ylabel("Harvest State", fontsize=5)
        axes[i].grid(True, alpha=0.15, linestyle=':') # Subtle grid
        axes[i].spines[['top', 'right']].set_visible(False) # Modern look

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')
    
    filename = f"{country}_harvest_seasons.png"

    # Save the figure
    plt.savefig(
        filename, 
        dpi=300,            # High resolution for reports
        bbox_inches='tight', # Prevents labels from being cut off
        facecolor='white'    # Ensures background isn't transparent
    )

    print(f"Saved plot as {filename}")

    plt.tight_layout()
    plt.show()

country_region = {'Argentina': ['Buenos Aires',
  'Córdoba',
  'Entre Ríos',
  'Santa Fe',
  'Santiago del Estero'],
 'Brazil': ['Bahia',
  'Espírito Santo',
  'Goiás',
  'Mato Grosso',
  'Mato Grosso do Sul',
  'Minas Gerais',
  'Paraná',
  'Rio Grande do Sul'],
 'Canada': ['Ontario', 'Quebec'],
 'China': ['Hebei',
  'Heilongjiang',
  'Henan',
  'Inner Mongolia',
  'Jiangsu',
  'Jilin',
  'Shandong'],
 'India': ['Bihar',
  'Karnataka',
  'Madhya Pradesh',
  'Maharashtra',
  'Tamil Nadu',
  'Telangana'],
 'Mexico': ['Guanajuato',
  'Guerrero',
  'Jalisco',
  'Michoacán',
  'Sinaloa',
  'State of Mexico',
  'Zacatecas'],
 'Paraguay': ['Alto Paraná',
  'Amambay',
  'Caaguazú',
  'Canindeyú',
  'Itapúa',
  'San Pedro'],
 'Russia': ['Bashkortostan',
  'Belgorod',
  'Bryansk',
  'Kabardino-Balkaria',
  'Krasnodar Krai',
  'Krasnoyarsk Krai',
  'Kursk',
  'Lipetsk',
  'Nizhny Novgorod',
  'Orenburg',
  'Oryol',
  'Penza',
  'Republic of Ingushetia',
  'Republic of Mordovia',
  'Republic of North Ossetia-Alania',
  'Republic of Tatarstan',
  'Rostov',
  'Ryazan',
  'Samara',
  'Saratov',
  'Stavropol Krai',
  'Tambov',
  'Tula',
  'Ulyanovsk',
  'Voronezh'],
 'South Africa': ['Free State',
  'Gauteng',
  'KwaZulu-Natal',
  'Mpumalanga',
  'North West',
  'Northern Cape'],
 'Ukraine': ['Cherkasy',
  'Dnipropetrovsk',
  'Odessa',
  'Poltava',
  'Sumy',
  'Vinnytsia'],
 'United States': ['Illinois',
  'Indiana',
  'Iowa',
  'Kansas',
  'Minnesota',
  'Missouri',
  'Nebraska',
  'North Dakota',
  'Ohio',
  'South Dakota',
  'Wisconsin']}

harvest_period(country_region, 'Russia') #Russia plot needs more columns