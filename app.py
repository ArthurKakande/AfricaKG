# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 20:37:49 2023

@author: Probook 450 G7
"""

import streamlit as st
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.plugins.sparql import prepareQuery

# Create an RDF namespace for your ontology
your_namespace = Namespace("Your_Ontology_Namespace_URI")

# Load your RDF knowledge graph from an RDF/XML file
g = Graph()
g.parse("africa_knowledge_graph.rdf", format="xml")  # Replace with your RDF/XML file path

# Streamlit UI
st.title("The Africa Knowledge Graph Query Tool")

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
