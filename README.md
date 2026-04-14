# Cinctra

Cinctra is an embedded, constraint-first database that stores and validates claims about relationships, preserving truth—even when it is incomplete or conflicting.

## What is Cinctra?

Cinctra is an embedded database designed to model relationships with enforced correctness, not just storage. Instead of flattening data into rows or forcing premature resolution, Cinctra stores claims—assertions about entities and their relationships—alongside the constraints that govern them.

Cinctra exists at the intersection of two philosophies:

- **Embedded, local-first databases** that prioritize simplicity and portability (as exemplified by SQLite)
- **Semantic data models** that treat relationships and constraints as first-class (as explored by TypeDB)

Rather than choosing between them, Cinctra combines these ideas into a constraint-first system that preserves truth—even when it is incomplete or conflicting.

## Terminology

- **Entity** — a distinct thing in the world (a person, a place, a document)
- **Relation** — a typed connection between entities (parent-of, born-in, authored-by)
- **Claim** — a sourced assertion that a relation holds ("Source X says A is parent of B"). Claims are never bare assertions—information doesn't just manifest, it has a source, even if that source is the author's own knowledge.
- **Constraint** — a declared rule governing what relations are valid ("a person has exactly two biological parents")
- **Invariant** — the system's active enforcement of a constraint; the guarantee that violations are detected and surfaced, not silently swallowed

## Non-goals

- **Not a general-purpose RDBMS** — Cinctra doesn't aim to replace Postgres or SQLite for arbitrary workloads
- **Not a graph database** — relationships are first-class, but this isn't a property graph or triple store
- **Not a query engine** — no SQL, no Datalog as a primary interface
- **Not a domain-specific tool** — genealogy is the first use case, but Cinctra is not a GEDCOM parser or genealogy application

## First use case: genealogy with conflicting evidence

Multiple sources may disagree about a birth date, parentage, or even whether two records refer to the same person. Cinctra preserves all claims and surfaces the contradictions rather than forcing premature resolution. Genealogy is an application of Cinctra, not a domain restriction—any domain with sourced, potentially conflicting relational data is a fit.
