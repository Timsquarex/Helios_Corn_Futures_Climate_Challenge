# Helios Corn Futures Climate Challenge (Kaggle Competition)

<p>
This repository is focusing on the process of
<ol type='1'>
    <li>Exploring the main dataset and figuring out the classification of the dataset depends on regional
    climate types, hemisphere and their corn planting seasonality</li>
    <li>Focusing heavily on the feature engineers of the pure climate variables as this is the main part of the competition.</li>
</ol>
</p>

<p>
For this repository, we could categorise the file into the state of:
<ol type='1'>
    <li>Light EDA on main dataset</li>
    <li>Feature Engineering exploration and backtesting by using my teammate's (William) API.</li>
    <li>Approach of feature selection</li>
    <li>My final submission (59.34) in private scoreboard</li>
</ol>

- Data: 
    - Dataset_by_countries directory (from index.qmd)
    - North_1_Hemisphere directory (from index.qmd)
    - North_2_Hemisphere directory (from index.qmd)
    - South_Hemisphere directory (from index.qmd)
    
    - corn_climate_risk_futures_daily_master.csv (main dataset from Kaggle, **too large to save in GitHub**)
    - corn_regional_market_share.csv (dataset from Kaggle)
    - corn_regional_climate_type.csv: Classified by Koppen climate type (by William)
    - corn_regional_hemisphere.csv: Classified by using hemisphere (by William)

    - final_result_corr_2.csv (from Phrase_3/overall_final_features_result.ipynb)

- harvest_season_plots: images saved (from harvest_period_plots.py)

- requirements.txt: libraries required.

- Phrase 1: Light EDA
    - index.qmd: Splitting dataset by using Koppen Climate Type, hemispheres, and mapping planting seasonality by integers. *Data/Dataset_by_countries, North_1_Hemisphere, North_2_Hemisphere, South_Hemisphere*

    - index_2.qmd: Using subsets to plot time series plots, distributional plots (on cliamate and corn futures variables).

    - harvest_period_plots.py: The file to plot planting seasonality for each regions, and saved them into *harvest_season_plot* folder.

    - EDA_regional_marketshare.html (by William)

- Phrase 2: Heavy feature engineering
    - feature_engineering_1.ipynb: for engineering new climate types with different equations, including heatwaves, coldwaves, flood, storms, and wildfires.

    - feature_engineering_2.ipynb: for engineering regime detection (La Nina, and El Nino) features, but ended up, those calculations became weather forecasting approach.

    - baseline_features_notebook.ipynb: baseline features modified by William, and used as our team baseline, and I tried and error different approaches in this notebook.

    - with_pca_attempt.ipynb: try to fit PCA approach to see if it is possible to engineer meaningful features.

    - helios_submission_1.ipynb: try the baseline that given by the host of the competition, and added my heatwaves, coldwaves, flood, storms, and wildfires climate risks to get a better result (but it didn't improve CFCS).

    - helios_submission_2.ipynb: try the baseline from Kaggle discussion, and added new climate risks types to get a better result (it does improve +0.6 CFCS, but not much).

    - helios_submission_3.ipynb: We used our own baseline notebook, and did non-linear transformation, lag features, new climate types features, and ended up we moved to Kaggle notebook since the dataset are too large to handle.

- Phrase 3: The most important part to show the final_submission (P.S. I have large dataset file, therefore it might not work locally but it works in Kaggle) 

    **You need to run according to this order**
        **1. overall_final_features_result.ipynb (You can skip this, since I have saved the result in Data)**
        **2. final_features_and_samplings.ipynb**
        **3. samplings_result.ipynb**
        **4. final_submission.ipynb**
    
    - overall_final_features_results.ipynb: This includes the whole process of final feature engineering, and because of long computation time, I ran the cfcs backtesting by chunks. I saved the those results into *Data/final_result_corr_2.csv*

    - final_features_and_samplings.ipynb: We decided to split into 20 subsets randomly and to test the consistent performance of different features.

    - samplings_result.ipynb: with the second filtering and the third filtering, I chose the only consistent top features in 20 subsets by ranking them according to sig_corr_ratio 

        - 1st filter: I only chose the features with 0.6 avg_sig_corr above according to the result from *Data/final_result_corr_2.csv* (Main dataset cfcs backtest result)

        - 2nd filter: Choose the features are performing consistently in those 20 parquet files (not saved in local, and I did run in Kaggle), by sorting **sig_corr_count** by listing out the first 100. --> We got 2 features only at the end of the filter.

        - 3rd filter: Choose the features are performing consistently in those 20 parquet files (not saved in local, and I did run in Kaggle), by sorting **avg_sig_corr** by listing out the first 220. --> We got 18 features only at the end of the filter, but I did just choose 13 features from the result.

        - Summary: ended up, we filtered the features from ~13,000 features into 15 features for the *final_submission.ipynb* by 2nd filter + 3rd filter

        - **Reasons of doing this: We realised that our feature with the highest avg_sig_corr does not always perform well in test data, that's why we tried to select a certain amount of features with consistent performance to optimise the score and prevent the overfitting problem.**

    - final_submission.ipynb: The final submission with the "best subset features" in Kaggle (with the score of 59.34)

- Backtesting API by William (teammate), includes:
    - cfcs.py
    - CFCS_API.txt

- .gitignore: ignoring the big dataset to prevent GitHub error.
</p>
