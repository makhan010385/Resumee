from pathlib import Path

import pandas as pd
import streamlit as st
from PIL import Image

# Inject custom CSS
st.markdown("""
    <style>
        /* Set the background color for the main content area */
        .stApp {
            background-color: #002b36;
            color: #ffffff;
        }

        /* Set the background color for the sidebar */
        .css-1d391kg {
            background-color: #586e75;
        }

        /* Set the primary color for interactive elements */
        .css-1cpxqw2 {
            color: #d33682;
        }

        /* Set the text color */
        .css-1cpxqw2, .css-1d391kg, .stApp {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "KVS.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Makhan Kumbhkar"
PAGE_ICON = ":wave:"
NAME = "Makhan"
DESCRIPTION = """
IT Profesional, Senior Data Analyst.
"""
EMAIL = "mkumbhcar@yahoo.com"
SOCIAL_MEDIA = {
    "YouTube": "#",
    "LinkedIn": "https://www.linkedin.com/in/makhan-kumbhkar-44b5361a/",
    "GitHub": "https://github.com/makhan010385",
   
}
PROJECTS = {
    "🏆 Building a system which automatic recognize plate number with OpenCV and Tesseract OCR": "#",
    "🏆 Face and Hand Landmarks Detection using Python": "#",
    "🏆 Building a Visual Similarity-based Recommendation System Using Python": "#",
    "🏆 Deep style web application using  transfer learning .": "#",
    "🏆 Face recognition of Mark Zuckerberg, Bill Gates and Mukesh Ambani using face_recogniton and openCV": "#",
    "🏆 PAN card fraud detection using computer vision. .": "#",
    "🏆 Fake news classifier .": "#",
    "🏆 Cartoonify Image with Machine Learning .": "#",
    "🏆 Emojify – Create your own emoji with Python .": "#",
    "🏆 Loan Prediction using Machine Learning.": "#",
    "🏆 MNIST Digit Classification using Machine Learning ": "#",
    "🏆 Fake News Detection using Machine learning and Natural language processing .": "#",
    "🏆 Bitcoin Price Predictor using Machine learning .": "#",
    "🏆 Uber Data Analysis Project using machine learning .": "#",
    "🏆 Personality Prediction Project Using supervised machine learning .": "#",
    "🏆 Housing Prices Prediction using Machine learning.": "#",
    "🏆 Credit Card Fraud Detection using machine learning .": "#",
    "🏆 Customer Segmentation using Machine Learning.": "#",
    "🏆 Sentiment Analysis using Machine Learning and deep learning .": "#",
    "🏆 Online Grocery Recommendation using Collaborative Filtering .": "#",
    "🏆 Movie Recommendation System Using Machine Learning .": "#",
    "🏆 Speech Emotion Recognition using Machine Learning .": "#",
    "🏆 Automatic License Number Plate Recognition System .": "#",
    "🏆 Web Application for Fake content Scrapping using Machine learning .": "#",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 10  Years expereince with teaching  and adminstrative
- ✔️ 7  Years expereince with IT Industry
- ✔️ Strong hands on experience and knowledge in ML, DL, Computer Vision, NLP
- ✔️ Good understanding Website development & deployment 
- 
"""
)


# --- Specialization:   ---
st.write('\n')
st.subheader("Specialization:")
st.write(
    """
- 📚 Modeling: LLM, Vision Transformer model,  Deep Learning, Machine Learning, Reinforcement Learning     
- 👩‍💻 Programming: Python, Scala, Java, .NET 
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- Qualification:   ---
st.write('\n')
st.subheader("Education Qualification:")
# st.write(
#     """
# - 📚 Modeling: LLM, Vision Transformer model,  Deep Learning, Machine Learning, Reinforcement Learning     
# - 👩‍💻 Programming: Python, Scala, Java, .NET 
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 🗄️ Databases: Postgres, MongoDB, MySQL
# """
# )

st.subheader("Education")
education = {
    "Degree": ["Ph.D. in Computer Science(Submmited)", "M.Phil  (CS) ","MCA", "B.Sc. in Computer Science"],
    "Institution": ["DAVV, Indore","DAVV, Indore", "RGPV, Bhopal", "VU, Ujjain"],
    "Year": ["2025", "2018","2008", "2005"]
}
st.table(pd.DataFrame(education))

# --- Research  Work ---
st.write('\n')
st.subheader("UGC Funding Project")
st.write("---")
st.write(
    """
- 📚 Title : Study of Design and Development of Cloud Environment in Autonomous Institution.      
- 👩‍💻 Desination: Co-PI
- 👩‍💻 Grant: 2 Lakh

"""
)
# st.subheader("Education")
# Publication = {
#     "Degree": ["Ph.D. in Computer Science(Submmited)", "M.Phil  (CS) ","MCA", "B.Sc. in Computer Science"],
#     "Institution": ["DAVV, Indore","DAVV, Indore", "RGPV, Bhopal", "VU, Ujjain"],
#     "Year": ["2025", "2018","2008", "2005"]
# }
# st.table(pd.DataFrame(Publication ))

import streamlit as st
import pandas as pd

st.subheader("Publications")

publications = {
    "S. No.": [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],
    "Author": ["Makhan Kumbhkar et al"]*35,
    "Title": [
        "Decoding Viewer Reactions: Sentiment and Emoji analysis on Youtube",
        "Design and Implementation of Web Scrapper for Fact-Checking Website",
        "LSSS-System: Fake Content Detection Using Linguistic Features",
        "Data Analytics for Fake Content Detection on Web",
        "An expert system for detecting fake content using machine learning and deep learning model through existing dataset",
        "Sentimental Analysis of ICAR-IISR Indore YouTube Channel using Lexicon-Based Approaches",
        "An Ensemble Model for Assessing Fake and Real Web Content on the Real Dataset",
        "Fake News Detection: State-of-the-Art Approaches, Challenges and Research Directions",
        "Fake Content Analysis on the Different Existing Dataset Using Machine Learning",
        "An Expert System for Detecting Fake and Real Website URL Using Machine Learning Approaches through Domain Based Features",
        "Compare ML Models to Improve Twitter Fake News Discovery and Verification",
        "DETR-DC5 Approaches for Improved Spatial Object Detection in Satellite Imagery",
        "Geospatial Object Detection in Hyperspectral Imagery using Spectral-Spatial Networks",
        "Integration of Machine Learning and Computer Vision to Detect and Prevent the Crime",
        "Dimensional Reduction Method based on Big Data Techniques for Large Scale Data",
        "Comparative analysis of machine learning models for fake content detection",
        "Delay Tolerant and Energy Reduced Task Allocation in Internet of Things with Cloud Systems",
        "Fake news detection: state-of- art approaches, challenges and research directions",
        "Evaluation of Block-Chain  Transaction Accuracy using Neural  Network Model",
        "Artificial Intelligence Assisted IoT  Data Intrusion Detection",
        "Investigating the Role of Block  Chain to Secure Identity in IoT for  Industrial Automation",
        "Creating virtual doctors by deploying the deep learning model for identifying pneumonia disease using chest-Xray.",
        "Study on Well Designed Irrigation  System through Applying Iot  Designed in Reflection of Crop  Field",
        "Expert System: Empirical Add-ons to Artificial Intelligence",
        "Detection of Maize Disease Using  Random Forest Classification  Algorithm",
        "Survey of Data Mining in Cloud  Computing Environment",
        "Survey paper on big data processing and technologies ",
        "An analysis on use of big data in  cloud computing environment ",
        "Cloud Computing Security Issues  and Challenges",
        "Security Analyzing in Unix for  Cloud Computing Environment",
        "Cloud Based College management  information System for Autonomous institute",
        "Analysis of Cloud Computing in  Higher Education",
        "Security in Cloud Environment ",
        "Performance Improvement of Software as a Service and Platform  as a Service in Cloud Computing  Solution",
        "Analysis of Cloud Computing  Security Issues in Software as a  Service",



        
    ],
    "Journal/Conference": [
       "Publisher:Springer – ICRAMSITA 2025",
        "Publisher:Springer – ICRAMSITA 2025",
        "Publisher:IEEE – ICTBIG 2024",
        "Publisher:Springer - IDBA-2024",
        "Publisher:Springer - iBCD-2024",
        "Publisher:Soybean  Research Journal, 2004",
        "Publisher:FUZZY SYSTEMS AND SOFT COMPUTING,(UGC Care Listed Journal),2024 ",
        "Publisher:Science & Technology Journal,(UGC Care Listed Journal),2024 ",
        "Publisher:FUZZY SYSTEMS AND SOFT COMPUTING,(UGC Care Listed Journal),2021 ",
        "Publisher:Science & Technology Journal,(UGC Care Listed Journal),2020 ",
        "Publisher:IEEE, ICCAMS, 2023",
        "Publisher: IEEE, ICCEBS, 2023",
        "Publisher: IEEE, ICCEBS, 2023",
        "Publisher: IEEE, ICCAMS, 2023",
        "Publisher: IEEE, ICICACS, 2023",
        "Publisher: Journal of Data Acquisition and Processing,2023",
        "Publisher: IEEE,IIHC, 2022",
        "Publisher:Journal of Emerging Technologies and Innovative Research,(UGC Care Listed Journal),2018 ",
        "Publisher: IEEE , ICACITE,2022",
        "Publisher: IEEE, ICCCT,2021",
        "Publisher: IEEE, ICACITE,2022",
        "Publisher:International Journal of Health Sciences,2022,Scopus",
        "Publisher:Design Engineering,2022",
        "Publisher:Juni Khyat,UGC Care Group I Listed Journal, 2020",
        "Publisher: Turkish Journal of Computer and  Mathematics Education,2021 ",
        "Publisher: Journal of Emerging Technologies and  Innovative Research,2014",
        "Publisher:Journal of Emerging Technologies and  Innovative Research,2019",
        "Publisher: Global journal of engineering science and  research,2018",
        "Publisher: International Journal of Scientific Research  in Computer Science and Engineering,2014",
        "Publisher: International Journal of Innovative Research  in Computer and Communication Engineering,2015",
        "Publisher: International Research Journal of  Engineering and Technology,2014",
        "Publisher: International Journal of Advanced Research  in Computer Science and Software Engineering, 2015",
        "Publisher:International Journal of Scientific Research  in Computer Science and Engineering, 2014",
        "Publisher: International Journal of Scientific Research in Computer Science and Engineering, 2013",
        "Publisher: International Journal of Scientific Research  in Computer Science and Engineering,2014"

       
    ]
}

df = pd.DataFrame(publications)
st.table(df)

import streamlit as st
import pandas as pd

st.subheader("Granted Patent From Australia, Germany, and Canada")
patents = {
    "S. No.": [1, 2, 3, 4, 5, 6],
    "Year": [2020, 2020, 2021, 2021, 2021, 2021],
     "Patent No.":[2020102637,202141023045, 202141020637, 202141031766, 202141031766, 2021105407],
    "Title": [
        "A TECHNIQUE FOR TRAFFIC PREDICTION AND CONGESTION CONTROL IN IOT NETWORKS USING MACHINE LEARNING.",
        "A SYSTEM AND METHOD FOR ANALYZING DYNAMIC OUT-OF-HOME ADVERTISING BASED ON REAL-TIME VIEWERS BIOMETRIC INFORMATION.",
        "A SYSTEM FOR CONSUMPTION OF BACKDRAFT FORCE ENERGY FROM TRAIN STATIONS.",
        "A SYSTEM AND METHOD FOR MINING TRAFFIC PATTERNS OF IOT DEVICES IN EDGE NETWORKS.",
        "IOT BASED PRODUCTION OF ENVIRONMENT FRIENDLY BIO-FUEL FROM RENEWABLE RESOURCES.",
        "UTILITY BASED WEB CONTENT MINING APPROACHES."
    ],
    "Patent Link": [
        "http://pericles.ipaustralia.gov.au/ols/auspat/quickSearch.do?queryString=2020102637&resultsPerPage=",
        "https://ipindiaservices.gov.in/PatentSearch/PatentSearch/ViewApplicationStatus",
        "https://ipindiaservices.gov.in/PatentSearch/PatentSearch/ViewApplicationStatus",
        "https://ipindiaservices.gov.in/PatentSearch/PatentSearch/ViewApplicationStatus",
        "http://pericles.ipaustralia.gov.au/ols/auspat/applicationDetails.do?applicationNo=2021104265",
        "http://pericles.ipaustralia.gov.au/ols/auspat/applicationDetails.do?applicationNo=2021105407"
    ]
}

df_patents = pd.DataFrame(patents)

# Display the table
st.dataframe(df_patents)

st.subheader("Utility Patents Published")
import streamlit as st
import pandas as pd

import pandas as pd

import pandas as pd

# Create the dataframe
data = {
    "SN": list(range(1, 31)),
    "Year": [
        2021, 2021, 2021, 2021, 2021, 2022, 2022, 2022, 2022, 2022,
        2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022,
        2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2022, 2023
    ],
    "Title": [
        "AN IOT BASED SYSTEM FOR EMERGENCY HEALTHCARE",
        "METHODOLOGY FOR IMPLEMENTATION ONLINE CLASSROOM PLATFORM LEARNING TECHNIQUE",
        "MACHINE LEARNING APPROACH TO VALIDATE THE AUTHENTICITY OF NEWS USING NATURAL LANGUAGE PROCESSING",
        "AI AND WIRELESS BASED SMART DRUG PRESCRIPTION MANAGEMENT FOR AUTONOMOUS DRUG DELIVERY SYSTEM",
        "ML & BIG DATA-BASED CLOUD COMPUTING CONSTRUCTION ASSESSMENT SYSTEM FOR ANDROID APPLICATIONS",
        "ML BASED BUILDING FACIAL EMOTION DETECTION MODEL USING CNN",
        "MULTIPLE SENSORS-BASED SYSTEM FOR DETECTION OF BREAST CANCER USING CNN MACHINE LEARNING MODEL",
        "INDUSTRY 4.0 BASED ML AND INTERNET OF THINGS FOR OBSERVING AND SAFEGUARD THE ENERGY METER OVER INTERNET",
        "AMBULATORY ASSISTIVE DEVICE FOR VISUALLY IMPAIRED PERSON USING ARTIFICIAL INTELLIGENCE WITH ASSISTANCE IN MAP NAVIGATION",
        "MULTI-AGENT TOPOLOGY FOR AN ENERGY-EFFICIENT BUILDING STRUCTURE WITH ARTIFICIAL INTELLIGENT",
        "CLASSIFICATION OF DISEASES IN GLORIOSASUPERBA PLANT USING DEEP LEARNING SCHEME",
        "FACIAL EMOTION DETECTION USING SEMI-SUPERVISED MODIFIED SELF ORGANIZING FEATURE MAP NEURAL NETWORK METHOD",
        "SYSTEM TO ANALYSIS OF ADVERTISEMENTS ON ONLINE VIDEO SHARING PLATFORM FOR DIGITAL MARKETING THROUGH MACHINE LEARNING TO REACH MASS AUDIENCES",
        "DESIGNING A WSN PLATFORM FOR LONG TERM ENVIRONMENTAL MONITORING FOR IOT APPLICATIONS",
        "METHOD AND PROCESS TO IMPROVE THE DIGITAL EDUCATION SYSTEM",
        "MACHINE LEARNING AND ARTIFICIAL INTELLIGENCE BASED ON FEEDBACK SYSTEM FOR EDUCATIONAL INSTITUTIONS",
        "IMAGE REGISTRATION AND RECOGNITION OF BRAIN IMAGES CAPTURED USING MULTIPLE MODALITIES FOR EARLY DETECTION",
        "WOMEN ENTREPRENEURSHIP CHALLENGES, PLANNING AND STRATEGY FOR SUSTAINABLE GROWTH IN INDIA",
        "IoT BASED PATIENT MONITORNING SYSYTEM USING SENSORS TO DETECT, ANALYSE AND MONITOR TWO PRIMARY VITAL SIGNS",
        "DEVELOPMENT OF AN IoT BASED HEALTH MONOTORING SYSTEM FOR E HEALTH",
        "IoT BASED WEARABLE DEVICE TO MONITOR THE SIGNS OF QUARANTINED REMOTE PATIENTS OF COVID-19",
        "IoT BASED REMOTE PATIENT HEALTH MONITORING SYSTEM",
        "IoT BASED HEALTH MONITORING & AUTOMATED PREDICTIVE SYSTEM TO CONFRONT COVID-19",
        "DETECTION OF FAKE NEWS TEXT CLASSIFICATION ON COVID-19 USING DEEP LEARNING APPROACHES",
        "MACHINE LEARNING MODEL TO IDENTIFY FAKE NEWS FOR COVID-19 IN HEALTH CARE SYSTEM",
        "DETECTING FALSE INFORMATION IN MEDICAL AND HEALTH CARE DOMAINS",
        "DETECTION OF FALSE MEDICAL REPORT GENERATED BY MRI MACHINE OF X RAY USING MACHINE LEARNING TECHNIQUES",
        "HEALTHCARE MISINFORMATION DETECTION AND FACT-CHECKING: A NOVEL APPROACH",
        "METHOD FOR ASSESSING VALUE OF A POST IN A SOCIAL MEDIA GAMIFICATION PLATFORM",
        "IOT BASED HUMIDITY MONITORING SYSTEM USING MACHINE LEARNING APPROACH IN AGRICULTURE FIELD"
    ],
    "Patent No.": [
        "202111049864", "202211002249", "202221000671", "", "202141044813",
        "202241025598", "", "202241026790", "202211027079", "202241030964",
        "202241028705", "202221027213", "", "202241037755", "202211042293",
        "202211042296", "202211042584", "202211042576", "202211048061",
        "202211048060", "202211048063", "202211048059", "202211048062",
        "202211053246", "202211053232", "202211052606", "202211053949",
        "202211055173", "202231006716", "202341001498"
    ],
    "URL": ["[https://ipindiaservices.gov.in/PatentSearch/PatentSearch/ViewApplicationStatus]"] * 30
}

Utility_patents = pd.DataFrame(data)
# Display the DataFrame
# Display the table
st.table(Utility_patents)


st.write("🚧", "**Copyrights (Intellectual Properties)**")

# Data for the table
data = {
    "S. No.": [1, 2, 3],
    "Year": [2021, 2021, 2021],
    "Title": [
        "Human robotic interaction by using artificial intelligence.",
        "Effect of aluminum nano particles and Mechanical properties of medium density fiber.",
        "Secure demand side management using machine learning and internet of things."
    ],
    "URL": [
        "https://copyright.gov.in/SearchRoc.aspx",
        "https://copyright.gov.in/SearchRoc.aspx",
        "https://copyright.gov.in/SearchRoc.aspx"
    ]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Displaying the table in Streamlit
st.title("Copyrights (Intellectual Properties)")
st.table(df)
import streamlit as st
import pandas as pd
# Heading
st.title("🚧 Chapter in Books")
st.write('\n')
# Data
data = {
  
    "Year": [2023, 2023, 2022, 2022,2023,2023,2023],
    "Title": [
        "Introduction to Emotion Detection and Predictive Psychology in the Age of Technology",
        "Development of a framework to Integrate Smart Home and Energy Operation Systems to Manage Energy Efficiency through AI.",
        "Investigating Role of IoT in the Development of Smart Application for Security Enhancement.",
        "Cyber Security and Network Security.",
        "An Efficient Design and Comparison of Machine learning Model for Diagnosis of  Cardiovascular disease.",
        "Deep Learning-Based Regulation of Healthcare Efficiency and Medical Services.",
        " Integrating IoT Based Security with Image Processing",
    ],
    "URL": [
        "https://www.igi-global.com/books/open-access/",
        "https://onlinelibrary.wiley.com/",
        "https://link.springer.com/chapter/10.1007/978-3-031-04524-0_13",
        "https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119812555.ch11",
        "https://benthambooks.com/book/9789815136531/",
        "https://benthambooks.com/book/9789815136531",
        "https://novapublishers.com/shop/the-impact-of-thrust-technologies-on-image-processing/",

    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)
# Make URLs clickable
df['URL'] = df['URL'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
# Ensure column order
df = df[[ "Year", "Title", "URL"]]
# CSS for this specific table (scoped using #chapter-table)
st.markdown("""
    <style>
    #chapter-table table {
        width: 100%;
        border-collapse: collapse;
    }
    #chapter-table th:nth-child(1), #chapter-table td:nth-child(1) {
        width: 50px;  /* S. No. */
        white-space: nowrap;
    }
    #chapter-table th:nth-child(2), #chapter-table td:nth-child(2) {
        width: 60px;  /* Year */
        white-space: nowrap;
    }
    #chapter-table th, #chapter-table td {
        padding: 8px;
        text-align: left;
        font-size: 15px;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)

# Wrap table in a unique ID
st.markdown(f'<div id="chapter-table">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)


st.title("🚧 Authors  in Books")

import streamlit as st
import pandas as pd

st.write("📚", "**Books Published**")
st.write('\n')

# Book data
data = {
    "S. No.": [1, 2, 3],
    "Year": [2021, 2021, 2022],
    "Title": [
        "MEDICAL DIAGNOSIS USING ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING TECHNIQUES",
        "INTRODUCTION TO DEEP LEARNING",
        "MACHINE LEARNING USING PYTHON"
    ],
    "URL": [
        "https://www.flipkart.com/medical-diagnosis-using-artificial-intelligence-machine-learning-techniques/p/itm9996af8cf8aad",
        "https://www.amazon.in/Introduction-Deep-Learning-Subba-Polamuri/dp/9394339213/ref=sr_1_2?qid=1682149141&refinements=p_27%3AD.+Makhan&s=books&sr=1-2",
        "https://sipinternationalpublishers.com/product-detail.php?PID=ODc0"
    ]
}

# Create DataFrame and make URL clickable
df = pd.DataFrame(data)
df['URL'] = df['URL'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
df = df[["S. No.", "Year", "Title", "URL"]]

# Apply scoped CSS styling
st.markdown("""
    <style>
    #books-table table {
        width: 100%;
        border-collapse: collapse;
    }
    #books-table th:nth-child(1), #books-table td:nth-child(1) {
        width: 50px;  /* S. No. */
        white-space: nowrap;
    }
    #books-table th:nth-child(2), #books-table td:nth-child(2) {
        width: 60px;  /* Year */
        white-space: nowrap;
    }
    #books-table th, #books-table td {
        padding: 8px;
        text-align: left;
        font-size: 15px;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)

# Render table inside scoped div
st.markdown(f'<div id="books-table">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)


st.title("👩‍💻Memberships/Awards")
import streamlit as st
import pandas as pd

st.write("🏅", "**Awards**")
st.write('\n')

# Awards data
data = {
    "S. No.": [1, 2],
    "Award": [
        "Young Researcher Award from MAA SHAKUMBARI TRUST, GREATER NOIDA, U.P., India",
        "Environmental Protection Awards by Global Foundation of Research and Development and DAVV, Indore. For excellent work for environment protection."
    ]
}

df = pd.DataFrame(data)

# Apply scoped CSS styling
st.markdown("""
    <style>
    #awards-table table {
        width: 100%;
        border-collapse: collapse;
    }
    #awards-table th:nth-child(1), #awards-table td:nth-child(1) {
        width: 50px;  /* S. No. */
        white-space: nowrap;
    }
    #awards-table th, #awards-table td {
        padding: 8px;
        text-align: left;
        font-size: 15px;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)

# Render table inside scoped div
st.markdown(f'<div id="awards-table">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)

import streamlit as st
import pandas as pd

st.write("📘", "**Memberships**")
st.write('\n')

# Memberships data
data = {
    "S. No.": list(range(1, 19)),
    "Memberships": [
        "Lifetime Member of Excel Research Management Association.",
        "ICPCT IEEE, International Conference as a Technical Program Committee member.",
        "Lifetime Member of International Association of Research and Developed Organization.",
        "Reviewer Board Member of Machine Learning Research.",
        "Reviewer Member of International Journal of Engineering Research & Technology.",
        "Reviewer Member of International Journal of Advanced Trends in Computer Applications (IJATCA).",
        "Reviewer Member of Journal of Computer Science Engineering and Information Technology Research (IJCSEIT).",
        "Member of Asia-Pacific Artificial Intelligence Association.",
        "Editorial Member of Prestigious International Journal of Recent and Innovation Trends.",
        "Editorial Board Member of SI International Journal of Artificial Intelligence (SIAI).",
        "Member of International Journal of Advance research in Science and Engineering.",
        "Member of Prestigious Journal International Journal of Innovative research in Science and Engineering.",
        "Reviewer Member of Journal of Emerging Technologies and Innovative Research.",
        "Member of International journal of creative research thought.",
        "Member of IAENG International Journal of Computer Science.",
        "Member of International Journal of science Technology and Management.",
        "Member of International Journal of Electrical & Electronics Engineering.",
        "Member of International Association of Research and Development Organization."
    ]
}

df = pd.DataFrame(data)

# Scoped CSS styling for this table
st.markdown("""
    <style>
    #memberships-table table {
        width: 100%;
        border-collapse: collapse;
    }
    #memberships-table th:nth-child(1), #memberships-table td:nth-child(1) {
        width: 50px;  /* S. No. */
        white-space: nowrap;
    }
    #memberships-table th, #memberships-table td {
        padding: 8px;
        text-align: left;
        font-size: 15px;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)

# Display the table inside a scoped div
st.markdown(f'<div id="memberships-table">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)

st.title("👩📘Resource Person")
st.write("🎙️", "**Expert Talks & Trainings**")
st.write('\n')

# Data for the table
data = {
    "S. No.": [1, 2, 3, 4, 5, 6, 7],
    "Year": [2025, 2025, 2023, 2022, 2022, 2020, 2020],
    "Title": [
        "Invited as expert talk on Scope of IT for Computer Science Students at Saint Paul College, Indore.",
        "Invited as expert talk on Scope of Enhancing The Programming Skills at Sage University.",
        "Invited as expert talk on Machine Learning at Sage University.",
        "Multivariate Analysis Trainer at Prestige Institute of Management And Research, Indore, M.P., India.",
        "Core Java Trainer at Government Maharani Laxmi Bai Girls Postgraduate College, Indore.",
        "One Day International Webinar Organized by Navyug Arts & Commerce College Jabalpur, India on title ”Scope of Employment after COVID-19 in Global Era” - 31 May 2020.",
        "One Day International Webinar Organized by Govt. P.G. College Bina, India on title “Aatm-Nirbhar Bharat and Possibilities of Employment” - 12 July 2020."
    ]
}

df = pd.DataFrame(data)

# Scoped CSS for this table only
st.markdown("""
    <style>
    #talks-table table {
        width: 100%;
        border-collapse: collapse;
    }
    #talks-table th:nth-child(1), #talks-table td:nth-child(1) {
        width: 60px;
        white-space: nowrap;
    }
    #talks-table th:nth-child(2), #talks-table td:nth-child(2) {
        width: 70px;
        white-space: nowrap;
    }
    #talks-table th, #talks-table td {
        padding: 8px;
        text-align: left;
        font-size: 15px;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)

# Display only this table with applied CSS
st.markdown(f'<div id="talks-table">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)


st.title("👩📘National/International Conference / Seminar/Webinar Attended")


import streamlit as st
import pandas as pd

st.write("🎓", "**Webinars & Conferences Attended**")
st.write('\n')

# Data for the table
data = {
    "S. No.": list(range(1, 20)),
    "Title": [
        "One Day National Webinar Organized by IEEE at KMEA Engineering College, Kerala, India on “IEEE - Enhancing Your Project Work and Research” at 18, May-2021.",
        "One Day International Webinar Organized by IEEE Student Branch-GSSS Institute of Engineering and Technology for Women, Mysuru in Association with IEEE Mysore Sub Section, and IEEE Bangalore on “Evolutionary Learning and its Engineering Applications” on 21 May 2021.",
        "One Day National Webinar Organized IEEE Circuits and Systems (CAS) Society Bangalore Chapter, India on “Anti-virus hardware: Exploring the new domain in system security” at 26, June-2021.",
        "One Day National Webinar Organized by Certified Handwriting Analyst, on the title “Secrets in your Handwriting” on 15 May 2021.",
        "One Day National Webinar Organized by IEEE Information Theory Society (ITS) Bangalore Chapter on “IOT Based Monitoring Systems” on 22 May 2021.",
        "One Day National Webinar Organized by IEEE Information Theory Society (ITS) Bangalore Chapter on “Indoor Localisation in Wireless Sensor Network” on 23 May 2021.",
        "One Day National Webinar Organized by Soundarya Institute of Management & Science, Bangalore University, on the title “Professionalism among faculty members in higher education” on 24th May 2021.",
        "One Day National Workshop organized by Cognizance Academia (Registered under Govt. of India) on \"Digital Devices: Safety & Security\" on 23 May, 2021.",
        "One Day National Workshop organized by KPR Institute of Engineering and Technology, On the title “Hands on Training Statistics using R- programming\" on 22-May, 2021.",
        "One Day National Workshop Organized by Military Institute of Science and Technology Mirpur, Dhaka IEEE Student Branch on the title “Machine Learning: The Beginning” 24 May 2021.",
        "One Day National Webinar Organized by IEEE Information Theory Society (ITS) Bangalore Chapter on “Machine Learning for Wireless Communication” on 8 June 2021.",
        "One Day National Webinar Organized by IEEE Information Theory Society (ITS) Bangalore Chapter on the title “Advancements in Speech and Audio Quality Assessment” 13 July 2021.",
        "One Day National Webinar Organized by Department of Mathematics, St. Joseph’s Institute of Technology, Chennai on “Application of Grammar Systems to Cryptography” on 22nd June 2020.",
        "One Day National Webinar Organized by Govt. Home Science PG Lead College on “Impact of GST and role played by it in Indian Economy” on 10 July 2020.",
        "National Conference Organized by M.B. Harris College of Arts & A.E.Kalsekar College of Commerce & Management, Burhan Chowk, Nawayat Nagar on the title “Minding our minds in Current scenario - How to manage yourself during this pandemic” on 20th May 2020.",
        "National Conference Organized by Christian Eminent College, Indore on March 16, 2019.",
        "National Conference Organized by Christian Eminent College, Indore on March 3, 2017.",
        "National Conference Organized by Christian Eminent College, Indore on March 15, 2015.",
        "National Conference Organized by Christian Eminent College, Indore on March 5, 2013."
    ]
}

df = pd.DataFrame(data)

# Apply scoped style
st.markdown("""
    <style>
    #webinars-table table {
        width: 100%;
        border-collapse: collapse;
    }
    #webinars-table th:nth-child(1), #webinars-table td:nth-child(1) {
        width: 60px;
        white-space: nowrap;
    }
    #webinars-table th, #webinars-table td {
        padding: 8px;
        text-align: left;
        font-size: 15px;
        vertical-align: top;
    }
    </style>
""", unsafe_allow_html=True)

# Render the table with scoped ID
st.markdown(f'<div id="webinars-table">{df.to_html(escape=False, index=False)}</div>', unsafe_allow_html=True)

st.title("👩📘FDP/WORKSHOP ATTENDED")


import streamlit as st
import pandas as pd

# Data
data = [
    ["1", "Six Days FDP Organized by E & ICT Academy, IIT Kanpur ( A Joint initiative of MeitY & IIT Kanpur), on the title 'IOT & Drone' 27-02-2023 to 04-03-2023."],
    ["1", "Three Week International FDP Organized by K L University, University in Guntur, Andhra Pradesh, India on the title 'Research perspective on AI, ML, Data Science & IOT' on 17 May to 5 June 2021."],
    ["2", "Five Days International FDP Organized by Krishna Engineering College in Ghaziabad, Uttar Pradesh, on the title 'Future and Challenges in Engineering and Technology' on 14-18 May 2021."],
    ["3", "Two Day International FDP Organized by A2Z Edu Learning Hub LLP, on the title 'Theory Building & Data Analysis in Research' on 29-30 May 2021."],
    ["4", "Two Day Workshop Organized by IEEE AISSMS IOIT Student Branch Chapter in Collaboration with IEEE Silver Oak University on Title 'Innovation and IPR' on 24-25 May, 2021."],
    ["5", "One Week FDP Organized by Prestige Institute of Management, Dewas on the title 'Online Research Methodology workshop' on 24 -29 May 2021."],
    ["6", "Two Day International Workshop Organized by IEEE Information Theory Society (ITS) Bangalore Chapter on 'Machine Learning for Wireless Communication' on 8 June 2021."],
    ["7", "Five Days FDP Organized by Sri Venkateshwara College of Engineering and Technology, Puducherry on the title 'Impact of Covid on higher Education and Research initiatives' on 24-28 May 2021."],
    ["8", "Five Days FDP Organized by Sri Venkateshwara College of Engineering and Technology, Puducherry on the title 'Exploring Entrepreneurship & Startup opportunities' on 5-9 July 2021."],
    ["9", "Five Days FDP Organized by CMR Engineering College, Hyderabad on the title 'ML/DL BY USING COLAB AND KNIME A ROAD MAP' on 1 -5 June 2021."],
    ["10", "Five Days FDP Organized by St. Francis De Sales College, also known as SFS College, Nagpur, on the title 'Advance Teaching, Learning, Research Methodology and Innovations' on 1st June to 5th June, 2021."],
    ["11", "Five Days FDP Organized by Maturi Venkata Subba Rao (MVSR) Engineering College, Hyderabad, on the title 'Multi Technologies' on 27 June to 3rd July, 2021."],
    ["12", "Eight Days International FDP Organized by Patrician College of Arts and Science College in Chennai, Tamil Nadu, on the title 'Effective and Quality Research Writing' on 7 -15 June 2021."],
    ["13", "Seven Days International FDP Organized by Patrician College of Arts and Science College in Chennai, Tamil Nadu, on the title 'Strategies for Effective Classroom Teaching' on 26 July -1 August, 2021."],
    ["14", "AICTE Sponsored One Week Online STTP Organized by Matrusri Engineering College, Saidabad, Hyderabad on the title 'RECENT ADVANCE IN EV TECHNOLOGY' on 17-22 ,May,2021."],
    ["15", "Seven Days International FDP Organized by St. Martin's Engineering College Secunderabad, Telangana, India, on the title Phase-I 'Medical Image Processing & It’s Applications in Automated Disease Detection' 18th June to 24th June 2021."],
    ["16", "Seven Days International FDP Organized by St. Martin's Engineering College Secunderabad, Telangana, India, on the title Phase-II 'Medical Image Processing & It’s Applications in Automated Disease Detection' 20-26, May 2021."],
    ["17", "Five Days FDP Organized by Reva University Bengaluru Karnataka, India, on the title 'Literature and humanity' on 24-28 May 2021."],
    ["18", "Five Days International FDP Organized by Sri Guru Tegh Bahadur Khalsa College, Jabalpur, India on the title 'Emerging Trends in Teaching and Technology' on 16-20 May 2021."],
    ["19", "Four Days International Examination Conference Organized by Council of Examiners -India and SkillSlate Foundation, Pune powered by Zovy Studios, Pune 'Examination-IDEA 2021' on 8-11 June 2021."],
    ["20", "Five Days National FDP Organized by Nagindas Khandwa College in Mumbai, Maharashtra, India on the title 'Tools and technique for Excellent Doctoral Research' on 16-20 May 2021."],
    ["21", "Three Days National FDP Organized by Indian Institute of Management and Commerce on the title 'Research Methodology for Social Sciences' on 17-21 May 2021."],
    ["22", "Two Days International Webinar Organized by SLI International Webcasting Network on the title 'Role of Nanotechnology in Current Scenario' on 27-28 May, 2021."],
    ["23", "Ten Days Online Faculty Development Program Organized by Institute of Management Studies, Davv, Indore on the title 'Curriculum Review in the Light of NEP 2020: A Futuristic Perspective' on 5-16 ,July 2021."],
    ["24", "Three Days National Webinar Organized by National Institute of Disaster Management, MHRD India, on the Title 'Online Process Orientation Programme on Child Centric Disaster Risk Reduction' on 09-11 Aug 2021."],
    ["25", "Five Days National FDP Organized by Toshniwal Arts, Commerce & Science College, India on the title 'Educational Video Creation: E -Content Development' on 11-13 May 2020."],
    ["26", "Six Days National FDP Organized by Acropolis Institute of Technology and Research, Indore, India on the title 'Data Science: Unfolding Layers of Knowledge (Phase I)' on 23-28 Nov, 2020."],
    ["27", "Five Days National Level E-Conference Organized by Council of Examiners, India and SkillSlate, Pune, Indore, India on the title 'National Examinations Transformation-2020' on 10-14 Aug, 2020."],
    ["28", "Three Days International E-Conference Organized by Government Vidarbha Institute of Science & Humanities, Amravati on the title 'Strategies & Challenges in Higher Education during COVID 19 Lockdown Period in India with reference to the World' on 15th - 17th May, 2020."]
]

# Creating a DataFrame
df = pd.DataFrame(data, columns=["ID", "Details"])

# Streamlit Table Display
st.title("Faculty Development Programmes and Workshops")
st.table(df)

st.title("👩📘Certificate Courses👩📘")

import streamlit as st
import pandas as pd

# Data
certificates = [
    ["1", "Certificate for Completion of R Language Training organized by Spoken Tutorial Project, IIT Bombay, funded by National Mission on Education through ICT, MHRD, Govt., of India. On May 2nd 2020."],
    ["2", "Beginner course to learn Machine learning Regression in Python organized by https://www.learnmall.in, on 20th May 2021."],
    ["3", "HANDS ON EXPERIENCE OF LATEX SOFTWARE by the Department of Applied Science & Humanities, PIEMR Indore (M.P.) on 10th May 2020."],
    ["4", "Certificate for PHP organized by SOLOLEARN on 29 April 2020."],
    ["5", "Certificate for JAVA organized by SOLOLEARN on 29 April 2020."],
    ["6", "Certificate course in Intellectual Property Rights (IPR), organized by Udemy on 16 Feb,2023."],
    ["7", "Certificate course in TensorFlow for Deep Learning with Python, organized by Udemy on 16 Feb,2023."]
]

# Creating a DataFrame
df_certificates = pd.DataFrame(certificates, columns=["ID", "Certification Details"])

# Streamlit Table Display
st.title("Certificates and Trainings")
st.table(df_certificates)

st.title("👩📘Machine learning, Deep learning, NLP and Computer Vision Project👩📘")

# Data
projects = [
    [1, "Building a system which automatic recognize plate number with OpenCV and Tesseract OCR", 
     "Our system recognition automatic number-plate. For that purpose we are using Tesseract OCR An Optical Character Recognition Engine (OCR Engine) to automatically recognize text in vehicle registration plates."],
    [2, "Face and Hand Landmarks Detection using Python", 
     "In this project we used Holistic model from mediapipe solutions to detect all the face and hand landmarks."],
    [3, "Building a Visual Similarity-based Recommendation System Using Python", 
     "Recommendation system help us for converting the shoppers to customers, engaging the customers, boosting sales and revenue, and delivering the most relevant content."],
    [4, "Deep style web application using transfer learning", 
     "Deep style is a transfer learning based neural style transfer web application that stylizes our image to one of the 4 styles available (at the moment)."],
    [6, "Face recognition of Mark Zuckerberg, Bill Gates and Mukesh Ambani using face_recognition and openCV", 
     "We used OpenCV and pillow library for detecting particular person image."],
    [7, "PAN card fraud detection using computer vision", 
     "The purpose of this project is to detect tampering/fraud of PAN cards using computer vision. This project will help the different organizations in detecting whether the Id i.e. the PAN card provided to them by their employees or customers, or anyone is original or not."],
    [8, "Fake news classifier", 
     "This project looks at building, training and evaluating neural networks to solve the fake news classification problem on Kaggle dataset. It uses Python and Keras."],
    [9, "Cartoonify Image with Machine Learning", 
     "Transform images into its cartoon. The objective of this machine learning project is to CARTOONIFY the images. Thus, we will build a python application that will transform an image into its cartoon using machine learning libraries."],
    [10, "Emojify – Create your own emoji with Python", 
     "The objective of this machine learning project is to classify human facial expressions and map them to emojis. We will build a convolution neural network to recognize facial emotions. Then we will map those emotions with the corresponding emojis or avatars."],
    [11, "Loan Prediction using Machine Learning", 
     "The idea behind this ML project is to build a model that will classify how much loan the user can take. It is based on the user’s marital status, education, number of dependents, and employments. We can build a linear model for this project."],
    [12, "Housing Prices Prediction using Machine learning", 
     "The dataset has house prices of the Boston residual areas. The expense of the house varies according to various factors like crime rate, number of rooms, etc. It is a good ML project for beginners to predict prices on the basis of new data."],
    [13, "MNIST Digit Classification using Machine Learning", 
     "The MNIST digit classification python project enables machines to recognize handwritten digits. This project could be very useful for computer vision. Here we need to use MNIST datasets to train the model using Convolutional Neural Networks."],
    [14, "Stock Price Prediction using Machine Learning", 
     "There are many datasets available for the stock market prices. This machine learning beginner’s project aims to predict the future price of the stock market based on the previous year’s data."],
    [15, "Fake News Detection using Machine learning and Natural language processing", 
     "Fake news spreads like a wildfire and this is a big issue in this era. We can learn how to distinguish fake news from a real one. We can use supervised learning to implement a model like this."],
    [16, "Music Genre Classification using Machine Learning", 
     "The idea behind this python machine learning project is to develop a machine learning project and automatically classify different musical genres from audio."],
    [17, "Bitcoin Price Predictor using Machine learning", 
     "The bitcoin price predictor is a useful project. Blockchain technology is increasing and there are many digital currencies rising. This project will help you predict the price of the bitcoin using previous data."],
    [18, "Uber Data Analysis Project using machine learning", 
     "The project can be used to perform data visualization on the uber data. The dataset contains 4.5 million of uber pickups in the New York city. This many data needs to be represented beautifully in order to analyse the rides so that further improvements in the business can be made."],
    [19, "Personality Prediction Project Using supervised machine learning", 
     "The Myers Briggs Type Indicator is a personality type system that divides a person into 16 distinct personalities based on introversion, intuition, thinking and perceiving capabilities. We can identify the personality of a person from the type of posts they put on social media."],
    [20, "Credit Card Fraud Detection using machine learning", 
     "Companies that involve a lot of transactions with the use of cards need to find anomalies in the system. The project aims to build a fraud detection model on credit cards."],
    [21, "Sign Language Recognition with Machine Learning", 
     "A lot of research has been done to help people who are deaf and dumb. In this sign language recognition project, we create a sign detector that detects sign language. This can be very helpful for the deaf and dumb people in communicating with others."],
    [22, "Customer Segmentation using Machine Learning", 
     "Customer segmentation is a technique in which we divide the customers based on their purchase history, gender, age, interest, etc. It is useful to get this information so that the store can get help in personalize marketing and provide customers with relevant deals. With the help of this project, companies can run user-specific campaigns and provide user-specific offers rather than broadcasting same offer to all the users."],
    [23, "Sentiment Analysis using Machine Learning and deep learning", 
     "Sentiment analysis is the process of analysing the emotion of the users. We can categorize their emotions as positive, negative, or neutral. It is a great project to understand how to perform sentiment analysis and it is widely being used nowadays. This is one of the most popular machine learning projects."],
    [24, "Speech Emotion Recognition using Machine Learning", 
     "This is one of the best machine learning projects. The speech emotion recognition system uses audio data. It takes a part of speech as input and then determines in what emotions the speaker is speaking. We can identify different emotions like happy, sad, surprised, angry, etc. This project could be helpful for identifying customer emotions during the call with the call centre."],
    [25, "Online Grocery Recommendation using Collaborative Filtering", 
     "Collaborative filtering is a great technique to filter out the items that a user might like based on the reaction of similar users. A grocery recommendation system would be a great project to make customers realize what they would like in their baskets."],
    [26, "Movie Recommendation System Using Machine Learning", 
     "Recommendation systems are everywhere, be it an online purchasing app, movie streaming app or music streaming. They all recommend products based on their targeted customers. A movie recommendation system is an excellent project to enhance your portfolio."],
    [27, "Automatic License Number Plate Recognition System", 
     "The objective of this machine learning project is to detect and recognize the license number plate of a vehicle and read the license numbers printed on the plate. This could be a good application for security scans, traffic monitoring, etc."],
    [28, "Web Application for Fake content Scrapping using machine learning", 
     "We can scrapped information using these scrapper form websites like https://www.snopes.com/"]
]

# Creating DataFrame
df_projects = pd.DataFrame(projects, columns=["S. No.", "Title", "Objective"])

# Streamlit Table Display
st.title("Machine Learning Projects")
st.table(df_projects)
st.title("👩📘Work Experience👩📘")

import streamlit as st
import pandas as pd

# Data
institutions = [
    [1, "Indian Institute of Soybean Research (IISR), Indore, M.P., India", "Young Professional –(IT)", "OCT-2022", "Till Date", "Ongoing"],
    [2, "ORLANDO ACADEMY (CDAC ACTS Authorized Training Centre)", "Data science visiting lecturer", "OCT-2023", "Till Date", "Ongoing"],
    [3, "Institute of Analytics, USA", "Adjunct Faculty", "Sep-2022", "Till Date", "Ongoing"],
    [4, "Christian Eminent College, Academy of Management Professional Education & Research, Indore, Madhya Pradesh, India", "Full Time Faculty", "FEB-2012", "OCT-2022", "10 Years"],
    [5, "Christian Eminent College, Academy of Management Professional Education & Research, Indore, Madhya Pradesh, India", "Visiting lecturer", "OCT-2022", "MAY-2023", "8 Months"],
    [6, "Prestige Institute of Management And Research, Indore, M.P., India", "Visiting lecturer", "Sep-2022", "Till Date", "2 Months"],
    [7, "School of Data Science, Devi Ahilya Vishwavidyalaya, University in Indore, Madhya Pradesh, India", "Visiting lecturer", "Feb-2020", "Till Date", "Ongoing"],
    [8, "School of Biotechnology, Devi Ahilya Vishwavidyalaya, University in Indore, Madhya Pradesh, India", "Visiting lecturer", "Aug-2022", "Till Date", "Ongoing"],
    [9, "Government Holkar Science College, College in Indore, Madhya Pradesh, India", "Guest Lecturer", "Jan-2011", "Sep-2011", "8 Months"],
    [10, "InstaDotAnalytics", "Full Stack Developer (Part time)", "Feb-2019", "June-2022", "3 Years"],
    [11, "League IT Solutions, Noida, UP, India", "Software Developer", "2010", "2011", "1 Year"]
]

# Creating DataFrame
df_institutions = pd.DataFrame(institutions, columns=["S. No.", "Institution", "Designation", "From", "To", "Experience"])

# Streamlit Table Display
st.title("Professional Experience")
st.table(df_institutions)

# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
