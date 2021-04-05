Code created by Kara Allison and Kali Allison. Data compiled by Kara Allison.

The Pacific Northwest, more specifically western Washington, is the region selected as a case study for this project. Baseline data will need to be adjusted for the users specific region.

This code computes the closest baseline data (compiled from various resources: see included bibliography file) for each US National Vegetation Classification (USNVC) plant association to the user-provided plot data by comparing vegetation presence/absence using percent cover and calculating the "distance" between them. 

The average and standard deviation of each data point (ie % western hemlock cover) was used to generate a z-score for each point of data (baseline or plot-derived). The distance between the baseline and plot derived z-scores is then calcuated, using the general formula for distance between points (this is the equation present in the Output tab). The closer to 0 the total distance is, the better the fit. Weighting and scaling were used to increase accuracy and can be adjusted as needed.

Most of the time, the appropriate plant association will be the first choice; however, based upon the nature of this baseline and associated data, it is not going to always select the classification that makes the most sense. For instance, if the inputed plot data contained only madrone and Douglas fir and best-fit association was "Madrone-lodgepole pine/salal," the second association "Douglas fir-Madrone/salal, the makes the most sense as there was no lodgepole pine present in the plot. To this end, the contained within the provided code is the option to produce graphs showing the best fit to all the scenarios.

It is important to keep in mind that the assigned classification is simply a reflection of the existing conditions. As described in the 2008 National Vegetation Classification Standard, the USNVC classification system does not "directly apply to [the] classification or mapping of potential natural vegetation." Instead, it "establishes national procedures for classifying existing vegetation."
