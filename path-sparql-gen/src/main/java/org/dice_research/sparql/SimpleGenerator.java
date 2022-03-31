package org.dice_research.sparql;

import java.util.Collection;

import org.apache.jena.graph.Triple;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.ResourceFactory;
import org.apache.jena.rdf.model.Statement;
import org.apache.jena.rdf.model.impl.StatementImpl;
import org.dice_research.fc.data.QRestrictedPath;
import org.dice_research.fc.paths.EmptyPredicateFactory;
import org.dice_research.fc.paths.IPathSearcher;
import org.dice_research.fc.paths.search.SPARQLBasedSOPathSearcher;

public class SimpleGenerator {

    public static final Property DUMMY_PROPERTY = ResourceFactory.createProperty("http://example.org/property");

    protected EmptyPredicateFactory factory = new EmptyPredicateFactory();
    protected Model dummyModel = ModelFactory.createDefaultModel();

    public String generateSparqlQuery() {
        IPathSearcher searcher = new SPARQLBasedSOPathSearcher(null, 0, null);

        searchPaths(searcher, null, null, null);

        return null;
    }

    protected Collection<QRestrictedPath> searchPaths(IPathSearcher searcher, String subject, String predicate, String object) {

        // TODO Add subject and object here
        Statement s = new StatementImpl(DUMMY_PROPERTY, DUMMY_PROPERTY, DUMMY_PROPERTY);

        Triple triple = new Triple(null, DUMMY_PROPERTY.asNode(), null);
        factory.generatePredicate(null);

        searcher.search(null, null, null);
        return null;
    }

}
