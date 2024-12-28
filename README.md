# **Philippines Earthquake Clustering & Hotspots**

In this project, analysis is done on the intensity of earthquakes in the Philippines from 2016 to 2024. The magnitude as well as the location (latitude & longitude) is provided to us as a CSV file by PHIVOLCS--which will then be used for our Machine Learning system to detect and visualize seismic hotspots all over the Philippines. 

#### **Data Source**

**PHIVOLCS** Earthquake Bulletins of latest seismic events in the Philippines are listed below. The event parameters (hypocenter, time and magnitude) are determined using incoming data from the 

Philippine Seismic Network. Philippine Standard Time (PST) is eight hours ahead of Coordinated Universal Time (UTC). (PST = UTC + 8H) UTC is the time standard for which the world regulates clocks and time. Earthquakes in this list with their date and time in blue have reported and recorded intensities. Intensity ratings are based on the PHIVOLCS Earthquake Intensity Scale.

#### **Dataset**

[1] BwandoWando. (2024). Philippine Earthquakes (from PHIVOLCS) [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DS/5555087 <br>
[2] https://simplemaps.com/gis/country/ph <br>
[3] https://earthquake.phivolcs.dost.gov.ph/
[4] https://www.foi.gov.ph/requests/shapefile-of-philippine-fault-system/

#### **Geomatics Services Request**

The Geomatics and Hazard Assessment Services Section (GeomHASS) of the Geology, Geophysics R&D Division produces and distributes processed Geographic Information System (GIS)- and Remote Sensing (RS)- related information to PHIVOLCS stakeholders.

### **Setup**
1. Clone the repository
2. Create a virtual environment
3. Activate the virtual environment: `env\Scripts\activate`
4. `pip install -r requirements.txt`
5. (Optional) `jupyter notebook` or `jupyter lab`

### **How to Run**
- To run exploratory data analysis (EDA): `notebooks/01_data_exploration.ipynb`
- To run clustering: `notebooks/02_clustering.ipynb` 
