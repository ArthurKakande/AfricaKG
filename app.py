# -*- coding: utf-8 -*-
"""
"""

import streamlit as st
import datetime
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.plugins.sparql import prepareQuery

# Create an RDF namespace for your ontology
your_namespace = Namespace("http://www.africaknowledgegraph.com#")

# Load your RDF knowledge graph from an RDF/XML file 
g = Graph()
g.parse("Africaknowledgegraph.rdf", format="xml")  # Replace with your RDF/XML file path


# Set page title and icon
st.set_page_config(
    page_title="Africa Knowledge Graph",
    page_icon="🌍",
)

# Introductory text for the Home page
intro_text = """
## Welcome to the Africa Knowledge Graph!

The Africa Knowledge Graph is a comprehensive repository of structured information, offering valuable insights into diverse aspects of the African continent. Within this knowledge graph, you will find meticulously organized data pertaining to:

- **African Nations:** Discover detailed profiles of countries across Africa, from Algeria to Zimbabwe, encompassing their history, culture, and socio-economic indicators.

- **African Capitals:** Explore the vibrant capitals of African countries, from bustling Cairo to scenic Cape Town, and gain a deeper understanding of their significance.

- **African Organizations:** Learn about key organizations and institutions shaping Africa's future, such as the African Union, United Nations agencies, and regional bodies.

- **Economic Development:** Access data on economic development initiatives, trade agreements, and projects aimed at fostering growth and prosperity across the continent.

- **Cultural Heritage:** Dive into Africa's rich cultural heritage, including traditions, languages, and historical landmarks that define its unique identity.

- **Environmental Initiatives:** Stay informed about environmental conservation efforts, wildlife conservation, and sustainable practices contributing to Africa's ecological well-being.

- **Collaborative Opportunities:** The Africa Knowledge Graph is a collaborative platform. To contribute or access additional features, please reach out through Twitter @ArthurKakande.

Our query tool provides a seamless experience for exploring this wealth of knowledge. You can access the query service at using the SPARQL box below. For data exports, reach out through Twitter @ArthurKakande for a link to the original ontology that you can query with your preferred tool of choice.

We are committed to continuously expanding this knowledge resource. If you are interested in collaborating or have inquiries, please reach out to us through Twitter @ArthurKakande.

For feature requests and bug reports, kindly use our the Twitter account provided above. Join us on this journey of discovery and exploration, where data science meets the African continent's real-world impact.

## The Query Box!

"""

# About Us page content
about_us_text = """

The Africa Knowledge Graph has been meticulously curated and developed by dedicated data scientists with a passion for unlocking the potential of data. Our mission is to bridge the gap between information and real-world impact.

**Your's truly,**                                                                                                                                                      
**The Finder's Lab**                                                                                                                                                                        
*(Extract, Analyze, Inform)*
"""

#The Finder's Lab is an African initiative using data science techniques to improve access to information, understand citizen feedback (on social media) on service delivery, etc, to facilitate actionable insights.

#We at The Finder's lab believe in the power of knowledge graphs to drive innovation and positive change.

#Feel free to reach out to The Finder's Lab to learn more about our work and contributions to the Africa Knowledge Graph.

# Footer with the last edit date
footer_text = f"""
---
*This page and graph were last edited on {datetime.date(2023, 9, 22)}*
"""

# Streamlit app layout
st.title("The Africa Knowledge Graph Query Tool")
st.sidebar.title("Navigation")

# Add navigation between tabs
page = st.sidebar.radio("Go to", ("Home", "About", "Query Box", "QA Box"))

if page == "Home":
    st.markdown(intro_text, unsafe_allow_html=True)
    # Input area for SPARQL query
    sparql_query = st.text_area("Enter your SPARQL Query:")

    # Function to execute SPARQL query
    def execute_query(query):
        try:
           results = g.query(query)
           return results
        except Exception as e:
           return str(e)

    # Execute the query and display results
    if st.button("Run Query"):
        if sparql_query:
            results = execute_query(sparql_query)
            st.subheader("Query Results:")
            for row in results:
                st.write(row)
        else:
            st.warning("Please enter a SPARQL query.")

elif page == "About":
    st.markdown(about_us_text, unsafe_allow_html=True)

st.sidebar.markdown(footer_text, unsafe_allow_html=True)


