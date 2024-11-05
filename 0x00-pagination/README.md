The 0x00 Pagination assignment is intended to help you learn and apply the following concepts:

Basic Pagination with Page and Page Size: You will implement a simple pagination system where the dataset is divided into "pages" based on a page number and page size, similar to how websites present limited items on a page. This will help you understand how to split data efficiently and serve portions of it based on user requests.

Hypermedia Pagination with Metadata: You'll implement a method that provides metadata along with paginated data, such as the current page number, page size, total pages, and links to the previous and next pages (HATEOAS, or Hypermedia as the Engine of Application State). This is useful in REST API design to provide clients with additional information, allowing them to navigate through paginated data seamlessly.

Deletion-Resilient Pagination: You will handle data deletions between queries in such a way that paginated results remain consistent and no items are missed. This teaches you how to manage datasets that may change dynamically, a common scenario in real-world applications where data can be modified or removed between user requests.

By working on this assignment, you’ll gain practical experience with:

Structuring APIs for efficient data retrieval.
Managing large datasets in a performant way.
Designing APIs that offer a smooth user experience, even when data changes.
Implementing type-annotations, code documentation, and other code quality requirements in Python.
This assignment reinforces backend concepts like data management and efficient querying while ensuring compliance with API standards for pagination.
