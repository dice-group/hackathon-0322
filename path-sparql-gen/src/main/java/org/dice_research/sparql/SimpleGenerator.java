package org.dice_research.sparql;

import java.util.Arrays;
import java.util.Collection;
import java.util.concurrent.TimeUnit;

import org.aksw.jena_sparql_api.core.QueryExecutionFactory;
import org.aksw.jena_sparql_api.delay.core.QueryExecutionFactoryDelay;
import org.aksw.jena_sparql_api.http.QueryExecutionFactoryHttp;
import org.aksw.jena_sparql_api.timeout.QueryExecutionFactoryTimeout;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.ResourceFactory;
import org.apache.jena.rdf.model.Statement;
import org.apache.jena.rdf.model.impl.StatementImpl;
import org.apache.jena.vocabulary.RDF;
import org.dice_research.fc.data.QRestrictedPath;
import org.dice_research.fc.paths.EmptyPredicateFactory;
import org.dice_research.fc.paths.IPathSearcher;
import org.dice_research.fc.paths.search.SPARQLBasedSOPathSearcher;
import org.dice_research.fc.sparql.filter.EqualsFilter;
import org.dice_research.fc.sparql.filter.NamespaceFilter;

public class SimpleGenerator {

    public static final Property DUMMY_PROPERTY = ResourceFactory.createProperty("http://example.org/property");
    public static final String ENDPOINT = "https://synthg-fact.dice-research.org/sparql";

    protected static final String[] FILTERED_PROPERTIES = new String[] {
            "http://dbpedia.org/ontology/wikiPageExternalLink", "http://dbpedia.org/ontology/wikiPageWikiLink" };

    protected EmptyPredicateFactory factory = new EmptyPredicateFactory();
    protected Model dummyModel = ModelFactory.createDefaultModel();

    public String generateSparqlQuery() {
        QueryExecutionFactory qef = null;
        try {
            qef = new QueryExecutionFactoryHttp(ENDPOINT);
            qef = new QueryExecutionFactoryDelay(qef, 100);
            qef = new QueryExecutionFactoryTimeout(qef, 30, TimeUnit.SECONDS, 30, TimeUnit.SECONDS);

            int maxPathLength = 2;
            IPathSearcher searcher = new SPARQLBasedSOPathSearcher(qef, maxPathLength, Arrays.asList(
                    new NamespaceFilter(new String[] { RDF.getURI() }, false), new EqualsFilter(FILTERED_PROPERTIES)));

            searchPaths(searcher, null, null);
        } finally {
            try {
                qef.close();
            } catch (Exception e) {
            }
        }
        return null;
    }

    protected Collection<QRestrictedPath> searchPaths(IPathSearcher searcher, String subject, String object) {
        Resource s = dummyModel.createResource(subject);
        Resource o = dummyModel.createResource(object);
        Statement stmt = new StatementImpl(s, DUMMY_PROPERTY, o);
        return searcher.search(s, factory.generatePredicate(stmt), o);
    }

}
