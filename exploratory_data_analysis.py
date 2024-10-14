#Using the tables created in collection_and_cleaning.py
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

###Plot 1: Global gaps between Max and Min Life expectancy
globalLifeExpectancy = HNP_base[["Year","Life expectancy at birth, total (years)"]]
globalLifeExpectancy = globalLifeExpectancy.dropna()

globalLifeExpectancy = globalLifeExpectancy.groupby('Year',as_index=False).agg(np.ptp)

plot1 = plt.plot(globalLifeExpectancy["Year"], globalLifeExpectancy['Life expectancy at birth, total (years)'])
#Format plot
plt.xlabel("Year")
plt.ylabel("Max Difference")
plt.xticks(rotation = 90)
plt.xticks(globalLifeExpectancy["Year"][::10])
plt.title("Difference in Min and Max Life Expectancy")
plt.show()

plt.savefig('Max_Difference_Over_Time.png')

###Plot 2a/b: Top 10 largest increases in Life Expectancy and Bottom 10 increases in Life Expectancy
countryLifeExpectancy = HNP_base[(HNP_stats["Year"] == "1960")|(HNP_stats["Year"] == "2022")]
countryLifeExpectancy = countryLifeExpectancy[['Country Name','Year','Life expectancy at birth, total (years)']]
countryLifeExpectancy= countryLifeExpectancy.pivot_table(index=['Country Name'], columns='Year', values='Life expectancy at birth, total (years)').reset_index()
countryLifeExpectancy["Difference"] = countryLifeExpectancy['2022'] - countryLifeExpectancy['1960']
countryLifeExpectancy = countryLifeExpectancy.dropna()
countryLifeExpectancy.sort_values(by=['Difference'], ascending=False)

top10LifeExpGrowth = countryLifeExpectancy.sort_values(by=['Difference'], ascending=False).head(10)
#top10LifeExpGrowth
bottom10LifeExpGrowth = countryLifeExpectancy.sort_values(by=['Difference'], ascending=True).head(10)
#bottom10LifeExpGrowth

countryLifeExpectancy

plot2a = plt.bar(top10LifeExpGrowth["Country Name"], top10LifeExpGrowth["Difference"])
#Format plot
plt.xlabel("Country")
plt.ylabel("Years Added to Life Expectancy")
plt.xticks(rotation = 90)
plt.title("Years Added to Life Expectancy (1960-2022):Top 10")
plt.show()

plt.savefig('Years_Added_Top10.png')

plot2b = plt.bar(bottom10LifeExpGrowth["Country Name"], bottom10LifeExpGrowth["Difference"])
#Format plot
plt.xlabel("Country")
plt.ylabel("Years Added to Life Expectancy")
plt.xticks(rotation = 90)
plt.title("Years Added to Life Expectancy (1960-2022):Bottom 10")
plt.show()

plt.savefig('Years_Added_Bottom_10.png')


###Plot 3: Histogram of global country increases in life expectancy
plot3 = plt.hist(countryLifeExpectancy["Difference"], bins=20)
#Format plot
plt.xlabel("Country")
plt.ylabel("Years Added to Life Expectancy")
plt.xticks(rotation = 90)
plt.title("Years Added to Life Expectancy (1960-2022):Global Progress")
plt.annotate("US: 7.66 Years", xy = (7.66, 10), xytext = (-2.66, 15),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

plt.savefig('Years_Added_World_Hist.png')

###Plot 4: Growth in life expectancy versus starting 1960 life expectancy level
plot4 = plt.scatter(countryLifeExpectancy["1960"], countryLifeExpectancy["Difference"])

#Format plot
plt.xlabel("Starting Life Expectancy (1960)")
plt.ylabel("Life Expectancy Change Rate")
plt.xticks(rotation = 90)
plt.title("Years Added to Life Expectancy")
plt.annotate("China: Starting Age 33.3, 45.3 year increase", xy = (33.6, 45), xytext = (38.6, 45),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate("Ukraine: Starting Age 69.5, 0.9 year decrease", xy = (69.2, -0.9), xytext = (30, -0.9),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

plt.savefig('Life_expectancy_change_rate.png')


#Plot 5: US growth in Life expectancy vs global average
HNP_stats_world_LE =HNP_stats_world[["Year","Life expectancy at birth, total (years)"]]
HNP_stats_world_LE = HNP_stats_world_LE.dropna()

USlifeExpectancy = HNP_base[HNP_base["Country Name"] == "United States"]
USlifeExpectancy = USlifeExpectancy[["Year","Life expectancy at birth, total (years)"]]
USlifeExpectancy = USlifeExpectancy.dropna()

plot5 = plt.plot(HNP_stats_world_LE["Year"], HNP_stats_world_LE["Life expectancy at birth, total (years)"])
plt.plot(USlifeExpectancy["Year"], USlifeExpectancy["Life expectancy at birth, total (years)"])
#Format plot
plt.xlabel("Year")
plt.ylabel("Life Expectancy")
plt.xticks(rotation = 90)
plt.xticks(globalLifeExpectancy["Year"][::10])
plt.title("US Increase in Life Expectancy Versus Global Trends")
plt.legend(['World', 'United States'])
plt.show()

plt.savefig('US_Vs_World_Increase.png')


###Plot 6:
fig, axs = plt.subplots(3, 1,constrained_layout=True)
axs[0].scatter(chronicIllness["Cause of death, by non-communicable diseases (% of total)"],
                  chronicIllness["Life expectancy at birth, total (years)"])
axs[0].set_title('Percentage of Deaths By Non-communicable Diseases')
axs[0].set(xlabel='Percentage of Population', ylabel='Life Expectancy')
fig.suptitle('Life Expectancy with Patterns of Chronic Disease', fontsize=16)

axs[1].scatter(chronicIllness["Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70 (%)"],
                  chronicIllness["Life expectancy at birth, total (years)"])
axs[1].set_title('Overall Mortality due to CVD, Cancer, Diabetes or CRD (ages 30-70)')
axs[1].set(xlabel='Percentage of Population', ylabel='Life Expectancy')

axs[2].scatter(chronicIllness["Prevalence of HIV, total (% of population ages 15-49)"],
                  chronicIllness["Life expectancy at birth, total (years)"])
axs[2].set_title('Prevalence of HIV (ages 15-49)')
axs[2].set(xlabel='Percentage of Population', ylabel='Life Expectancy')
fig.set_size_inches(12, 10)

plt.show()

plt.savefig('ChronicIllness.png')

###Plot 7: Alcohol use vs average life expectancy
bins = [0, 1, 2, 3, 5, 10, 20]

alcoholUse["Alcohol Consumption"] = pd.cut(alcoholUse["Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)"],
                                            bins,labels=['0 to 1', '1 to 2', '2 to 3', "3 to 5", "5 to 10", "10 to 20"])

alcoholUseBinned = alcoholUse.groupby(["Alcohol Consumption"],as_index=False).mean("Life expectancy at birth, total (years)")

plt.bar(x = alcoholUseBinned["Alcohol Consumption"], height = alcoholUseBinned["Life expectancy at birth, total (years)"] )
#Format plot
plt.xlabel("Average Consumption (Liters per Capita)")
plt.ylabel("Average Life Expectancy")
plt.title("Alcohol Consumption and Average Life Expectancy")
plt.show()

plt.savefig('AlcoholConsumption.png')

###Plot 8: Public Health practices and life expectancy

fig, axs = plt.subplots(3, 1,constrained_layout=True)
axs[0].scatter(publicHealth["People practicing open defecation (% of population)"],
                  publicHealth["Life expectancy at birth, total (years)"])
axs[0].set_title('Practicing Open Defecation')
axs[0].set(xlabel='Percentage of Population', ylabel='Life Expectancy')
fig.suptitle('Life Expectancy with Standards of Public Health', fontsize=16)


axs[1].scatter(publicHealth["People using safely managed drinking water services (% of population)"],
                  publicHealth["Life expectancy at birth, total (years)"])
axs[1].set_title('Drinking Clean Water')
axs[1].set(xlabel='Percentage of Population', ylabel='Life Expectancy')

axs[2].scatter(publicHealth["People using safely managed sanitation services (% of population)"],
                  publicHealth["Life expectancy at birth, total (years)"])
axs[2].set_title('Using Safely Managed Sanitation Service')
axs[2].set(xlabel='Percentage of Population', ylabel='Life Expectancy')
fig.set_size_inches(12, 10)

plt.show()

plt.savefig('publicHealth.png')

###Plot 9: Government Expenditure on Health and Life Expectancy
plot9 = plt.scatter(economicCost["Domestic general government health expenditure per capita (current US$)"],
                    economicCost["Domestic general government health expenditure (% of GDP)"],
                    c = economicCost["Life expectancy at birth, total (years)"])
plt.xlabel("Government health expenditure per capita (current US$)")
plt.ylabel("Government health expenditure (% of GDP)")
plt.title("GDP Investment in Health")
plt.colorbar(plot9, label='Life Expectancy')
plt.annotate("Tuvalu: 22.25% of GDP", xy = (500, 22.25), xytext = (550,22.25),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate("United States: 10.69% of GDP", xy = (6700, 11), xytext = (2900, 12.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

plt.savefig('GDPinvestment.png')


###Plot 10: Life Expectancy vs Country Income Level
fig = plt.figure()
fig.suptitle('Life Expectancy by Income Levels (2020)')
ax = fig.add_subplot(111)
ax.boxplot([incomeGroups2020low, incomeGroups2020lowMid, incomeGroups2020upMid, incomeGroups2020High])
ax.set_xticklabels(["Low","Lower middle","Upper middle","High"])
ax.set_ylabel('Life Expectancy')
ax.set_xlabel("Income Levels")
plt.show()

plt.savefig('IncomeGroups.png')
