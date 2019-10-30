---
title: Getting started
path: /docs/
---

# Getting started

Strawberry is a Python library for building [GraphQL APIs](https://graphql.org).

This guide will help you to create your first GraphQL API using Strawberry.

## Installation

To install Strawberry you can use your favourite dependency manager (pip, poetry or pipenv). In this guide we’ll assume you’re working in a virtual env and using pip. To install Strawberry run the following command:

```shell
pip install strawberry-graphql
```

## Creating our first schema

Every GraphQL API has a schema, which defines all the types and fields available in the API. There’s only one type that’s mandatory in a GraphQL API: `Query`. It this we are all the data of our API will come from.

Strawberry takes a code-first approach, where you use code to define the schema, as opposed to a schema-first approach where you write the schema first.

Strawberry uses [type hints](https://docs.python.org/3/library/typing.html) to declare the types for the GraphQL fields.

Let’s create our first type. As mentioned we need to create a `Query` type. To keep this example short let’s have only one field, called `hello`, that always returns “hello world”.

```python
import strawberry

@strawberry.type
class Query:
    hello: str = "hello world"
```
