## Composition vs Inheritance

Inheritance can be used to share methods across multiple classes. However it introduces very strong coupling. A change in the parent class would effect all child classes downstream. Bad practice to try using inheritance to separate things.

Composition can allow you to share functionality without resulting in such high amount of coupling. This is done by connecting different classes via instance variables. Reduces coupling, lowers duplication, and enables reusability.

## Cohesion

Can also be understood as single responsibility principle. Every function or method should have one responsibility. Every class should be a collection of methods that handle a specific idea. Complex logic should be created through the interaction of these units.

## Low Coupling

Coupling is the degree in which functions and class need each other. High coupling occurs when a change in one function requires a change in other functions. Low coupling allows you to change code without breaking other parts of your system, and enables you to reuse your code more often.

Best practice to follow is principle of least knowledge. Create units that only talk to and understand closely related units. 


- content coupling : one method/function directly modifies data in another class
- global coupling : different functions share the same global data
- external coupling : application depends on external api
- control coupling : one module controls the flow of another part of the code
- stamp coupling : data structure needlessly coupled, ex module depend on a structure even though it doesn't use the structure details
- data coupling : when methods share data via parameters
- import coupling : importing a module
- message coupling : connect pieces of program together via events, like in gui interfaces

## Dependency Injection

Make a class independent of its dependencies by separating the creation of an object and its usage. Done by passing objects to a class that uses it, rather than having the class responsible for creating it. Leads to lower coupling.

Also makes it easier to isolate pieces of a program. Which can be useful when testing. As mocks of dependencies can be easily created and passed to a class.
