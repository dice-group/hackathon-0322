package org.dice_research.sparql;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import org.aksw.sparql2nl.naturallanguagegeneration.SimpleNLGwithPostprocessing;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.Syntax;
import org.dllearner.kb.sparql.SparqlEndpoint;

/**
 * https://github.com/AKSW/SPARQL2NL/blob/master/src/test/java/org/aksw/sparql2nl/SPARQL2NLTest.java
 */
public class SPARQLVerbalizer {
  private SparqlEndpoint ep;
  private SimpleNLGwithPostprocessing snlg;
  
  public SPARQLVerbalizer(String sparqlEndpoint) {
    try {
      ep = new SparqlEndpoint(new URL(sparqlEndpoint));
    } catch (MalformedURLException e) {
      e.printStackTrace();
    }
    snlg = new SimpleNLGwithPostprocessing(ep);
  }
  
  public Map<String, String> getNLFromSPARQL(String... queries) {
    Map<String, String> queries2NL = new HashMap<>();
    for (String q : queries) {
      Query sparqlQuery = QueryFactory.create(q, Syntax.syntaxARQ);
      queries2NL.putIfAbsent(q, snlg.getNLR(sparqlQuery));
    }
    return queries2NL;
  }

  public static void main(String[] args) {
    String query = "PREFIX dbo: <http://dbpedia.org/ontology/> "
        + "PREFIX res: <http://dbpedia.org/resource/> "
        + "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "
        + "SELECT DISTINCT ?uri WHERE { res:Skype dbo:developer ?uri. }";
    
    SPARQLVerbalizer verb = new SPARQLVerbalizer("https://synthg-fact.dice-research.org/sparql");
    verb.getNLFromSPARQL(query);
  }

}
