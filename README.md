# **Philippines Earthquake Clustering & Hotspots**

In this project, analysis is done on the intensity of earthquakes in the Philippines from 2016 to 2024. The magnitude as well as the location (latitude & longitude) is provided to us as a CSV file by PHIVOLCS--which will then be used for our Machine Learning system to detect and visualize seismic hotspots all over the Philippines. 

#### **Data Source**

**PHIVOLCS** Earthquake Bulletins of latest seismic events in the Philippines are listed below. The event parameters (hypocenter, time and magnitude) are determined using incoming data from the 

Philippine Seismic Network. Philippine Standard Time (PST) is eight hours ahead of Coordinated Universal Time (UTC). (PST = UTC + 8H) UTC is the time standard for which the world regulates clocks and time. Earthquakes in this list with their date and time in blue have reported and recorded intensities. Intensity ratings are based on the PHIVOLCS Earthquake Intensity Scale.

#### **Dataset**

[1] BwandoWando. (2024). 🇵🇭 Philippine Earthquakes (from PHIVOLCS) [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DS/5555087 <br>
[2] https://www.kaggle.com/datasets/bwandowando/philippine-earthquakes-from-phivolcs <br>
[3] https://earthquake.phivolcs.dost.gov.ph/

### **Project Structure**

### **Setup**
1. Clone the repository
2. Create and activate a virtual environment
3. `pip install -r requirements.txt`
4. (Optional) `jupyter notebook` or `jupyter lab`

### **How to Run**
- To run data exploration: `notebooks/01_data_exploration.ipynb`
- To run clustering: `notebooks/02_clustering.ipynb` 
- OR use the scripts in `src/` if you prefer a non-notebook workflow.
